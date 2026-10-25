# Bibliography — RGBT Object Detection Literature Library

40 篇经核实的文献（2021–2026 为主，含少量基础工作），2026-10-25 调研时逐条对照 arXiv / 出版方 / 会议页面核实，每条都带 DOI 或 arXiv 链接（个别只有出版记录的条目标注了卷期页码）。

优先级分布：**must-cite 12 篇 · should-cite 18 篇 · optional 10 篇**

分类分布：RGBT architecture 13 · RGBT architecture / quality fusion 1 · Survey/benchmark 2 · Robust fusion 11 · Imbalance 4 · Missing modality 3 · Missing modality (detection) 1 · Missing modality / distillation 1 · Test-time adaptation 2 · Test-time intervention 1 · Amortized optimization 1

配套文件：[`papers.csv`](papers.csv)（同一批数据，可筛选/导入表格） · [`references.bib`](references.bib)（BibTeX）

## 文献表

| # | Category | Paper | Link | One-sentence contribution | Relevance | Priority |
|---|---|---|---|---|---|---|
| 1 | RGBT architecture | Cross-Modality Fusion Transformer (CFT) — Fang, Han, Wang, 2021, arXiv | [link](https://arxiv.org/abs/2111.00273) | YOLOv5-based transformer cross-modal fusion for RGB-T detection. | Canonical transformer-fusion baseline on FLIR + LLVIP; appears in all recent comparison tables. | must-cite |
| 2 | RGBT architecture | C2Former: Calibrated and Complementary Transformer — Yuan & Wei, 2024, IEEE TGRS | https://arxiv.org/abs/2306.16175 (DOI 10.1109/TGRS.2024.3376819) | Cross-attention calibration + adaptive sampling for misaligned RGB-T pairs. | Leading cross-attention line; note it does not evaluate on LLVIP/FLIR/M3FD. | must-cite |
| 3 | RGBT architecture | DAMSDet — Guo, Gao, Liu, Meng, Gao, 2024, ECCV | [link](https://eccv.ecva.net/virtual/2024/poster/801) | Competitive query selection + deformable cross-attention in a DETR RGB-T detector. | SOTA DETR representative on M3FD/FLIR/LLVIP (FLIR mAP 49.3, LLVIP mAP 69.6). | must-cite |
| 4 | RGBT architecture | YOLOv11-RGBT — Wan et al., 2025, arXiv | [link](https://arxiv.org/abs/2506.14696) | Six-fusion-mode study over YOLO/RT-DETR with P3 mid-fusion + controllable fine-tuning (MCF). | Direct predecessor: same backbone family and mid-fusion design point as the manuscript's detector. | must-cite |
| 5 | RGBT architecture | Fusion-Mamba — Dong et al., 2025, IEEE TMM | DOI 10.1109/TMM.2025.3599020 | State-space (Mamba) cross-modal fusion for IR-VIS detection. | Current SOTA-line representative (M3FD mAP 61.9 in comparative tables). | must-cite |
| 6 | RGBT architecture | DEYOLO — Chen et al., 2024, ICPR | [link](https://arxiv.org/abs/2412.04931) | Dual semantic/spatial enhancement modules on YOLOv8 dual streams. | YOLO-line comparator on M3FD + LLVIP. | should-cite |
| 7 | RGBT architecture | WaveMamba — Zhu et al., 2025, ICCV | [link](https://arxiv.org/abs/2507.18173) | Wavelet frequency-decomposed Mamba fusion with YOLOv8 head. | Latest Mamba-line SOTA claim on M3FD/LLVIP/FLIR-Aligned. | should-cite |
| 8 | RGBT architecture | LRAF-Net — Fu et al., 2023, IEEE TNNLS | DOI 10.1109/TNNLS.2023.3266452 | Long-range attention fusion + complementary-mask augmentation vs single-modality bias. | Bridges architecture and imbalance sections; FLIR/LLVIP results. | should-cite |
| 9 | RGBT architecture | CALNet (Cross-Modal Conflict-Aware Learning) — He, Tang, Zou, Zhang, 2023, ACM MM | DOI 10.1145/3581783.3612651 | Rectifies cross-modal feature conflict before selective fusion. | "Conflict" framing is a conceptual neighbour of corrupted-modality harm. | should-cite |
| 10 | RGBT architecture / quality fusion | Confidence-Aware Fusion via Dempster–Shafer (CMPD) — Li, Zhang, Hu, Fu, Zhu, 2023, IEEE TMM | (IEEE TMM 25:3420–3431) | Per-modality confidence subnetworks combined evidentially for pedestrian detection. | In-domain precedent for quality/confidence-weighted RGB-T fusion. | must-cite |
| 11 | RGBT architecture | CDDFuse — Zhao et al., 2023, CVPR | [link](https://arxiv.org/abs/2211.14461) | Correlation-driven dual-branch decomposition fusion, incl. downstream detection. | Task-coupled fusion line (fusion-for-detection). | should-cite |
| 12 | RGBT architecture | MetaFusion — Zhao et al., 2023, CVPR | DOI 10.1109/CVPR52729.2023.01341 | Detection-guided meta-feature embedding mutually promoting fusion and detection. | Supports the manuscript's task-constrained motivation. | should-cite |
| 13 | RGBT architecture | GM-DETR — Xiao et al., 2024, CVPR Workshops | (CVPRW 2024, pp.5541–5549) | Lightweight DETR-style RGB-T detector. | Additional DETR-line data point on FLIR + LLVIP. | optional |
| 14 | RGBT architecture | UniRGB-IR — Yuan et al., 2025, ACM MM | [link](https://arxiv.org/abs/2404.17360) | Adapter injection of RGB-IR fusion into a frozen ViT foundation model. | Foundation-model line; FLIR mAP 44.1 / LLVIP 63.2. | optional |
| 15 | Survey/benchmark | Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption — Liu et al., 2025, IEEE TPAMI | https://arxiv.org/abs/2501.10761 (DOI 10.1109/TPAMI.2024.3521416) | Comprehensive IVIF survey organized around task adaptation. | Authoritative section anchor from the TarDAL/M3FD group. | should-cite |
| 16 | Survey/benchmark | MSOD-Bench: Optimizing Multispectral Object Detection — Zhou et al., 2024, arXiv | [link](https://arxiv.org/abs/2411.18288) | Standardized re-implementation/benchmark of 20+ RGB-T detectors. | Fair-comparison framing; guards against cherry-picked baseline numbers. | should-cite |
| 17 | Robust fusion | Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance — Tian, Yang, Zhu, Wang, He, 2025, Pattern Recognition Letters | [link](https://arxiv.org/abs/2505.22154) | Quality-mask interaction + pseudo-degradation + EMA base/auxiliary consistency for imbalanced RGB-T. | **Closest prior work** — see §(b). KAIST LAMR + FLIR mAP; Gaussian-noise and contrast-degradation tests. | must-cite |
| 18 | Robust fusion | Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF) — Zhang et al., 2023, ICML | [link](https://arxiv.org/abs/2306.02050) | Energy-based uncertainty drives dynamic decision-level fusion weights, with guarantees. | Reference quality-aware fusion method; classification-only contrast to feature correction. | must-cite |
| 19 | Robust fusion | Multimodal Fusion on Low-quality Data: A Comprehensive Survey — Zhang et al., 2024, arXiv | [link](https://arxiv.org/abs/2404.18947) | Taxonomy separating noisy, incomplete, imbalanced, quality-varying multimodal data. | Cleanest citation legitimizing the corrupted ≠ missing distinction. | must-cite |
| 20 | Robust fusion | Trusted Multi-View Classification (TMC) — Han, Zhang, Fu, Zhou, 2021, ICLR | [link](https://arxiv.org/abs/2102.02051) | Evidential per-view quality assessment with Dempster–Shafer fusion. | Foundational trusted/quality-aware fusion citation. | should-cite |
| 21 | Robust fusion | MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion — Park, Kim, Kim, Choi, 2025, CVPR | [link](https://arxiv.org/abs/2503.19776) | Per-query routing among camera/LiDAR/fused experts by local feature quality. | Strongest analogue of region-dependent takeover (routing, not correction; 3D driving). | must-cite |
| 22 | Robust fusion | MEFormer — Cha et al., 2024, arXiv | [link](https://arxiv.org/abs/2407.19156) | Defines and mitigates "negative fusion" from defective modalities. | Names the manuscript's core phenomenon; cite the term. | should-cite |
| 23 | Robust fusion | WiSE-OD — Medeiros et al., 2026, WACV | [link](https://arxiv.org/abs/2507.18925) | Weight-space ensembling for OOD RGB-T detection; introduces LLVIP-C / FLIR-C. | Corruption-benchmark protocol (AP50, mPC) a reviewer may demand alignment with. | should-cite |
| 24 | Robust fusion | Benchmarking Robustness of 3D Object Detection to Common Corruptions — Dong et al., 2023, CVPR | [link](https://arxiv.org/abs/2303.11040) | 27-corruption benchmark; fusion models more robust, motion corruptions worst. | Corruption-protocol precedent for the manuscript's degradation suite. | should-cite |
| 25 | Robust fusion | MultiCorrupt — Beemelmanns, Zhang, Eckstein, 2024, IEEE IV | [link](https://arxiv.org/abs/2402.11677) | 10 LiDAR-camera corruptions × 3 severities with Resistance Ability metric. | Severity-graded corruption evaluation model. | optional |
| 26 | Robust fusion | DynMM — Xue & Marculescu, 2023, CVPR Workshops | [link](https://arxiv.org/abs/2204.00102) | On-the-fly gating over modality and fusion-level computation paths. | Dynamic-fusion precedent (efficiency-motivated). | optional |
| 27 | Robust fusion | SB-BEVFusion — Essl et al., 2026, arXiv (ICIP 2026) | [link](https://arxiv.org/abs/2605.11799) | BEV fusion explicitly treating corrupted vs missing sensors as distinct cases. | Verbatim corrupted-vs-missing distinction; very recent, camera-LiDAR. | optional |
| 28 | Imbalance | OGM-GE — Peng, Wei, Deng, Wang, Hu, 2022, CVPR (Oral) | [link](https://arxiv.org/abs/2203.15332) | On-the-fly gradient modulation by modality contribution discrepancy. | Standard balancing citation next to the existing competition papers. | must-cite |
| 29 | Imbalance | PMR: Prototypical Modal Rebalance — Fan, Xu, Wang, Wang, Guo, 2023, CVPR | DOI 10.1109/CVPR52729.2023.01918 (arXiv:2211.07089) | Prototypes accelerate the slow-learning modality; entropy regularizer vs dominant modality. | Balancing line representative. | should-cite |
| 30 | Imbalance | ReconBoost — Hua, Xu, Bao, Yang, Huang, 2024, ICML | [link](https://proceedings.mlr.press/v235/hua24a.html) | Modality-alternating boosting with KL reconcilement vs competition. | Most recent reconcilement-framed balancing method. | should-cite |
| 31 | Imbalance | MMPareto — Wei & Hu, 2024, ICML | [link](https://arxiv.org/abs/2405.17730) | Pareto-integrated gradients resolving multimodal/unimodal gradient conflict. | Gradient-conflict framing. | optional |
| 32 | Missing modality | SMIL — Ma et al., 2021, AAAI | https://arxiv.org/abs/2103.05677 (DOI 10.1609/aaai.v35i3.16330) | Bayesian meta-learning for severely (≤90%) missing modalities. | Canonical missing-modality method citation. | should-cite |
| 33 | Missing modality | ShaSpec — Wang et al., 2023, CVPR | [link](https://arxiv.org/abs/2307.14126) | Shared-specific features + residual fusion for missing modality at train/test. | Representation-side missing-modality approach. | should-cite |
| 34 | Missing modality (detection) | ProbEn — Chen, Shi, Ye, Mertz, Ramanan, Kong, 2022, ECCV | [link](https://arxiv.org/abs/2104.02904) | Probabilistic late ensembling; marginalization handles missing modalities natively. | Only verified detection-native missing-modality method; KAIST + FLIR. | must-cite |
| 35 | Missing modality | Multimodal Learning with Missing Modalities: A Survey — Wu, Wang, Chen, 2024, arXiv (TMLR) | [link](https://arxiv.org/abs/2409.07825) | Survey of imputation/representation/distillation approaches to missing modalities. | Section anchor for Q3. | should-cite |
| 36 | Missing modality / distillation | MM-CKD — Sang, Funakoshi, Okumura, 2024, arXiv | [link](https://arxiv.org/abs/2410.08692) | Cross-modal knowledge distillation robust to missing modality (sentiment). | Only distillation-for-missing citation found; non-vision. | optional |
| 37 | Test-time adaptation | Tent — Wang, Shelhamer, Liu, Olshausen, Darrell, 2021, ICLR | [link](https://arxiv.org/abs/2006.10726) | Test-time entropy minimization over norm affine parameters. | Canonical "adapt at test time" contrast (parameter-level, unsupervised). | should-cite |
| 38 | Test-time adaptation | MEMO — Zhang, Levine, Finn, 2022, NeurIPS | [link](https://arxiv.org/abs/2110.09506) | Per-test-point adaptation via marginal entropy over augmentations. | Single-point test-time intervention precedent. | optional |
| 39 | Test-time intervention | Inference-Time Intervention (ITI) — Li, Patel, Viégas, Pfister, Wattenberg, 2023, NeurIPS Spotlight | [link](https://arxiv.org/abs/2306.03341) | Shifts selected attention-head activations along probed directions at inference. | Terminological namesake of "intervention"; LLM-only, one clarifying sentence. | optional |
| 40 | Amortized optimization | OptNet — Amos & Kolter, 2017, ICML | [link](https://arxiv.org/abs/1703.00443) | Differentiable QP layers via implicit KKT differentiation. | Foundational only; redundant given existing Amos/CF-OPT citations. | optional |

## 审稿人最可能要求对比的基线（8 个）

| Baseline | Why demanded | Dataset / metric reported |
|---|---|---|
| Tian et al. 2025 (robust RGB-T detector) | 与本文问题陈述最接近：模态退化/不平衡下的 RGB-T 检测 | KAIST LAMR（含 σ=20 高斯噪声与对比度退化）；FLIR mAP |
| YOLOv11-RGBT (incl. MCF) | 同一 YOLO11 骨干 + P3 中层融合，同一数据集 | LLVIP + FLIR，mAP/mAP50；MCF 使 FLIR mAP 提升 3.41–5.65%（最高 47.61%） |
| DAMSDet | DETR 线最强 RGB-T 检测器，数据集三元组完全重合 | M3FD / FLIR-aligned / LLVIP，FLIR mAP 49.3，LLVIP mAP 69.6（干净数据） |
| Fusion-Mamba (or WaveMamba) | 2025 年 SOTA 声称的融合线 | M3FD mAP 61.9（二手对比表），FLIR-Aligned，DroneVehicle |
| ICAFusion（稿件已引） | 稿件自有参考文献里的既有锚点，审稿人预期其干净数据成绩 | LLVIP mAP50 98.4 / mAP 64.5；M3FD mAP50 90.8 / mAP 60.9（二手来源） |
| CFT | 老牌 Transformer 融合基线，FLIR/LLVIP 权重公开，易在退化套件下复跑 | FLIR + LLVIP，mAP50/mAP（LLVIP mAP 63.6，二手对比表） |
| ProbEn | 缺失模态分支唯一检测原生的对比方法 | KAIST aligned + FLIR unaligned，标准检测 AP，含缺失模态设置 |
| WiSE-OD protocol (LLVIP-C / FLIR-C) | 不是模型而是协议：本文数据集的退化版本基准 | LLVIP-C / FLIR-C，AP50 与 mPC；另有真实 OOD M3FD 雨/雾/夜划分 |

## 新颖性威胁（显式标注）

1. **Tian et al. 2025 — 高威胁。** 同任务、同叙事（退化模态拖累 RGB-T 检测，用质量感知机制让健康模态主导）。区别：训练时伪退化 + EMA 一致性 vs 推理时学习的局部修正；窄对比度/偏置退化族 vs 未知混合退化；融合内质量重加权 vs 最小幅度、任务约束的特征修正；未区分 corrupted 与 missing，也没有修正目标消融。
2. **YOLOv11-RGBT (2025) — 中威胁（定位而非方法）。** 先占了 “YOLO11 中层融合做 RGBT” 的说法，其 MCF 是训练侧再平衡；本文新颖性应只落在干预算子与接管理论分析上。
3. **MoME (CVPR 2025) — 中威胁。** 按局部特征质量逐 query 选专家，与 “区域依赖接管” 概念相邻；区别是专家选择 vs 融合特征的连续局部修正，LiDAR-相机 3D vs RGBT 2D。
4. **MEFormer (2024) — 低-中威胁。** 已命名本文的现象 “negative fusion”，应引用并沿用该术语并注明出处。
5. **QMF + CMPD — 低威胁（单个看）。** 两者共同确立了质量/置信度加权融合是成熟方向；本文应定位为 *correction*（改变受损特征）而非 *weighting*（降权）。

调研结论：未发现同时具备「推理时应用 + 局部（区域/尺度依赖）特征修正 + 最小幅度约束 + 任务惩罚训练目标」四点、且用于 RGBT 检测的工作。

## Could not verify / 使用前注意

- 稿件所引 “TARDet” 查无此文，核实到的工作是 **TarDAL**（CVPR 2022, arXiv:2203.16220），同时也是 M3FD 数据集论文，引用前请对照 .bib 核对。
- CMDistill (IEEE JSTARS 2024) 仅在他文参考文献中出现，未能独立核实，已排除出本表。
- C2Former 的 DOI 取自引用它的论文参考文献表，其 arXiv 记录本身已核实。
- Fusion-Mamba 的部分数字为二手对比表来源（如 M3FD mAP 61.9 来自 IRDFusion 对比表），正式引用前请回原文核对。
- MEFormer、MSOD-Bench 仅核实 arXiv 记录，未核实正式发表 venue。
