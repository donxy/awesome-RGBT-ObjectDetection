#!/usr/bin/env python3
"""Generate README.md, bibliography.md, references.bib and the website
exports (papers.json, deep.json, datasets.json) from papers.csv.

papers.csv is the single source of truth for the paper list. Edit the CSV,
then run:  python3 tools/generate.py
Static README text (intro, scope, news, file list) lives in this script;
dataset summary tables are read from datasets.md. Site-only note texts
(card takeaway / comment, deep-read sections, figure captions) live in
site_content.json, keyed by paper title, and are merged in at export time;
figure images themselves are website assets (rgbt-notes/figs/<slug>.webp),
only their file names are exported here.
"""
import csv, re, os, sys, json, unicodedata
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

DEEP_SECTIONS = ["问题定义", "方法细节", "实验设置", "关键数字", "消融说明了什么", "局限"]

# Tag presentation metadata for the website filter panel: Chinese label and
# panel group for every tag in the controlled vocabulary (validate.py checks
# this table covers the vocabulary exactly).
TAG_META = {
    # 挑战 — the problem a paper addresses
    "alignment":            {"zh": "对齐", "group": "挑战"},
    "conflict-aware":       {"zh": "冲突感知", "group": "挑战"},
    "corruption":           {"zh": "腐蚀", "group": "挑战"},
    "degraded-modality":    {"zh": "模态退化", "group": "挑战"},
    "efficiency":           {"zh": "效率", "group": "挑战"},
    "missing-modality":     {"zh": "模态缺失", "group": "挑战"},
    "modality-imbalance":   {"zh": "模态不平衡", "group": "挑战"},
    "negative-fusion":      {"zh": "负融合", "group": "挑战"},
    "quality-aware":        {"zh": "质量感知", "group": "挑战"},
    "test-time-adaptation": {"zh": "测试时适配", "group": "挑战"},
    "test-time-intervention": {"zh": "测试时干预", "group": "挑战"},
    # 架构 — architecture / mechanism family
    "adapter":          {"zh": "适配器", "group": "架构"},
    "cross-attention":  {"zh": "跨模态注意力", "group": "架构"},
    "decision-level":   {"zh": "决策级", "group": "架构"},
    "detr":             {"zh": "DETR", "group": "架构"},
    "distillation":     {"zh": "蒸馏", "group": "架构"},
    "dual-stream":      {"zh": "双流", "group": "架构"},
    "dynamic-fusion":   {"zh": "动态融合", "group": "架构"},
    "ensemble":         {"zh": "集成", "group": "架构"},
    "evidential":       {"zh": "证据理论", "group": "架构"},
    "expert-routing":   {"zh": "专家路由", "group": "架构"},
    "foundation-model": {"zh": "基础模型", "group": "架构"},
    "frequency-domain": {"zh": "频域", "group": "架构"},
    "image-fusion":     {"zh": "图像融合", "group": "架构"},
    "mamba":            {"zh": "Mamba", "group": "架构"},
    "task-coupled":     {"zh": "任务耦合", "group": "架构"},
    "transformer":      {"zh": "Transformer", "group": "架构"},
    "yolo":             {"zh": "YOLO", "group": "架构"},
    # 场景与类型 — application scene / entry type
    "aerial":       {"zh": "航拍", "group": "场景与类型"},
    "benchmark":    {"zh": "基准", "group": "场景与类型"},
    "lidar-camera": {"zh": "激光–相机", "group": "场景与类型"},
    "pedestrian":   {"zh": "行人", "group": "场景与类型"},
    "survey":       {"zh": "综述", "group": "场景与类型"},
    "thermal-only-inference": {"zh": "仅热红外推理", "group": "场景与类型"},
}


def slugify(title):
    """Stable URL/anchor slug from a paper title (e.g. 'WiSE-OD' -> 'wise-od')."""
    t = unicodedata.normalize("NFKD", title)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t or "paper"


def eff_slug(title, content):
    """A paper's website slug: an explicit 'slug' in site_content.json wins,
    so permalinks and figure file names stay stable across title edits."""
    return content.get(title, {}).get("slug") or slugify(title)


