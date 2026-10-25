# owesome-RGBT-ObjectDetection

A curated collection of **RGBT object detection** resources — papers, datasets, and code.

RGBT (also written RGB-T, RGB-Thermal, multispectral, or visible–infrared) object detection fuses a visible-light image with a thermal (LWIR) image to detect objects under conditions where either modality alone fails — darkness, glare, smoke, or adverse weather.

**Scope.** Object detection only: general, pedestrian, vehicle, and aerial/UAV detection with paired visible–thermal imagery. Segmentation, salient object detection, crowd counting, and tracking are out of scope (see Related Lists).

**How this list is organised — one axis only.** Papers in the main list are RGBT detection papers, classified by *technical route*: the level at which the two modalities are fused (pixel → feature → decision), with architecture families as subsections of feature-level fusion. Challenges such as misalignment, degradation, or missing modalities are **tags** (shown in italics, and a column in papers.csv), not sections — so every paper has exactly one home. Work that is not RGBT detection but transfers to it (general multimodal fusion, imbalance/missing-modality learning, test-time methods, driving robustness) lives in a separate Appendix, clearly marked, instead of being mixed into the main list.

## News

- [2026-10-25] Reclassified by technical route (fusion level + architecture family), with challenge tags and a separate appendix for non-RGBT related work. 42 papers: 21 core RGBT detection, 21 appendix.
- [2026-10-25] Initial general, detection-only structure: datasets first, themed paper list, structured data files (CSV / BibTeX), detailed bibliography, learning roadmap.

## Contents

