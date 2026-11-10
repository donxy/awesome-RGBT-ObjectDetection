# Classification Rules

This list is organised on **one axis only**. Every paper has exactly one home,
and the home is decided by the rules below — never by topic, difficulty, or
which challenge a paper studies. Challenges and mechanisms are **tags**
(controlled vocabulary in `papers.csv`, enforced by `tools/validate.py`),
not sections. These rules were written down on 2026-11-04 after an audit
found that expansion had let mechanism themes creep back into the section
tree; the repair of that date applied the rules below to the whole list.

## Main list (core): RGBT detection papers

**Step 1 — document type before method axis.** Surveys and benchmark papers
have no fusion stage of their own, so they form one section,
**Surveys & Benchmarks**, ahead of the method sections. A paper whose primary
contribution is a method goes to the method sections even if it also releases
a dataset (e.g. TarDAL with M3FD); a paper whose primary contribution is a
benchmark or an empirical study goes to Surveys & Benchmarks even if it ships
baseline code (e.g. WiSE-OD, MSOD-Bench).

**Step 2 — fusion stage.** A method paper is classified by the level at which
the two modalities' information is combined for the detection output:

- **Pixel-Level Fusion for Detection** — a fused image (or fused input
  representation) is produced first and then detected on: image-fusion
  networks with detection downstream, input-level fusion, early fusion.
- **Feature-Level Fusion** — modality features are combined inside the
  detector (before or within the detection head). This includes methods with
  an evidential or confidence layer on top of feature fusion (e.g. CMPD,
  EHF): the evidence layer does not make them decision-level, because the
  modalities are already mixed at feature level.
- **Decision-Level Fusion** — each modality is detected independently and
  the *predictions* are combined (ensembling, late fusion of outputs).
  A section is allowed to be small: after the 2026-11-04 repair this section
  holds only true decision-level work.

**Step 3 — architecture family (subsections of Feature-Level Fusion only).**
Subsections are by the architecture family of the fusion network, nothing
else:

- **Attention, Transformers & Foundation Models** — transformer / DETR-family
  detectors, cross-attention fusion architectures, and foundation-model-based
  detectors.
- **Dual-Stream CNN & YOLO-Based Detectors** — dual-stream convolutional
  detectors, including YOLO-family single-stage detectors and two-stage
  CNN detectors (Faster R-CNN family), whatever auxiliary attention, gating,
  or quality-estimation modules they carry.
- **State-Space Models (Mamba)** — SSM/Mamba-based fusion networks.

Pixel-Level and Decision-Level have no subsections (granularity convention:
subsections exist only where a section is large).

**Tie-breaks.** (a) A mechanism never outranks architecture: a
reliability-aware YOLO stays with the YOLO/CNN family, and a
reliability-aware DETR stays with the Transformers — the mechanism is
expressed by tags (`quality-aware`, `conflict-aware`, `expert-routing`, …).
(b) A training-only framework is classified by the architecture it trains
and the fusion it keeps at inference. (c) If a paper genuinely fuses at two
stages, classify by the stage its headline contribution operates on.

## Appendix: related work beyond RGBT detection

The appendix is grouped by **contribution type** — one standard, applied to
every group:

- **Surveys (General Multimodal)** — survey papers.
- **Benchmarks & Evaluation Studies** — benchmark datasets, corruption /
  robustness benchmarks, and evaluation or attack studies whose object is
  an existing detector rather than a new fusion method.
- **Robust & Dynamic Fusion (General Multimodal)** — general multimodal
  fusion methods whose mechanisms transfer to RGBT.
- **Modality Imbalance & Missing-Modality Learning (General)** — general
  methods for learning under modality imbalance or missing modalities.
- **Test-Time Adaptation, Intervention & Amortized Optimization** —
  test-time paradigms and their inference-time / optimisation background.

Scope rulings are unchanged: a work is core only if it is RGBT (visible +
thermal/LWIR) object detection; multispectral work without a thermal
channel (e.g. the visible–NIR benchmark MODA) and non-detection work stay in
the appendix even when closely related.