def load_content(root=ROOT):
    path = os.path.join(root, "site_content.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_datasets(root=ROOT):
    """Structured dataset rows from the datasets.md tables (website export)."""
    ds = open(os.path.join(root, "datasets.md"), encoding="utf-8").read()

    def rows_after(marker, keys):
        out = []
        for line in table_after(ds, marker)[2:]:  # skip header + separator
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            m = re.match(r"\[(.*?)\]\((.*?)\)", cells[0])
            name = re.sub(r"<[^>]+>", "", m.group(1)) if m else cells[0]
            row = {"name": name, "url": m.group(2) if m else ""}
            for k, v in zip(keys, cells[1:]):
                row[k] = v
            out.append(row)
        return out

    return {
        "general": rows_after("## General & Pedestrian Detection",
                              ["year", "modality", "images", "classes"]),
        "aerial": rows_after("## Aerial / UAV Object Detection",
                             ["year", "modality", "images", "classes", "alignment"]),
    }


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
    L = [GENERATED, "# awesome-RGBT-ObjectDetection", "",
         "A curated collection of **RGBT object detection** resources — papers, datasets, and code.", "",
         "RGBT (also written RGB-T, RGB-Thermal, multispectral, or visible–infrared) object detection fuses a visible-light image with a thermal (LWIR) image to detect objects under conditions where either modality alone fails — darkness, glare, smoke, or adverse weather.", "",
         "**Scope.** Object detection only: general, pedestrian, vehicle, and aerial/UAV detection with paired visible–thermal imagery. Segmentation, salient object detection, crowd counting, and tracking are out of scope (see Related Lists).", "",
         "**How this list is organised — one axis only.** Papers in the main list are RGBT detection papers, classified by *technical route*: the level at which the two modalities are fused (pixel → feature → decision), with architecture families as subsections of feature-level fusion. Challenges such as misalignment, degradation, or missing modalities are **tags** (shown in italics, and a column in papers.csv), not sections — so every paper has exactly one home. Work that is not RGBT detection but transfers to it (general multimodal fusion, imbalance/missing-modality learning, test-time methods, driving robustness) lives in a separate Appendix, clearly marked, instead of being mixed into the main list.", "",
         "**Single source of truth.** The paper list lives in [papers.csv](papers.csv); README.md, bibliography.md and references.bib are generated from it by [tools/generate.py](tools/generate.py) and checked by tools/validate.py. Edit the CSV, never the generated files. The notes website ([donxy.github.io/rgbt-notes](https://donxy.github.io/rgbt-notes/)) reads the generated papers.json / deep.json / datasets.json exports (papers.csv merged with the site-only texts in site_content.json), so the site and this repository share one dataset.", "",
         "## News", "",
         "- [2026-10-29] Website data pipeline: the notes site now consumes this repo's generated JSON exports (papers / deep reads / datasets); figure images split into per-paper files on the site.",
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
          "- [site_content.json](site_content.json) — site-only note texts for the website (card takeaway/comment, deep-read sections, figure captions), keyed by paper title; merged with papers.csv at export time",
          "- [papers.json](papers.json) / [deep.json](deep.json) / [datasets.json](datasets.json) — generated exports consumed by the notes website; do not edit by hand",
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


def ordered_rows(rows, content):
    """Papers in website/README display order: canonical section groups,
    then the site_content.json 'ord' within each group (CSV order as fallback)."""
    csv_idx = {r["title"]: i for i, r in enumerate(rows)}

    def key(r):
        return (content.get(r["title"], {}).get("ord", 100000 + csv_idx[r["title"]]),
                csv_idx[r["title"]])

    out = []
    for _, items in group_core(rows).items():
        out += sorted(items, key=key)
    for _, items in group_appendix(rows).items():
        out += sorted(items, key=key)
    return out


def build_papers_json(rows, content):
    papers = []
    for r in ordered_rows(rows, content):
        c = content.get(r["title"], {})
        slug = eff_slug(r["title"], content)
        papers.append({
            "id": slug,
            "list": r["list"],
            "sec": r["section"],
            "sub": r["subsection"] or "",
            "title": r["title"],
            "authors": r["authors"],
            "year": int(r["year"]),
            "venue": r["venue"],
            "paper": r["paper_link"],
            "code": r["code_link"],
            "doi": r.get("doi", ""),
            "tags": [t.strip() for t in r["tags"].split(";") if t.strip()],
            "basis": "full" if r["notes_basis"] == "full-text" else "",
            "deep": bool(c.get("deep")),
            "take": c.get("take", ""),
            "note": c.get("note", ""),
            "paperNote": c.get("paperNote", ""),
            "fig": f"figs/{slug}.webp" if c.get("figCap") else "",
            "figAlt": c.get("figAlt", ""),
            "figCap": c.get("figCap", ""),
            "figSrc": c.get("figSrc", ""),
        })
    return json.dumps({"tagMeta": TAG_META, "papers": papers},
                      ensure_ascii=False, separators=(",", ":")) + "\n"


def build_deep_json(rows, content):
    deep = {}
    for r in ordered_rows(rows, content):
        c = content.get(r["title"], {})
        if c.get("deep"):
            deep[eff_slug(r["title"], content)] = c["deep"]
    return json.dumps(deep, ensure_ascii=False, separators=(",", ":")) + "\n"


def build_datasets_json(root=ROOT):
    return json.dumps(parse_datasets(root), ensure_ascii=False, separators=(",", ":")) + "\n"


def build_all(root=ROOT):
    rows = load_rows(root)
    content = load_content(root)
    return {"README.md": build_readme(rows, root),
            "bibliography.md": build_bibliography(rows),
            "references.bib": build_bib(rows),
            "papers.json": build_papers_json(rows, content),
            "deep.json": build_deep_json(rows, content),
            "datasets.json": build_datasets_json(root)}


if __name__ == "__main__":
    out = build_all()
    for name, text in out.items():
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote", name, len(text.encode()), "bytes")
