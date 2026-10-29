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
    "cross-attention", "decision-level", "degraded-modality", "detr", "distillation",
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
