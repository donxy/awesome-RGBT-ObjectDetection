#!/usr/bin/env python3
"""Generate README.md, bibliography.md and references.bib from papers.csv.

papers.csv is the single source of truth for the paper list. Edit the CSV,
then run:  python3 tools/generate.py
Static README text (intro, scope, news, file list) lives in this script;
dataset summary tables are read from datasets.md.
"""
import csv, re, os, sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORE_SECTIONS = [
    ("Surveys & Benchmarks", [None]),
    ("Pixel-Level Fusion for Detection", [None]),
    ("Feature-Level Fusion", [
        "Attention, Transformers & Foundation Models",
        "Dual-Stream CNN & YOLO-Based Detectors",
        "State-Space Models (Mamba)",
        "Quality- & Conflict-Aware Fusion",
    ]),
    ("Decision-Level & Evidential Fusion", [None]),
]
APPENDIX_SECTIONS = [
    "Robust & Dynamic Fusion (General Multimodal)",
    "Corruption Robustness Benchmarks (Driving / 3D)",
    "Modality Imbalance & Missing-Modality Learning (General)",
    "Test-Time Adaptation, Intervention & Amortized Optimization",
]
GENERATED = "<!-- Generated from papers.csv by tools/generate.py — do not edit by hand. -->"
SRC_NOTE = ("Dataset statistics below are compiled from the datasets' official pages and the public list "
            "[Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) (accessed 2026-10-25); "
            "always confirm numbers on the official page before citing them.")


