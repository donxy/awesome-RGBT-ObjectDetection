# Learning Roadmap — RGBT Object Detection

A staged learning path through the papers in this repository. The principle: read by *question*, not by list order — each stage answers one question a newcomer (or a reviewer) will ask. Deep-read the core papers, skim the supporting ones with the abstract and method figure, and only look up the rest when writing.

**How to work through a paper:** (1) read the guided question for the stage first; (2) read the paper's abstract, introduction, and method figure; (3) write a note card — Problem / Method / Datasets & results / Relation to other entries / Open questions; (4) at the end of each stage, explain the stage's question out loud in your own words before moving on.

## Stage 0 — Build the Map

**Question:** What does the field look like as a whole?  
**Depth:** 略读  
**Pass criterion:** You can name the main fusion families, the standard datasets, and what a fair comparison looks like.

- Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption — Liu et al., 2025, IEEE TPAMI · [Paper](https://arxiv.org/abs/2501.10761)
- MSOD-Bench: Optimizing Multispectral Object Detection — Zhou et al., 2024, arXiv · [Paper](https://arxiv.org/abs/2411.18288)

## Stage 1 — Architecture Lineage

**Question:** Where does a detector fuse, and why does the fusion point matter?  
**Depth:** 精读 YOLOv11-RGBT 与 DAMSDet，其余导读  
**Pass criterion:** You can draw a fusion taxonomy (early / mid / late, attention, DETR queries, state-space) and locate any new paper on it.

- Cross-Modality Fusion Transformer (CFT) — Fang, Han, Wang, 2021, arXiv · [Paper](https://arxiv.org/abs/2111.00273)
- YOLOv11-RGBT — Wan et al., 2025, arXiv · [Paper](https://arxiv.org/abs/2506.14696)
- DAMSDet — Guo, Gao, Liu, Meng, Gao, 2024, ECCV · [Paper](https://eccv.ecva.net/virtual/2024/poster/801)
- C2Former: Calibrated and Complementary Transformer — Yuan & Wei, 2024, IEEE TGRS · [Paper](https://arxiv.org/abs/2306.16175)
- Fusion-Mamba — Dong et al., 2025, IEEE TMM · [Paper](https://doi.org/10.1109/TMM.2025.3599020)
- DEYOLO — Chen et al., 2024, ICPR · [Paper](https://arxiv.org/abs/2412.04931)

## Stage 2 — Robust & Quality-Aware Fusion (the core stage)

**Question:** When one modality degrades, should the model down-weight it or repair it?  
**Depth:** 精读 Tian et al. 2025，其余精读/导读  
**Pass criterion:** You can state the weighting-vs-correction distinction precisely and contrast the representative methods on it.

- Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance — Tian, Yang, Zhu, Wang, He, 2025, Pattern Recognition Letters · [Paper](https://arxiv.org/abs/2505.22154)
- Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF) — Zhang et al., 2023, ICML · [Paper](https://arxiv.org/abs/2306.02050)
- Confidence-Aware Fusion via Dempster–Shafer (CMPD) — Li, Zhang, Hu, Fu, Zhu, 2023, IEEE TMM
- Multimodal Fusion on Low-quality Data: A Comprehensive Survey — Zhang et al., 2024, arXiv · [Paper](https://arxiv.org/abs/2404.18947)
- Trusted Multi-View Classification (TMC) — Han, Zhang, Fu, Zhou, 2021, ICLR · [Paper](https://arxiv.org/abs/2102.02051)
- CALNet (Cross-Modal Conflict-Aware Learning) — He, Tang, Zou, Zhang, 2023, ACM MM · [Paper](https://doi.org/10.1145/3581783.3612651)
- LRAF-Net — Fu et al., 2023, IEEE TNNLS · [Paper](https://doi.org/10.1109/TNNLS.2023.3266452)

## Stage 3 — Degradation Protocols

**Question:** How do you evaluate robustness honestly: corrupted is not missing.  
**Depth:** 导读为主，WiSE-OD 精读协议部分  
**Pass criterion:** You can audit a corruption suite against LLVIP-C / FLIR-C style protocols (corruption types, severities, mPC).

- MEFormer — Cha et al., 2024, arXiv · [Paper](https://arxiv.org/abs/2407.19156)
- MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion — Park, Kim, Kim, Choi, 2025, CVPR · [Paper](https://arxiv.org/abs/2503.19776)
- WiSE-OD — Medeiros et al., 2026, WACV · [Paper](https://arxiv.org/abs/2507.18925)
- Benchmarking Robustness of 3D Object Detection to Common Corruptions — Dong et al., 2023, CVPR · [Paper](https://arxiv.org/abs/2303.11040)
- MultiCorrupt — Beemelmanns, Zhang, Eckstein, 2024, IEEE IV · [Paper](https://arxiv.org/abs/2402.11677)
- SB-BEVFusion — Essl et al., 2026, arXiv (ICIP 2026) · [Paper](https://arxiv.org/abs/2605.11799)
- DynMM — Xue & Marculescu, 2023, CVPR Workshops · [Paper](https://arxiv.org/abs/2204.00102)

## Stage 4 — Imbalance & Missing-Modality Training

**Question:** What can training-time remedies fix, and what can they not?  
**Depth:** 精读 ProbEn，其余导读  
**Pass criterion:** You can explain why training-time methods assume the failure mode is known or missing — not actively harmful — and position modality dropout in this family.

- OGM-GE — Peng, Wei, Deng, Wang, Hu, 2022, CVPR (Oral) · [Paper](https://arxiv.org/abs/2203.15332)
- PMR: Prototypical Modal Rebalance — Fan, Xu, Wang, Wang, Guo, 2023, CVPR · [Paper](https://doi.org/10.1109/CVPR52729.2023.01918)
- ReconBoost — Hua, Xu, Bao, Yang, Huang, 2024, ICML · [Paper](https://proceedings.mlr.press/v235/hua24a.html)
- MMPareto — Wei & Hu, 2024, ICML · [Paper](https://arxiv.org/abs/2405.17730)
- SMIL — Ma et al., 2021, AAAI · [Paper](https://arxiv.org/abs/2103.05677)
- ShaSpec — Wang et al., 2023, CVPR · [Paper](https://arxiv.org/abs/2307.14126)
- ProbEn — Chen, Shi, Ye, Mertz, Ramanan, Kong, 2022, ECCV · [Paper](https://arxiv.org/abs/2104.02904)
- Multimodal Learning with Missing Modalities: A Survey — Wu, Wang, Chen, 2024, arXiv (TMLR) · [Paper](https://arxiv.org/abs/2409.07825)
- MM-CKD — Sang, Funakoshi, Okumura, 2024, arXiv · [Paper](https://arxiv.org/abs/2410.08692)

## Stage 5 — Test-Time Intervention

**Question:** What does it mean to intervene at inference instead of retraining?  
**Depth:** 导读  
**Pass criterion:** You can distinguish parameter-level unsupervised adaptation from feature-level supervised correction, in one paragraph.

- Tent — Wang, Shelhamer, Liu, Olshausen, Darrell, 2021, ICLR · [Paper](https://arxiv.org/abs/2006.10726)
- MEMO — Zhang, Levine, Finn, 2022, NeurIPS · [Paper](https://arxiv.org/abs/2110.09506)
- Inference-Time Intervention (ITI) — Li, Patel, Viégas, Pfister, Wattenberg, 2023, NeurIPS Spotlight · [Paper](https://arxiv.org/abs/2306.03341)
- OptNet — Amos & Kolter, 2017, ICML · [Paper](https://arxiv.org/abs/1703.00443)

## Stage 6 — Fill the Gaps

**Question:** Complete the task-coupled and recent-architecture picture, as needed when writing.  
**Depth:** 查阅 / 速览  
**Pass criterion:** You can place TarDAL, ICAFusion, CDDFuse, MetaFusion, WaveMamba, GM-DETR, and UniRGB-IR in the taxonomy without re-reading them.

- WaveMamba — Zhu et al., 2025, ICCV · [Paper](https://arxiv.org/abs/2507.18173)
- CDDFuse — Zhao et al., 2023, CVPR · [Paper](https://arxiv.org/abs/2211.14461)
- MetaFusion — Zhao et al., 2023, CVPR · [Paper](https://doi.org/10.1109/CVPR52729.2023.01341)
- GM-DETR — Xiao et al., 2024, CVPR Workshops
- UniRGB-IR — Yuan et al., 2025, ACM MM · [Paper](https://arxiv.org/abs/2404.17360)
- TarDAL: Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection — Liu et al., 2022, CVPR · [Paper](https://arxiv.org/abs/2203.16220)
- ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection — Shen et al., 2024, Pattern Recognition · [Paper](https://ieeexplore.ieee.org/abstract/document/10225383)

**Pace:** about 4–5 papers per week finishes the path in roughly 4 weeks. End each stage with a short review: state the stage question, your answer, and the two entries that best support it.
