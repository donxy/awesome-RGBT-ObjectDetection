# owesome-RGBT-ObjectDetection

A curated collection of **RGBT object detection** resources — papers, datasets, and code.

RGBT (also written RGB-T, RGB-Thermal, multispectral, or visible–infrared) object detection fuses a visible-light image with a thermal (LWIR) image to detect objects under conditions where either modality alone fails — darkness, glare, smoke, or adverse weather.

**Scope.** This list covers *object detection only*: general, pedestrian, vehicle, and aerial/UAV detection with paired visible–thermal imagery. Semantic segmentation, salient object detection, crowd counting, and tracking are out of scope — see the related lists at the bottom. Every entry appears exactly once, under its primary theme; entries carry a paper link and a code link where an official repository is known.

## News

- [2026-10-25] Restructured as a general, detection-only list: datasets first, papers organised by theme, plus structured data files (CSV / BibTeX), a detailed bibliography, and a learning roadmap. Initial collection: 42 papers.

## Contents

1. [Datasets](#datasets)
2. [Surveys & Benchmarks](#surveys--benchmarks)
3. [Fusion Architectures — Cross-Attention & Transformers](#fusion-architectures--cross-attention--transformers)
4. [Fusion Architectures — YOLO-Based Detectors](#fusion-architectures--yolo-based-detectors)
5. [Fusion Architectures — State-Space (Mamba)](#fusion-architectures--state-space-mamba)
6. [Fusion Architectures — Task-Coupled Fusion (Fusion for Detection)](#fusion-architectures--task-coupled-fusion-fusion-for-detection)
7. [Fusion Architectures — Quality- & Conflict-Aware Fusion](#fusion-architectures--quality---conflict-aware-fusion)
8. [Fusion Architectures — Foundation-Model Adapters](#fusion-architectures--foundation-model-adapters)
9. [Robust Fusion under Degraded or Missing Modalities](#robust-fusion-under-degraded-or-missing-modalities)
10. [Modality Imbalance & Missing-Modality Training](#modality-imbalance--missing-modality-training)
11. [Test-Time Adaptation, Intervention & Amortized Optimization](#test-time-adaptation-intervention--amortized-optimization)
12. [Repository Files](#repository-files)
13. [Adding an Entry](#adding-an-entry)
14. [Related Lists](#related-lists)

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

1. WiSE-OD, WACV 2026, Medeiros et al. [[Paper](https://arxiv.org/abs/2507.18925)]
2. Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption, IEEE TPAMI 2025, Liu et al. [[Paper](https://arxiv.org/abs/2501.10761)]
3. MSOD-Bench: Optimizing Multispectral Object Detection, arXiv 2024, Zhou et al. [[Paper](https://arxiv.org/abs/2411.18288)]
4. Multimodal Fusion on Low-quality Data: A Comprehensive Survey, arXiv 2024, Zhang et al. [[Paper](https://arxiv.org/abs/2404.18947)]
5. Multimodal Learning with Missing Modalities: A Survey, arXiv (TMLR) 2024, Wu, Wang, Chen [[Paper](https://arxiv.org/abs/2409.07825)]

## Fusion Architectures — Cross-Attention & Transformers

1. C2Former: Calibrated and Complementary Transformer, IEEE TGRS 2024, Yuan & Wei [[Paper](https://arxiv.org/abs/2306.16175)] [[Code](https://github.com/yuanmaoxun/C2Former)]
2. DAMSDet, ECCV 2024, Guo, Gao, Liu, Meng, Gao [[Paper](https://eccv.ecva.net/virtual/2024/poster/801)] [[Code](https://github.com/gjj45/DAMSDet)]
3. GM-DETR, CVPR Workshops 2024, Xiao et al. ((CVPRW 2024, pp.5541–5549))
4. Cross-Modality Fusion Transformer (CFT), arXiv 2021, Fang, Han, Wang [[Paper](https://arxiv.org/abs/2111.00273)]

## Fusion Architectures — YOLO-Based Detectors

1. YOLOv11-RGBT, arXiv 2025, Wan et al. [[Paper](https://arxiv.org/abs/2506.14696)] [[Code](https://github.com/wandahangFY/YOLOv11-RGBT)]
2. DEYOLO, ICPR 2024, Chen et al. [[Paper](https://arxiv.org/abs/2412.04931)]

## Fusion Architectures — State-Space (Mamba)

1. Fusion-Mamba, IEEE TMM 2025, Dong et al. [[Paper](https://doi.org/10.1109/TMM.2025.3599020)]
2. WaveMamba, ICCV 2025, Zhu et al. [[Paper](https://arxiv.org/abs/2507.18173)] [[Code](https://github.com/EhanDong/WaveMamba)]

## Fusion Architectures — Task-Coupled Fusion (Fusion for Detection)

1. ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection, Pattern Recognition 2024, Shen et al. [[Paper](https://ieeexplore.ieee.org/abstract/document/10225383)] [[Code](https://github.com/chanchanchan97/ICAFusion)]
2. CDDFuse, CVPR 2023, Zhao et al. [[Paper](https://arxiv.org/abs/2211.14461)]
3. MetaFusion, CVPR 2023, Zhao et al. [[Paper](https://doi.org/10.1109/CVPR52729.2023.01341)]
4. TarDAL: Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection, CVPR 2022, Liu et al. [[Paper](https://arxiv.org/abs/2203.16220)] [[Code](https://github.com/JinyuanLiu-CV/TarDAL)]

## Fusion Architectures — Quality- & Conflict-Aware Fusion

1. LRAF-Net, IEEE TNNLS 2023, Fu et al. [[Paper](https://doi.org/10.1109/TNNLS.2023.3266452)]
2. CALNet (Cross-Modal Conflict-Aware Learning), ACM MM 2023, He, Tang, Zou, Zhang [[Paper](https://doi.org/10.1145/3581783.3612651)]
3. Confidence-Aware Fusion via Dempster–Shafer (CMPD), IEEE TMM 2023, Li, Zhang, Hu, Fu, Zhu ((IEEE TMM 25:3420–3431))

## Fusion Architectures — Foundation-Model Adapters

1. UniRGB-IR, ACM MM 2025, Yuan et al. [[Paper](https://arxiv.org/abs/2404.17360)]

## Robust Fusion under Degraded or Missing Modalities

1. SB-BEVFusion, arXiv (ICIP 2026) 2026, Essl et al. [[Paper](https://arxiv.org/abs/2605.11799)]
2. Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance, Pattern Recognition Letters 2025, Tian, Yang, Zhu, Wang, He [[Paper](https://arxiv.org/abs/2505.22154)]
3. MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion, CVPR 2025, Park, Kim, Kim, Choi [[Paper](https://arxiv.org/abs/2503.19776)]
4. MEFormer, arXiv 2024, Cha et al. [[Paper](https://arxiv.org/abs/2407.19156)]
5. MultiCorrupt, IEEE IV 2024, Beemelmanns, Zhang, Eckstein [[Paper](https://arxiv.org/abs/2402.11677)]
6. Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF), ICML 2023, Zhang et al. [[Paper](https://arxiv.org/abs/2306.02050)]
7. Benchmarking Robustness of 3D Object Detection to Common Corruptions, CVPR 2023, Dong et al. [[Paper](https://arxiv.org/abs/2303.11040)]
8. DynMM, CVPR Workshops 2023, Xue & Marculescu [[Paper](https://arxiv.org/abs/2204.00102)]
9. Trusted Multi-View Classification (TMC), ICLR 2021, Han, Zhang, Fu, Zhou [[Paper](https://arxiv.org/abs/2102.02051)]

## Modality Imbalance & Missing-Modality Training

1. ReconBoost, ICML 2024, Hua, Xu, Bao, Yang, Huang [[Paper](https://proceedings.mlr.press/v235/hua24a.html)]
2. MMPareto, ICML 2024, Wei & Hu [[Paper](https://arxiv.org/abs/2405.17730)]
3. MM-CKD, arXiv 2024, Sang, Funakoshi, Okumura [[Paper](https://arxiv.org/abs/2410.08692)]
4. PMR: Prototypical Modal Rebalance, CVPR 2023, Fan, Xu, Wang, Wang, Guo [[Paper](https://doi.org/10.1109/CVPR52729.2023.01918)]
5. ShaSpec, CVPR 2023, Wang et al. [[Paper](https://arxiv.org/abs/2307.14126)]
6. OGM-GE, CVPR (Oral) 2022, Peng, Wei, Deng, Wang, Hu [[Paper](https://arxiv.org/abs/2203.15332)]
7. ProbEn, ECCV 2022, Chen, Shi, Ye, Mertz, Ramanan, Kong [[Paper](https://arxiv.org/abs/2104.02904)]
8. SMIL, AAAI 2021, Ma et al. [[Paper](https://arxiv.org/abs/2103.05677)]

## Test-Time Adaptation, Intervention & Amortized Optimization

1. Inference-Time Intervention (ITI), NeurIPS Spotlight 2023, Li, Patel, Viégas, Pfister, Wattenberg [[Paper](https://arxiv.org/abs/2306.03341)]
2. MEMO, NeurIPS 2022, Zhang, Levine, Finn [[Paper](https://arxiv.org/abs/2110.09506)]
3. Tent, ICLR 2021, Wang, Shelhamer, Liu, Olshausen, Darrell [[Paper](https://arxiv.org/abs/2006.10726)]
4. OptNet, ICML 2017, Amos & Kolter [[Paper](https://arxiv.org/abs/1703.00443)]

## Repository Files

- [datasets.md](datasets.md) — dataset tables, KAIST tools, and robustness benchmarks
- [bibliography.md](bibliography.md) — the same papers in a detailed table: one-sentence contribution and notes for every entry
- [papers.csv](papers.csv) — structured data for all entries (theme, title, authors, year, venue, paper/code links)
- [references.bib](references.bib) — BibTeX for all entries
- [learning-roadmap.md](learning-roadmap.md) — a staged learning path through this list (stages 0–6), with goals and self-check criteria per stage

## Adding an Entry

One line per paper, in the format used above: `Title, Venue Year, First Author et al., [[Paper](url)] [[Code](url)]`. Place it under exactly one theme, newest first within the theme. Add the same entry to papers.csv, references.bib, and bibliography.md so the four views stay in sync. Only add entries whose paper link you have verified.

## Related Lists

- [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) — the broader RGB-T fusion collection (pedestrian/aerial detection, segmentation, salient detection, crowd counting, tracking)
- [Awesome-RGBT](https://github.com/VisionVerse/Awesome-RGBT) — RGB-T fusion across tasks
- [MOD-ZOO](https://github.com/DocF/MOD-ZOO) — curated resources accompanying a multispectral object detection survey