def load_rows(root=ROOT):
    with open(os.path.join(root, "papers.csv"), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def sort_key(r):
    return (-int(r["year"]), r["title"])


def one_line(r):
    s = f'{r["title"]}, {r["venue"]} {r["year"]}, {r["authors"]}'
    if r["paper_link"].startswith("http"):
        s += f' [[Paper]({r["paper_link"]})]'
    elif r["paper_link"]:
        s += (f' {r["paper_link"]}' if r["paper_link"].startswith("(") else f' ({r["paper_link"]})')
    if r["code_link"]:
        s += f' [[Code]({r["code_link"]})]'
    if r["tags"]:
        s += f' — *{r["tags"]}*'
    return s


def table_after(ds_text, marker):
    idx = ds_text.find(marker)
    if idx < 0:
        return []
    out = []
    for line in ds_text[idx:].splitlines()[1:]:
        if line.startswith("|"):
            out.append(line)
        elif out:
            break
    return out


def group_core(rows):
    groups = OrderedDict()
    for sec, subs in CORE_SECTIONS:
        for sub in subs:
            sel = [r for r in rows if r["list"] == "core" and r["section"] == sec
                   and (r["subsection"] or None) == sub]
            if sel:
                groups[(sec, sub)] = sorted(sel, key=sort_key)
    return groups


def group_appendix(rows):
    groups = OrderedDict()
    for sec in APPENDIX_SECTIONS:
        sel = [r for r in rows if r["list"] == "appendix" and r["section"] == sec]
        if sel:
            groups[sec] = sorted(sel, key=sort_key)
    return groups


def build_readme(rows, root=ROOT):
    ds = open(os.path.join(root, "datasets.md"), encoding="utf-8").read()
    ped = table_after(ds, "## General & Pedestrian Detection")
    aer = table_after(ds, "## Aerial / UAV Object Detection")
    n_core = sum(1 for r in rows if r["list"] == "core")
    n_app = sum(1 for r in rows if r["list"] == "appendix")
    L = [GENERATED, "# owesome-RGBT-ObjectDetection", "",
         "A curated collection of **RGBT object detection** resources — papers, datasets, and code.", "",
         "RGBT (also written RGB-T, RGB-Thermal, multispectral, or visible–infrared) object detection fuses a visible-light image with a thermal (LWIR) image to detect objects under conditions where either modality alone fails — darkness, glare, smoke, or adverse weather.", "",
         "**Scope.** Object detection only: general, pedestrian, vehicle, and aerial/UAV detection with paired visible–thermal imagery. Segmentation, salient object detection, crowd counting, and tracking are out of scope (see Related Lists).", "",
         "**How this list is organised — one axis only.** Papers in the main list are RGBT detection papers, classified by *technical route*: the level at which the two modalities are fused (pixel → feature → decision), with architecture families as subsections of feature-level fusion. Challenges such as misalignment, degradation, or missing modalities are **tags** (shown in italics, and a column in papers.csv), not sections — so every paper has exactly one home. Work that is not RGBT detection but transfers to it (general multimodal fusion, imbalance/missing-modality learning, test-time methods, driving robustness) lives in a separate Appendix, clearly marked, instead of being mixed into the main list.", "",
         "**Single source of truth.** The paper list lives in [papers.csv](papers.csv); README.md, bibliography.md and references.bib are generated from it by [tools/generate.py](tools/generate.py) and checked by tools/validate.py. Edit the CSV, never the generated files.", "",
         "## News", "",
         "- [2026-10-26] Tooling: papers.csv is now the single source of truth — README, bibliography and BibTeX are generated and validated automatically. Tag vocabulary consolidated.",
         "- [2026-10-25] Reclassified by technical route (fusion level + architecture family), with challenge tags and a separate appendix for non-RGBT related work. 42 papers: 21 core RGBT detection, 21 appendix.",
         "- [2026-10-25] Initial general, detection-only structure: datasets first, themed paper list, structured data files (CSV / BibTeX), detailed bibliography, learning roadmap.", "",
         "## Contents", "",
         "1. [Datasets](#datasets)",
         "2. [Surveys & Benchmarks](#surveys--benchmarks)",
         "3. [Pixel-Level Fusion for Detection](#pixel-level-fusion-for-detection)",
         "4. [Feature-Level Fusion](#feature-level-fusion)",
         "5. [Decision-Level & Evidential Fusion](#decision-level--evidential-fusion)",
         "6. [Appendix — Related Work Beyond RGBT Detection](#appendix--related-work-beyond-rgbt-detection)",
         "7. [Repository Files](#repository-files)",
         "8. [Adding an Entry](#adding-an-entry)",
         "9. [Related Lists](#related-lists)", "",
         "## Datasets", "",
         "Full tables with tools and robustness benchmarks are in [datasets.md](datasets.md). Summary of the main benchmarks:", ""]
    L += ped + [""] + aer + ["", "> " + SRC_NOTE, ""]
    last_sec = None
    for (sec, sub), items in group_core(rows).items():
        if sec != last_sec:
            L += [f"## {sec}", ""]; last_sec = sec
        if sub:
            L += [f"### {sub}", ""]
        for i, r in enumerate(items, 1):
            L.append(f"{i}. {one_line(r)}")
        L.append("")
    L += ["## Appendix — Related Work Beyond RGBT Detection", "",
          "Not RGBT detection papers. They are collected because their methods or protocols transfer directly (quality-aware fusion, imbalance and missing-modality learning, corruption benchmarks, test-time intervention). They are deliberately kept out of the main list above.", ""]
    for sec, items in group_appendix(rows).items():
        L += [f"### {sec}", ""]
        for i, r in enumerate(items, 1):
            L.append(f"{i}. {one_line(r)}")
        L.append("")
    L += ["## Repository Files", "",
          "- [papers.csv](papers.csv) — **the single source of truth**: section, subsection, tags, links, DOI, contribution, notes",
          "- [datasets.md](datasets.md) — dataset tables, KAIST tools, and robustness benchmarks (hand-maintained)",
          "- [bibliography.md](bibliography.md) — generated detailed table (contribution and notes), same classification as this README",
          "- [references.bib](references.bib) — generated BibTeX for all entries",
          "- [learning-roadmap.md](learning-roadmap.md) — a staged reading path through this list (stages 0–6); a reading order, separate from the classification above",
          "- [tools/generate.py](tools/generate.py) / tools/validate.py — regenerate and validate the list from papers.csv", "",
          "## Adding an Entry", "",
          "Add one row to papers.csv (that is the only edit), then run `python3 tools/generate.py && python3 tools/validate.py`. Decide the section by fusion level first (pixel / feature / decision), then the architecture family; put challenges in tags (controlled vocabulary enforced by the validator), never in a new section. Non-RGBT work goes to the Appendix. Only add entries whose paper link you have verified.", "",
          "## Related Lists", "",
          "- [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) — the broader RGB-T fusion collection (pedestrian/aerial detection, segmentation, salient detection, crowd counting, tracking)",
          "- [Awesome-RGBT](https://github.com/VisionVerse/Awesome-RGBT) — RGB-T fusion across tasks",
          "- [MOD-ZOO](https://github.com/DocF/MOD-ZOO) — curated resources accompanying a multispectral object detection survey", ""]
    return "\n".join(L)


def build_bibliography(rows):
    L = [GENERATED, "# Detailed Bibliography — RGBT Object Detection", "",
         "Detailed companion to the [README](README.md): every entry with a one-sentence contribution and notes, in the README's technical-route classification (core list first, appendix second). Generated from papers.csv.", ""]
    def section(title, items):
        L.append(f"## {title}"); L.append("")
        L.append("| Paper | Link | Tags | Contribution | Notes |")
        L.append("|---|---|---|---|---|")
        for r in items:
            link = f'[Paper]({r["paper_link"]})' if r["paper_link"].startswith("http") else r["paper_link"]
            if r["code_link"]:
                link += f' · [Code]({r["code_link"]})'
            c = lambda s: s.replace("|", "/")
            L.append(f'| {c(r["title"])} — {c(r["authors"])}, {r["year"]}, {c(r["venue"])} | {link} | {c(r["tags"])} | {c(r["contribution"])} | {c(r["notes"])} |')
        L.append("")
    for (sec, sub), items in group_core(rows).items():
        section(f"{sec} — {sub}" if sub else sec, items)
    L += ["## Appendix — Related Work Beyond RGBT Detection", ""]
    for sec, items in group_appendix(rows).items():
        section(f"Appendix: {sec}", items)
    L += ["## Verification Notes", "",
          "- Links were verified against arXiv, publisher, or proceedings pages on 2026-10-25. Two entries (CMPD, GM-DETR) are recorded with volume/page references where no stable paper URL was verified.",
          "- \"TARDet\" does not exist under that name in the verified literature; the work is TarDAL (CVPR 2022), included in the main list.",
          "- CMDistill (IEEE JSTARS 2024) could not be independently verified and is excluded.",
          "- Some performance figures in the notes come from comparative tables in other papers (secondary sources); check the original paper before citing a number.", ""]
    return "\n".join(L)


def bib_key(r, seen):
    first = re.split(r"[,\s&]+", r["authors"])[0].lower() if r["authors"] else "ref"
    first = re.sub(r"[^a-z]", "", first) or "ref"
    word = re.sub(r"[^A-Za-z0-9]", "", r["title"].split(":")[0].split()[0]).lower()
    k = f"{first}{r['year']}{word}"
    if k in seen:
        seen[k] += 1; k += str(seen[k])
    else:
        seen[k] = 1
    return k


def build_bib(rows):
    ordered = [r for _, items in group_core(rows).items() for r in items] + \
              [r for _, items in group_appendix(rows).items() for r in items]
    seen, entries = {}, []
    for r in ordered:
        venue = r["venue"]
        typ = "article" if any(j in venue for j in ["IEEE", "Pattern Recognition", "TMLR"]) else \
              ("inproceedings" if any(c in venue for c in ["CVPR", "ECCV", "ICML", "ICLR", "NeurIPS", "AAAI", "ACM MM", "ICCV", "ICPR", "WACV", "ICIP"]) else "misc")
        esc = lambda s: s.replace("{", "").replace("}", "")
        def ba(a):
            a = a.strip()
            if a.endswith("et al."):
                return a[:-6].strip() + " and others"
            parts = [x.strip() for x in a.replace("&", ",").split(",") if x.strip()]
            return " and ".join(parts) if parts else a
        fields = [f"  author = {{{esc(ba(r['authors']))}}}", f"  title = {{{esc(r['title'])}}}", f"  year = {{{r['year']}}}"]
        if venue:
            fields.append(f"  journal = {{{esc(venue)}}}" if typ == "article" else
                          (f"  booktitle = {{{esc(venue)}}}" if typ == "inproceedings" else f"  note = {{{esc(venue)}}}"))
        if r.get("doi"):
            fields.append(f"  doi = {{{esc(r['doi'])}}}")
        if r["paper_link"].startswith("http"):
            fields.append(f"  url = {{{r['paper_link']}}}")
        elif r["paper_link"]:
            fields.append(f"  note = {{{esc(r['paper_link'])}}}")
        entries.append(f"@{typ}{{{bib_key(r, seen)},\n" + ",\n".join(fields) + "\n}")
    return ("% Generated from papers.csv by tools/generate.py — do not edit by hand.\n"
            "% Check the original paper before formal citation (author lists and DOIs are being completed).\n\n"
            + "\n\n".join(entries) + "\n")


def build_all(root=ROOT):
    rows = load_rows(root)
    return {"README.md": build_readme(rows, root),
            "bibliography.md": build_bibliography(rows),
            "references.bib": build_bib(rows)}


if __name__ == "__main__":
    out = build_all()
    for name, text in out.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote", name, len(text.encode()), "bytes")
