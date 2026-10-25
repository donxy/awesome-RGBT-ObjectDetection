# Detailed Bibliography — RGBT Object Detection

Detailed companion to the [README](README.md): every entry with a one-sentence contribution and notes, in the README's technical-route classification (core list first, appendix second).

## Surveys & Benchmarks

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| WiSE-OD — Medeiros et al., 2026, WACV | [Paper](https://arxiv.org/abs/2507.18925) | degraded-modality; benchmark; out-of-distribution | Weight-space ensembling for OOD RGB-T detection; introduces LLVIP-C / FLIR-C. | Corruption-benchmark protocol (AP50, mPC) a reviewer may demand alignment with. |
| Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption — Liu et al., 2025, IEEE TPAMI | [Paper](https://arxiv.org/abs/2501.10761) | survey | Comprehensive IVIF survey organized around task adaptation. | Authoritative section anchor from the TarDAL/M3FD group. |
| MSOD-Bench: Optimizing Multispectral Object Detection — Zhou et al., 2024, arXiv | [Paper](https://arxiv.org/abs/2411.18288) | benchmark | Standardized re-implementation/benchmark of 20+ RGB-T detectors. | Fair-comparison framing; guards against cherry-picked baseline numbers. |

## Pixel-Level Fusion for Detection

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| CDDFuse — Zhao et al., 2023, CVPR | [Paper](https://arxiv.org/abs/2211.14461) | image-fusion; task-coupled | Correlation-driven dual-branch decomposition fusion, incl. downstream detection. | Task-coupled fusion line (fusion-for-detection). |
| MetaFusion — Zhao et al., 2023, CVPR | [Paper](https://doi.org/10.1109/CVPR52729.2023.01341) | image-fusion; task-coupled | Detection-guided meta-feature embedding mutually promoting fusion and detection. | Supports the manuscript's task-constrained motivation. |
| TarDAL: Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection — Liu et al., 2022, CVPR | [Paper](https://arxiv.org/abs/2203.16220) · [Code](https://github.com/JinyuanLiu-CV/TarDAL) | image-fusion; task-coupled | Target-aware dual adversarial learning that fuses infrared and visible images for detection; introduced the M3FD benchmark. | Classic task-coupled fusion entry; the M3FD dataset paper. |

## Feature-Level Fusion — Attention, Transformers & Foundation Models

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| UniRGB-IR — Yuan et al., 2025, ACM MM | [Paper](https://arxiv.org/abs/2404.17360) | foundation-model; adapter | Adapter injection of RGB-IR fusion into a frozen ViT foundation model. | Foundation-model line; FLIR mAP 44.1 / LLVIP 63.2. |
| C2Former: Calibrated and Complementary Transformer — Yuan & Wei, 2024, IEEE TGRS | [Paper](https://arxiv.org/abs/2306.16175) · [Code](https://github.com/yuanmaoxun/C2Former) | alignment; cross-attention; transformer | Cross-attention calibration + adaptive sampling for misaligned RGB-T pairs. | Leading cross-attention line; note it does not evaluate on LLVIP/FLIR/M3FD. |
| DAMSDet — Guo, Gao, Liu, Meng, Gao, 2024, ECCV | [Paper](https://eccv.ecva.net/virtual/2024/poster/801) · [Code](https://github.com/gjj45/DAMSDet) | transformer; detr | Competitive query selection + deformable cross-attention in a DETR RGB-T detector. | SOTA DETR representative on M3FD/FLIR/LLVIP (FLIR mAP 49.3, LLVIP mAP 69.6). |
| GM-DETR — Xiao et al., 2024, CVPR Workshops | (CVPRW 2024, pp.5541–5549) | transformer; detr; efficiency | Lightweight DETR-style RGB-T detector. | Additional DETR-line data point on FLIR + LLVIP. |
| ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection — Shen et al., 2024, Pattern Recognition | [Paper](https://ieeexplore.ieee.org/abstract/document/10225383) · [Code](https://github.com/chanchanchan97/ICAFusion) | cross-attention | Iterative cross-attention guided feature fusion for multispectral object detection. | Established cross-attention fusion reference, widely used as a comparison baseline (LLVIP, M3FD). |
| Cross-Modality Fusion Transformer (CFT) — Fang, Han, Wang, 2021, arXiv | [Paper](https://arxiv.org/abs/2111.00273) | cross-attention; transformer | YOLOv5-based transformer cross-modal fusion for RGB-T detection. | Canonical transformer-fusion baseline on FLIR + LLVIP; appears in all recent comparison tables. |

## Feature-Level Fusion — Dual-Stream CNN & YOLO-Based Detectors

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| YOLOv11-RGBT — Wan et al., 2025, arXiv | [Paper](https://arxiv.org/abs/2506.14696) · [Code](https://github.com/wandahangFY/YOLOv11-RGBT) | yolo; efficiency | Six-fusion-mode study over YOLO/RT-DETR with P3 mid-fusion + controllable fine-tuning (MCF). | Direct predecessor: same backbone family and mid-fusion design point as the manuscript's detector. |
| DEYOLO — Chen et al., 2024, ICPR | [Paper](https://arxiv.org/abs/2412.04931) | yolo; dual-stream | Dual semantic/spatial enhancement modules on YOLOv8 dual streams. | YOLO-line comparator on M3FD + LLVIP. |
| LRAF-Net — Fu et al., 2023, IEEE TNNLS | [Paper](https://doi.org/10.1109/TNNLS.2023.3266452) | dual-stream; modality-bias; mask-augmentation | Long-range attention fusion + complementary-mask augmentation vs single-modality bias. | Bridges architecture and imbalance sections; FLIR/LLVIP results. |

## Feature-Level Fusion — State-Space Models (Mamba)

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| Fusion-Mamba — Dong et al., 2025, IEEE TMM | [Paper](https://doi.org/10.1109/TMM.2025.3599020) | mamba; state-space | State-space (Mamba) cross-modal fusion for IR-VIS detection. | Current SOTA-line representative (M3FD mAP 61.9 in comparative tables). |
| WaveMamba — Zhu et al., 2025, ICCV | [Paper](https://arxiv.org/abs/2507.18173) · [Code](https://github.com/EhanDong/WaveMamba) | mamba; state-space; frequency-domain | Wavelet frequency-decomposed Mamba fusion with YOLOv8 head. | Latest Mamba-line SOTA claim on M3FD/LLVIP/FLIR-Aligned. |

## Feature-Level Fusion — Quality- & Conflict-Aware Fusion

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance — Tian, Yang, Zhu, Wang, He, 2025, Pattern Recognition Letters | [Paper](https://arxiv.org/abs/2505.22154) | degraded-modality; quality-aware; modality-imbalance | Quality-mask interaction + pseudo-degradation + EMA base/auxiliary consistency for imbalanced RGB-T. | **Closest prior work** — see §(b). KAIST LAMR + FLIR mAP; Gaussian-noise and contrast-degradation tests. |
| CALNet (Cross-Modal Conflict-Aware Learning) — He, Tang, Zou, Zhang, 2023, ACM MM | [Paper](https://doi.org/10.1145/3581783.3612651) | conflict-aware; aerial | Rectifies cross-modal feature conflict before selective fusion. | "Conflict" framing is a conceptual neighbour of corrupted-modality harm. |

## Decision-Level & Evidential Fusion

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| Confidence-Aware Fusion via Dempster–Shafer (CMPD) — Li, Zhang, Hu, Fu, Zhu, 2023, IEEE TMM | (IEEE TMM 25:3420–3431) | evidential; decision-level; pedestrian | Per-modality confidence subnetworks combined evidentially for pedestrian detection. | In-domain precedent for quality/confidence-weighted RGB-T fusion. |
| ProbEn — Chen, Shi, Ye, Mertz, Ramanan, Kong, 2022, ECCV | [Paper](https://arxiv.org/abs/2104.02904) | missing-modality; decision-level; ensemble; pedestrian | Probabilistic late ensembling; marginalization handles missing modalities natively. | Only verified detection-native missing-modality method; KAIST + FLIR. |

## Appendix — Related Work Beyond RGBT Detection

## Appendix: Robust & Dynamic Fusion (General Multimodal)

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion — Park, Kim, Kim, Choi, 2025, CVPR | [Paper](https://arxiv.org/abs/2503.19776) | expert-routing; degraded-modality; lidar-camera | Per-query routing among camera/LiDAR/fused experts by local feature quality. | Strongest analogue of region-dependent takeover (routing, not correction; 3D driving). |
| MEFormer — Cha et al., 2024, arXiv | [Paper](https://arxiv.org/abs/2407.19156) | negative-fusion; degraded-modality | Defines and mitigates "negative fusion" from defective modalities. | Names the manuscript's core phenomenon; cite the term. |
| Multimodal Fusion on Low-quality Data: A Comprehensive Survey — Zhang et al., 2024, arXiv | [Paper](https://arxiv.org/abs/2404.18947) | survey; low-quality-data; missing-modality | Taxonomy separating noisy, incomplete, imbalanced, quality-varying multimodal data. | Cleanest citation legitimizing the corrupted ≠ missing distinction. |
| DynMM — Xue & Marculescu, 2023, CVPR Workshops | [Paper](https://arxiv.org/abs/2204.00102) | dynamic-fusion; efficiency | On-the-fly gating over modality and fusion-level computation paths. | Dynamic-fusion precedent (efficiency-motivated). |
| Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF) — Zhang et al., 2023, ICML | [Paper](https://arxiv.org/abs/2306.02050) | quality-aware; low-quality-data | Energy-based uncertainty drives dynamic decision-level fusion weights, with guarantees. | Reference quality-aware fusion method; classification-only contrast to feature correction. |
| Trusted Multi-View Classification (TMC) — Han, Zhang, Fu, Zhou, 2021, ICLR | [Paper](https://arxiv.org/abs/2102.02051) | evidential; trusted-fusion | Evidential per-view quality assessment with Dempster–Shafer fusion. | Foundational trusted/quality-aware fusion citation. |

## Appendix: Corruption Robustness Benchmarks (Driving / 3D)

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| SB-BEVFusion — Essl et al., 2026, arXiv (ICIP 2026) | [Paper](https://arxiv.org/abs/2605.11799) | corrupted-vs-missing; lidar-camera | BEV fusion explicitly treating corrupted vs missing sensors as distinct cases. | Verbatim corrupted-vs-missing distinction; very recent, camera-LiDAR. |
| MultiCorrupt — Beemelmanns, Zhang, Eckstein, 2024, IEEE IV | [Paper](https://arxiv.org/abs/2402.11677) | benchmark; corruption | 10 LiDAR-camera corruptions × 3 severities with Resistance Ability metric. | Severity-graded corruption evaluation model. |
| Benchmarking Robustness of 3D Object Detection to Common Corruptions — Dong et al., 2023, CVPR | [Paper](https://arxiv.org/abs/2303.11040) | benchmark; corruption | 27-corruption benchmark; fusion models more robust, motion corruptions worst. | Corruption-protocol precedent for the manuscript's degradation suite. |

## Appendix: Modality Imbalance & Missing-Modality Learning (General)

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| MM-CKD — Sang, Funakoshi, Okumura, 2024, arXiv | [Paper](https://arxiv.org/abs/2410.08692) | missing-modality; distillation | Cross-modal knowledge distillation robust to missing modality (sentiment). | Only distillation-for-missing citation found; non-vision. |
| MMPareto — Wei & Hu, 2024, ICML | [Paper](https://arxiv.org/abs/2405.17730) | modality-imbalance; gradient-conflict | Pareto-integrated gradients resolving multimodal/unimodal gradient conflict. | Gradient-conflict framing. |
| Multimodal Learning with Missing Modalities: A Survey — Wu, Wang, Chen, 2024, arXiv (TMLR) | [Paper](https://arxiv.org/abs/2409.07825) | survey; missing-modality | Survey of imputation/representation/distillation approaches to missing modalities. | Section anchor for Q3. |
| ReconBoost — Hua, Xu, Bao, Yang, Huang, 2024, ICML | [Paper](https://proceedings.mlr.press/v235/hua24a.html) | modality-imbalance; modality-competition | Modality-alternating boosting with KL reconcilement vs competition. | Most recent reconcilement-framed balancing method. |
| PMR: Prototypical Modal Rebalance — Fan, Xu, Wang, Wang, Guo, 2023, CVPR | [Paper](https://doi.org/10.1109/CVPR52729.2023.01918) | modality-imbalance | Prototypes accelerate the slow-learning modality; entropy regularizer vs dominant modality. | Balancing line representative. |
| ShaSpec — Wang et al., 2023, CVPR | [Paper](https://arxiv.org/abs/2307.14126) | missing-modality | Shared-specific features + residual fusion for missing modality at train/test. | Representation-side missing-modality approach. |
| OGM-GE — Peng, Wei, Deng, Wang, Hu, 2022, CVPR (Oral) | [Paper](https://arxiv.org/abs/2203.15332) | modality-imbalance; gradient-modulation | On-the-fly gradient modulation by modality contribution discrepancy. | Standard balancing citation next to the existing competition papers. |
| SMIL — Ma et al., 2021, AAAI | [Paper](https://arxiv.org/abs/2103.05677) | missing-modality | Bayesian meta-learning for severely (≤90%) missing modalities. | Canonical missing-modality method citation. |

## Appendix: Test-Time Adaptation, Intervention & Amortized Optimization

| Paper | Link | Tags | Contribution | Notes |
|---|---|---|---|---|
| Inference-Time Intervention (ITI) — Li, Patel, Viégas, Pfister, Wattenberg, 2023, NeurIPS Spotlight | [Paper](https://arxiv.org/abs/2306.03341) | test-time-intervention | Shifts selected attention-head activations along probed directions at inference. | Terminological namesake of "intervention"; LLM-only, one clarifying sentence. |
| MEMO — Zhang, Levine, Finn, 2022, NeurIPS | [Paper](https://arxiv.org/abs/2110.09506) | test-time-adaptation | Per-test-point adaptation via marginal entropy over augmentations. | Single-point test-time intervention precedent. |
| Tent — Wang, Shelhamer, Liu, Olshausen, Darrell, 2021, ICLR | [Paper](https://arxiv.org/abs/2006.10726) | test-time-adaptation | Test-time entropy minimization over norm affine parameters. | Canonical "adapt at test time" contrast (parameter-level, unsupervised). |
| OptNet — Amos & Kolter, 2017, ICML | [Paper](https://arxiv.org/abs/1703.00443) | amortized-optimization | Differentiable QP layers via implicit KKT differentiation. | Foundational only; redundant given existing Amos/CF-OPT citations. |

## Verification Notes

- Links were verified against arXiv, publisher, or proceedings pages on 2026-10-25. Two entries (CMPD, GM-DETR) are recorded with volume/page references where no stable paper URL was verified.
- "TARDet" does not exist under that name in the verified literature; the work is TarDAL (CVPR 2022), included in the main list.
- CMDistill (IEEE JSTARS 2024) could not be independently verified and is excluded.
- Some performance figures in the notes come from comparative tables in other papers (secondary sources); check the original paper before citing a number.