1. [Datasets](#datasets)
2. [Surveys & Benchmarks](#surveys--benchmarks)
3. [Pixel-Level Fusion for Detection](#pixel-level-fusion-for-detection)
4. [Feature-Level Fusion](#feature-level-fusion)
5. [Decision-Level & Evidential Fusion](#decision-level--evidential-fusion)
6. [Appendix — Related Work Beyond RGBT Detection](#appendix--related-work-beyond-rgbt-detection)
7. [Repository Files](#repository-files)
8. [Adding an Entry](#adding-an-entry)
9. [Related Lists](#related-lists)

## Datasets

Full tables with tools and robustness benchmarks are in [datasets.md](datasets.md). Summary of the main benchmarks:

|Dataset                        | Years |Modality     |Images| Classes|
|-------------------------------|-------|-------------|------|--------|
|[KAIST](https://soonminhwang.github.io/rgbt-ped-detection/)|2015|RGB, LWIR|95K|1|
|[CVC-14](http://adas.cvc.uab.es/elektra/enigma-portfolio/cvc-14-visible-fir-day-night-pedestrian-sequence-dataset/)|2016|RGB, LWIR|8K|1|
|[FLIR](https://www.flir.cn/oem/adas/adas-dataset-form/)|2018|RGB, LWIR|20K|5|
|[FLIR-aligned](https://github.com/zonaqiu/FLIR-align)|2020|RGB, LWIR|5K|3|
|[Utokyo](https://www.mi.t.u-tokyo.ac.jp/static/projects/mil_multispectral/)|2017|RGB, NIR, MIR, FIR|7K|5|
|[LLVIP](https://bupt-ai-cz.github.io/LLVIP/)|2021| RGB, LWIR|15K|1|
|[M<sup>3</sup>FD](https://github.com/dlut-dimt/TarDAL)|2022|RGB, LWIR|4K|6|
|[Multi-Spectral Stereo](https://github.com/UkcheolShin/MS2-MultiSpectralStereoDataset)|2023|RGB, NIR, LWIR|195K|4|
|[SMOD](https://www.kaggle.com/datasets/zizhaochen6/sjtu-multispectral-object-detection-smod-dataset)|2024|RGB, LWIR|8K|4|
|[MMPD](https://github.com/jin-s13/MMPD-Dataset)|2024|RGB, LWIR|260K|1|
|[InfraParis](https://ensta-u2is-ai.github.io/infraParis/)|2024| RGB, LWIR, Depth|7K|19|
|[MFAD](https://github.com/hukefy/EI2Det)|2025|RGB, LWIR|12K|6|
|[MMVIP](https://github.com/yyppptjr/MMVIP)|2026|RGB, LWIR|128K|2|
|[RGBT-Ground](https://github.com/crazyxiaoxi/RGBTVG)|2026|RGB, LWIR|40K|5|

|Dataset                        | Years |Modality     |Images| Classes|Alignment|
|-------------------------------|-------|-------------|------|--------|---------|
|[DroneVehicle](https://github.com/VisDrone/DroneVehicle)|2021|RGB, LWIR|56K|5|Partially|
|[VEDAI](https://downloads.greyc.fr/vedai/)|2014|RGB, NIR|1K|9|Strictly|
|[NII-CU](https://www.nii-cu-multispectral.org/)|2022|RGB, LWIR|5K|1|Strictly|
|[DVTOD](https://github.com/VDT-2048/DVTOD)|2024|RGB, LWIR|2K|3|Misaligned|
|[VTSaR](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10833840)|2024|RGB, LWIR|40K|1|Strictly|
|[RGBT-Tiny](https://github.com/XinyiYing/RGBT-Tiny)|2025|RGB, LWIR|93K|7|Partially|
|[ATR-UMOD](https://github.com/supercpy/ATR-UMOD)|2025|RGB, LWIR|13K|11|Partially|
|[MODA](https://github.com/shuaihao-han/MODA)|2026|RGB, NIR|13K|8|Strictly|
|[Tri-Modal Dataset](https://github.com/radlab-sketch/trimodal-uav-det.git)|2026|RGB, LWIR, Event|10K|1|Partially|

> Dataset statistics below are compiled from the datasets' official pages and the public list [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) (accessed 2026-10-25); always confirm numbers on the official page before citing them.

## Surveys & Benchmarks

1. WiSE-OD, WACV 2026, Medeiros et al. [[Paper](https://arxiv.org/abs/2507.18925)] — *degraded-modality; benchmark; out-of-distribution*
2. Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption, IEEE TPAMI 2025, Liu et al. [[Paper](https://arxiv.org/abs/2501.10761)] — *survey*
3. MSOD-Bench: Optimizing Multispectral Object Detection, arXiv 2024, Zhou et al. [[Paper](https://arxiv.org/abs/2411.18288)] — *benchmark*

## Pixel-Level Fusion for Detection

1. CDDFuse, CVPR 2023, Zhao et al. [[Paper](https://arxiv.org/abs/2211.14461)] — *image-fusion; task-coupled*
2. MetaFusion, CVPR 2023, Zhao et al. [[Paper](https://doi.org/10.1109/CVPR52729.2023.01341)] — *image-fusion; task-coupled*
3. TarDAL: Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection, CVPR 2022, Liu et al. [[Paper](https://arxiv.org/abs/2203.16220)] [[Code](https://github.com/JinyuanLiu-CV/TarDAL)] — *image-fusion; task-coupled*

## Feature-Level Fusion

### Attention, Transformers & Foundation Models

1. UniRGB-IR, ACM MM 2025, Yuan et al. [[Paper](https://arxiv.org/abs/2404.17360)] — *foundation-model; adapter*
2. C2Former: Calibrated and Complementary Transformer, IEEE TGRS 2024, Yuan & Wei [[Paper](https://arxiv.org/abs/2306.16175)] [[Code](https://github.com/yuanmaoxun/C2Former)] — *alignment; cross-attention; transformer*
3. DAMSDet, ECCV 2024, Guo, Gao, Liu, Meng, Gao [[Paper](https://eccv.ecva.net/virtual/2024/poster/801)] [[Code](https://github.com/gjj45/DAMSDet)] — *transformer; detr*
4. GM-DETR, CVPR Workshops 2024, Xiao et al. (CVPRW 2024, pp.5541–5549) — *transformer; detr; efficiency*
5. ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection, Pattern Recognition 2024, Shen et al. [[Paper](https://ieeexplore.ieee.org/abstract/document/10225383)] [[Code](https://github.com/chanchanchan97/ICAFusion)] — *cross-attention*
6. Cross-Modality Fusion Transformer (CFT), arXiv 2021, Fang, Han, Wang [[Paper](https://arxiv.org/abs/2111.00273)] — *cross-attention; transformer*

### Dual-Stream CNN & YOLO-Based Detectors

1. YOLOv11-RGBT, arXiv 2025, Wan et al. [[Paper](https://arxiv.org/abs/2506.14696)] [[Code](https://github.com/wandahangFY/YOLOv11-RGBT)] — *yolo; efficiency*
2. DEYOLO, ICPR 2024, Chen et al. [[Paper](https://arxiv.org/abs/2412.04931)] — *yolo; dual-stream*
3. LRAF-Net, IEEE TNNLS 2023, Fu et al. [[Paper](https://doi.org/10.1109/TNNLS.2023.3266452)] — *dual-stream; modality-bias; mask-augmentation*

### State-Space Models (Mamba)

1. Fusion-Mamba, IEEE TMM 2025, Dong et al. [[Paper](https://doi.org/10.1109/TMM.2025.3599020)] — *mamba; state-space*
2. WaveMamba, ICCV 2025, Zhu et al. [[Paper](https://arxiv.org/abs/2507.18173)] [[Code](https://github.com/EhanDong/WaveMamba)] — *mamba; state-space; frequency-domain*

### Quality- & Conflict-Aware Fusion

1. Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance, Pattern Recognition Letters 2025, Tian, Yang, Zhu, Wang, He [[Paper](https://arxiv.org/abs/2505.22154)] — *degraded-modality; quality-aware; modality-imbalance*
2. CALNet (Cross-Modal Conflict-Aware Learning), ACM MM 2023, He, Tang, Zou, Zhang [[Paper](https://doi.org/10.1145/3581783.3612651)] — *conflict-aware; aerial*

## Decision-Level & Evidential Fusion

1. Confidence-Aware Fusion via Dempster–Shafer (CMPD), IEEE TMM 2023, Li, Zhang, Hu, Fu, Zhu (IEEE TMM 25:3420–3431) — *evidential; decision-level; pedestrian*
2. ProbEn, ECCV 2022, Chen, Shi, Ye, Mertz, Ramanan, Kong [[Paper](https://arxiv.org/abs/2104.02904)] — *missing-modality; decision-level; ensemble; pedestrian*

## Appendix — Related Work Beyond RGBT Detection

Not RGBT detection papers. They are collected because their methods or protocols transfer directly (quality-aware fusion, imbalance and missing-modality learning, corruption benchmarks, test-time intervention). They are deliberately kept out of the main list above.

### Robust & Dynamic Fusion (General Multimodal)

1. MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion, CVPR 2025, Park, Kim, Kim, Choi [[Paper](https://arxiv.org/abs/2503.19776)] — *expert-routing; degraded-modality; lidar-camera*
2. MEFormer, arXiv 2024, Cha et al. [[Paper](https://arxiv.org/abs/2407.19156)] — *negative-fusion; degraded-modality*
3. Multimodal Fusion on Low-quality Data: A Comprehensive Survey, arXiv 2024, Zhang et al. [[Paper](https://arxiv.org/abs/2404.18947)] — *survey; low-quality-data; missing-modality*
4. DynMM, CVPR Workshops 2023, Xue & Marculescu [[Paper](https://arxiv.org/abs/2204.00102)] — *dynamic-fusion; efficiency*
5. Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF), ICML 2023, Zhang et al. [[Paper](https://arxiv.org/abs/2306.02050)] — *quality-aware; low-quality-data*
6. Trusted Multi-View Classification (TMC), ICLR 2021, Han, Zhang, Fu, Zhou [[Paper](https://arxiv.org/abs/2102.02051)] — *evidential; trusted-fusion*

### Corruption Robustness Benchmarks (Driving / 3D)

1. SB-BEVFusion, arXiv (ICIP 2026) 2026, Essl et al. [[Paper](https://arxiv.org/abs/2605.11799)] — *corrupted-vs-missing; lidar-camera*
2. MultiCorrupt, IEEE IV 2024, Beemelmanns, Zhang, Eckstein [[Paper](https://arxiv.org/abs/2402.11677)] — *benchmark; corruption*
3. Benchmarking Robustness of 3D Object Detection to Common Corruptions, CVPR 2023, Dong et al. [[Paper](https://arxiv.org/abs/2303.11040)] — *benchmark; corruption*

### Modality Imbalance & Missing-Modality Learning (General)

1. MM-CKD, arXiv 2024, Sang, Funakoshi, Okumura [[Paper](https://arxiv.org/abs/2410.08692)] — *missing-modality; distillation*
2. MMPareto, ICML 2024, Wei & Hu [[Paper](https://arxiv.org/abs/2405.17730)] — *modality-imbalance; gradient-conflict*
3. Multimodal Learning with Missing Modalities: A Survey, arXiv (TMLR) 2024, Wu, Wang, Chen [[Paper](https://arxiv.org/abs/2409.07825)] — *survey; missing-modality*
4. ReconBoost, ICML 2024, Hua, Xu, Bao, Yang, Huang [[Paper](https://proceedings.mlr.press/v235/hua24a.html)] — *modality-imbalance; modality-competition*
5. PMR: Prototypical Modal Rebalance, CVPR 2023, Fan, Xu, Wang, Wang, Guo [[Paper](https://doi.org/10.1109/CVPR52729.2023.01918)] — *modality-imbalance*
6. ShaSpec, CVPR 2023, Wang et al. [[Paper](https://arxiv.org/abs/2307.14126)] — *missing-modality*
7. OGM-GE, CVPR (Oral) 2022, Peng, Wei, Deng, Wang, Hu [[Paper](https://arxiv.org/abs/2203.15332)] — *modality-imbalance; gradient-modulation*
8. SMIL, AAAI 2021, Ma et al. [[Paper](https://arxiv.org/abs/2103.05677)] — *missing-modality*

### Test-Time Adaptation, Intervention & Amortized Optimization

1. Inference-Time Intervention (ITI), NeurIPS Spotlight 2023, Li, Patel, Viégas, Pfister, Wattenberg [[Paper](https://arxiv.org/abs/2306.03341)] — *test-time-intervention*
2. MEMO, NeurIPS 2022, Zhang, Levine, Finn [[Paper](https://arxiv.org/abs/2110.09506)] — *test-time-adaptation*
3. Tent, ICLR 2021, Wang, Shelhamer, Liu, Olshausen, Darrell [[Paper](https://arxiv.org/abs/2006.10726)] — *test-time-adaptation*
4. OptNet, ICML 2017, Amos & Kolter [[Paper](https://arxiv.org/abs/1703.00443)] — *amortized-optimization*

## Repository Files

- [datasets.md](datasets.md) — dataset tables, KAIST tools, and robustness benchmarks
- [bibliography.md](bibliography.md) — all entries in a detailed table (contribution and notes), in the same classification as this README
- [papers.csv](papers.csv) — structured data: section, subsection, tags, links, contribution, notes
- [references.bib](references.bib) — BibTeX for all entries
- [learning-roadmap.md](learning-roadmap.md) — a staged learning path through this list (stages 0–6); the roadmap is a reading order, separate from the classification above

## Adding an Entry

One line per paper: `Title, Venue Year, First Author et al., [[Paper](url)] [[Code](url)] — *tags*`. Decide the section by fusion level first (pixel / feature / decision), then the architecture family; put challenges in tags, never in a new section. Non-RGBT work goes to the Appendix. Add the same entry to papers.csv, references.bib, and bibliography.md. Only add entries whose paper link you have verified.

## Related Lists

- [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) — the broader RGB-T fusion collection (pedestrian/aerial detection, segmentation, salient detection, crowd counting, tracking)
- [Awesome-RGBT](https://github.com/VisionVerse/Awesome-RGBT) — RGB-T fusion across tasks
- [MOD-ZOO](https://github.com/DocF/MOD-ZOO) — curated resources accompanying a multispectral object detection survey