## Facet fields (REQ-01, added 2026-11-04)

Alongside the tree above, `papers.csv` carries three faceted fields used by
the website's combined filtering. They are derived from the tree and the
tags — the tree remains the classification of record:

- `fusion_level` — pixel / feature / decision / na. Core methods take it
  from their section; appendix methods are judged by the level at which
  they combine modalities; surveys, benchmarks and test-time paradigms
  are `na`.
- `architecture` — multi-value from {CNN, YOLO, Transformer, DETR, Mamba,
  Other}, or `na`. Taken from the architecture subsection, refined where
  the deep-read record verifies a YOLO or DETR family member.
- `mechanisms` — multi-value, derived only from the mechanism tags
  (Attention, Routing, Quality-Aware, Conflict-Aware, Alignment,
  Distillation, Evidential, Dynamic Fusion, Negative Fusion,
  Frequency-Domain). Empty means no named mechanism facet.

`paper_id` is a stable identifier (first-author surname + year + first
title word, the references.bib key base) assigned once and never reused
or reassigned, independent of row order.

Facet rulings (2026-11-06, from the REQ-04 extraction cross-check):

- **QMF** (zhang2023provable) and **ReconBoost** (hua2024reconboost):
  `fusion_level` corrected from `feature` to `decision`. Both are
  appendix papers, so under the rule above their facet is judged by the
  level at which they combine modalities: QMF weights the modalities'
  final prediction scores by an energy-based uncertainty, and ReconBoost
  sums the modalities' output scores unweighted at inference — both are
  decision-level late fusion.
- **MDQF** (tian2026modalitydecoupled) stays in Feature-Level Fusion
  with `fusion_level = feature`, by ruling. Its two detectors are fully
  independent and their features never meet; the only coupling is an
  exchange of query/proposal sets between decoder stages. That coupling
  sits *inside* the decoding pipeline, at the level of intermediate
  representations, and each branch's later decoding is conditioned on
  the other branch's hypotheses — it is not a post-hoc combination of
  final outputs of the ProbEn kind, which is what Decision-Level
  collects. The compare table records its fusion strategy verbatim as
  decision-style query coupling, so the distinction stays visible in
  the data.

## Scope tiers (REQ-02, approved 2026-11-04)

Independent of the list placement above, every paper carries a `scope`
in papers.csv — **the two axes must not be conflated** (a paper can be
Related in scope while staying in the appendix, and vice versa):

- **Core** — object detection that actually uses both RGB and thermal at
  inference, plus the field's own surveys and benchmarks.
- **Related** — directly adjacent work: thermal-only deployment,
  image-fusion networks whose output is a fused image (detection
  downstream), cross-modal distillation for single-modality detection,
  general IVIF surveys, multispectral benchmarks, and transferable
  robustness-evaluation protocols.
- **Reference** — general multimodal / robust-learning / optimization
  method references with no direct RGBT-detection task link.

Decision order: (1) surveys & benchmarks by subject; (2) methods by
inference modality (training-time use of a second modality does not
count); (3) dual-modality methods by deliverable (detector vs fused
image); (4) multi-variant work judged by its deployed versions — a
variant that trains and infers on both modalities keeps the paper Core;
(5) general methods by protocol/task transferability. Current
distribution: Core 66 / Related 13 / Reference 23.

## Tags

Tags are faceted metadata — challenges (`degraded-modality`,
`missing-modality`, `modality-imbalance`, `alignment`), mechanisms
(`quality-aware`, `conflict-aware`, `evidential`, `expert-routing`,
`dynamic-fusion`, `negative-fusion`), domains (`pedestrian`, `aerial`), and
properties (`efficiency`, `thermal-only-inference`). Two constraints keep
tags consistent with the tree: a tag must never contradict the paper's
section (fusion-stage values such as "decision-level" are carried by
sections and are **not** tags), and a mechanism tag should be applied to
every paper whose headline mechanism it names, not only to some.
