#!/usr/bin/env python3
"""Validate the RGBT paper list.

Checks (errors fail, warnings are reported):
- papers.csv schema: required fields non-empty, year in range, list/section/subsection legal
- titles unique; tags within the controlled vocabulary
- paper_link is a URL (warning for the known page-reference entries)
- generated files (README.md, bibliography.md, references.bib) are up to date with papers.csv
- every CSV title appears exactly once in README.md and bibliography.md; BibTeX entry count matches
- content warnings (never fail): DOI year vs catalogued year (journal issue-year
  exceptions listed in DOI_YEAR_EXCEPTIONS), arXiv DOIs in the doi column, and
  paper_link publisher domain inconsistent with the venue's publisher
Run:  python3 tools/validate.py   (exit code 1 on errors)
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate

ROOT = generate.ROOT
TAG_VOCAB = {
    "adapter", "aerial", "alignment", "benchmark", "conflict-aware", "corruption",
    "cross-attention", "degraded-modality", "detr", "distillation",
    "dual-stream", "dynamic-fusion", "efficiency", "ensemble", "evidential",
    "expert-routing", "foundation-model", "frequency-domain", "image-fusion",
    "lidar-camera", "mamba", "missing-modality", "modality-imbalance",
    "negative-fusion", "pedestrian", "quality-aware", "survey", "task-coupled",
    "test-time-adaptation", "test-time-intervention", "thermal-only-inference",
    "transformer", "yolo",
}

# Journal papers are catalogued by issue year; a DOI minted at early access can
# legitimately predate it by more than the one-year tolerance below. Keyed by title.
DOI_YEAR_EXCEPTIONS = {
    "Weakly Aligned Feature Fusion for Multimodal Object Detection":
        "DOI 10.1109/TNNLS.2021.3105143 minted at 2021 early access; catalogued by 2025 issue year (TNNLS vol. 36)",
}
ELSEVIER_VENUES = ("Pattern Recognition", "Information Fusion", "Neurocomputing",
                   "Expert Systems with Applications", "Image and Vision Computing")


def doi_year(doi):
    m = re.search(r"(?:^|[./])((?:19|20)\d{2})(?:[./]|$)", doi)
    return int(m.group(1)) if m else None


def venue_family(venue):
    if any(v in venue for v in ELSEVIER_VENUES):
        return "elsevier"
    if venue.startswith("IEEE"):
        return "ieee"
    if venue.startswith("ACM"):
        return "acm"
    return None


def link_family(url):
    if "ieeexplore.ieee.org" in url:
        return "ieee"
    if "sciencedirect.com" in url or "elsevier.com" in url:
        return "elsevier"
    if "dl.acm.org" in url:
        return "acm"
    return None
CORE_SECTIONS = {sec for sec, _ in generate.CORE_SECTIONS}
CORE_SUBS = {sub for _, subs in generate.CORE_SECTIONS for sub in subs if sub}
APPENDIX_SECTIONS = set(generate.APPENDIX_SECTIONS)
REQUIRED = ["list", "section", "title", "authors", "year", "venue", "paper_link", "tags", "contribution", "notes"]


def main():
    errors, warnings = [], []
    rows = generate.load_rows()
    titles = [r["title"] for r in rows]
    if len(titles) != len(set(titles)):
        errors.append("duplicate titles in papers.csv")
    if rows and "paper_id" in rows[0]:
        pids = [r["paper_id"] for r in rows]
        if len(pids) != len(set(pids)):
            errors.append("duplicate paper_id in papers.csv")
    for i, r in enumerate(rows, 2):
        for f in REQUIRED:
            if not r.get(f, "").strip():
                errors.append(f"row {i} ({r['title'][:40]}): empty required field '{f}'")
        if r["list"] not in ("core", "appendix"):
            errors.append(f"row {i}: illegal list '{r['list']}'")
        if r["list"] == "core" and r["section"] not in CORE_SECTIONS:
            errors.append(f"row {i}: illegal core section '{r['section']}'")
        if r["list"] == "core" and r["subsection"] and r["subsection"] not in CORE_SUBS:
            errors.append(f"row {i}: illegal subsection '{r['subsection']}'")
        if r["list"] == "appendix" and r["section"] not in APPENDIX_SECTIONS:
            errors.append(f"row {i}: illegal appendix section '{r['section']}'")
        try:
            y = int(r["year"])
            if not (2010 <= y <= 2027):
                errors.append(f"row {i}: year out of range {y}")
        except ValueError:
            errors.append(f"row {i}: year not an integer '{r['year']}'")
        for t in [x.strip() for x in r["tags"].split(";") if x.strip()]:
            if t not in TAG_VOCAB:
                errors.append(f"row {i} ({r['title'][:30]}): tag not in vocabulary: '{t}'")
        if "paper_id" in r:
            if not re.fullmatch(r"[a-z0-9]+", r["paper_id"] or ""):
                errors.append(f"row {i}: malformed paper_id '{r['paper_id']}'")
            if r["fusion_level"] not in ("pixel", "feature", "decision", "na"):
                errors.append(f"row {i}: illegal fusion_level '{r['fusion_level']}'")
            if r.get("scope") not in ("Core", "Related", "Reference"):
                errors.append(f"row {i}: illegal scope '{r.get('scope')}'")
            arch = [x.strip() for x in r["architecture"].split(";") if x.strip()]
            if not arch or any(a not in ("CNN", "YOLO", "Transformer", "DETR", "Mamba", "Other", "na") for a in arch):
                errors.append(f"row {i}: illegal architecture '{r['architecture']}'")
            if "na" in arch and len(arch) > 1:
                errors.append(f"row {i}: architecture 'na' must stand alone")
            for m in [x.strip() for x in r["mechanisms"].split(";") if x.strip()]:
                if m not in ("Attention", "Routing", "Quality-Aware", "Conflict-Aware",
                             "Alignment", "Distillation", "Evidential", "Dynamic Fusion",
                             "Negative Fusion", "Frequency-Domain"):
                    errors.append(f"row {i}: illegal mechanism '{m}'")
        if not r["paper_link"].startswith("http"):
            warnings.append(f"row {i} ({r['title'][:40]}): paper_link is not a URL")
        if r["code_link"] and not r["code_link"].startswith("http"):
            errors.append(f"row {i}: code_link is not a URL")
        if r.get("doi") and not r["doi"].startswith("10."):
            errors.append(f"row {i}: malformed DOI '{r['doi']}'")
        if r.get("doi"):
            if r["doi"].startswith("10.48550"):
                warnings.append(f"row {i} ({r['title'][:40]}): arXiv DOI in doi column — publisher DOIs only")
            dy = doi_year(r["doi"])
            if dy is not None and abs(dy - int(r["year"])) > 1 and r["title"] not in DOI_YEAR_EXCEPTIONS:
                warnings.append(f"row {i} ({r['title'][:40]}): DOI year {dy} vs catalogued year {r['year']} — check issue vs early-access year")
        vf, lf = venue_family(r["venue"]), link_family(r["paper_link"])
        if vf and lf and vf != lf:
            warnings.append(f"row {i} ({r['title'][:40]}): paper_link domain is {lf} but venue '{r['venue']}' is {vf} — link probably wrong")
        if not r["venue"].startswith("arXiv") and \
           not any(c in r["venue"] for c in generate.CONFERENCE_TOKENS) and \
           not any(j in r["venue"] for j in generate.JOURNAL_TOKENS):
            warnings.append(f"row {i} ({r['title'][:40]}): venue '{r['venue']}' is in neither BibTeX token list — defaults to @misc; classify it in tools/generate.py")
    # datasets.csv / protocols.csv (REQ-06 structured sources, 2026-11-04)
    try:
        dsets = generate.load_datasets()
    except FileNotFoundError:
        errors.append("datasets.csv is missing")
        dsets = []
    dnames = [d["dataset"] for d in dsets]
    if len(dnames) != len(set(dnames)):
        errors.append("duplicate dataset names in datasets.csv")
    for j, d in enumerate(dsets, 2):
        for f in ("dataset", "section", "year", "modalities", "images_as_listed", "classes", "source"):
            if not d.get(f, "").strip():
                errors.append(f"datasets.csv row {j} ({d.get('dataset', '?')}): empty field '{f}'")
        if d["section"] not in ("general", "aerial"):
            errors.append(f"datasets.csv row {j}: illegal section '{d['section']}'")
    BIG5 = {"KAIST", "LLVIP", "M<sup>3</sup>FD", "FLIR-aligned", "DroneVehicle"}
    for d in dsets:
        if d["dataset"] in BIG5 and not (d["metrics"].strip() and d["protocol"].strip()):
            errors.append(f"datasets.csv: priority dataset {d['dataset']} lacks metrics/protocol (REQ-06)")
    protos = []
    ppath = os.path.join(ROOT, "protocols.csv")
    if not os.path.exists(ppath):
        errors.append("protocols.csv is missing")
    else:
        with open(ppath, encoding="utf-8") as f:
            protos = list(csv.DictReader(f))
        for j, p in enumerate(protos, 2):
            for f in ("protocol", "source_paper", "datasets", "degradation_types", "severity", "scope", "metrics"):
                if not p.get(f, "").strip():
                    errors.append(f"protocols.csv row {j}: empty field '{f}'")
    print(f"datasets.csv: {len(dsets)} datasets; protocols.csv: {len(protos)} protocols")
    # compare_fields.csv (REQ-04 extraction, 2026-11-05): validate rows present;
    # completeness to 102 rows is enforced at extraction close-out, not here.
    cpath = os.path.join(ROOT, "compare_fields.csv")
    if os.path.exists(cpath):
        with open(cpath, encoding="utf-8") as f:
            crows = list(csv.DictReader(f))
        pidset = {r["paper_id"] for r in rows if "paper_id" in r}
        seen_pid = set()
        for j, c in enumerate(crows, 2):
            if c["paper_id"] not in pidset:
                errors.append(f"compare_fields.csv row {j}: unknown paper_id '{c['paper_id']}'")
            if c["paper_id"] in seen_pid:
                errors.append(f"compare_fields.csv row {j}: duplicate paper_id '{c['paper_id']}'")
            seen_pid.add(c["paper_id"])
            for col in ("quality_estimation", "suppression", "compensation", "robustness_evaluation"):
                if c[col] not in ("Yes", "No", "Unknown"):
                    errors.append(f"compare_fields.csv row {j}: illegal {col} '{c[col]}'")
            for col in ("qe_evidence", "suppression_evidence", "compensation_evidence", "robustness_evidence"):
                if not c[col].strip():
                    errors.append(f"compare_fields.csv row {j}: empty {col} (evidence pointer required)")
            if c["basis"] not in ("full-text", "abstract"):
                errors.append(f"compare_fields.csv row {j}: illegal basis '{c['basis']}'")
        print(f"compare_fields.csv: {len(crows)} rows extracted so far")
    # generated files up to date?
    fresh = generate.build_all()
    for name, text in fresh.items():
        path = os.path.join(ROOT, name)
        current = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if current != text:
            errors.append(f"{name} is out of date with papers.csv — run tools/generate.py")
    # title presence in entry position (anchored, so mentions inside notes don't count)
    for t in titles:
        n = len(re.findall(r"(?m)^\d+\. " + re.escape(t) + r"[,，]", fresh["README.md"]))
        if n != 1:
            errors.append(f"README.md: entry for title found {n}x: {t[:50]}")
        n = len(re.findall(r"(?m)^\| " + re.escape(t) + r" —", fresh["bibliography.md"]))
        if n != 1:
            errors.append(f"bibliography.md: entry for title found {n}x: {t[:50]}")
    n_bib = len(re.findall(r"@\w+\{", fresh["references.bib"]))
    if n_bib != len(rows):
        errors.append(f"references.bib: {n_bib} entries vs {len(rows)} CSV rows")
    n_core = sum(1 for r in rows if r["list"] == "core")
    print(f"papers.csv: {len(rows)} rows (core {n_core}, appendix {len(rows) - n_core})")
    for w in warnings:
        print("WARN:", w)
    for e in errors:
        print("ERROR:", e)
    print("OK — no errors" if not errors else f"FAILED — {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
