# owesome-RGBT-ObjectDetection

RGBT Object Detection Literature Library — RGBT 目标检测文献库

一个专门存放 RGBT（可见光–热红外）目标检测文献的仓库。首批收录 2026-10-25 调研核实的 **40 篇**文献，按类别与引用优先级整理，服务于稿件 *“Task-Constrained Local Intervention for RGB–Thermal Modality Takeover”* 的 Related Work 修订。

## 文件说明

- [`bibliography.md`](bibliography.md) — 完整文献表（分类、链接、一句话贡献、与稿件的关系、优先级），另附审稿人最可能要求的 8 个基线、新颖性威胁清单与未核实事项
- [`papers.csv`](papers.csv) — 同一批 40 篇的结构化表格，可按类别/优先级筛选
- [`references.bib`](references.bib) — 对应的 BibTeX 条目，可直接并入稿件的 .bib（正式投稿前请回原文核对 venue 与页码）

## 收录概况

- 总数：40 篇（must-cite 12 · should-cite 18 · optional 10）
- RGBT architecture：13 篇
- RGBT architecture / quality fusion：1 篇
- Survey/benchmark：2 篇
- Robust fusion：11 篇
- Imbalance：4 篇
- Missing modality：3 篇
- Missing modality (detection)：1 篇
- Missing modality / distillation：1 篇
- Test-time adaptation：2 篇
- Test-time intervention：1 篇
- Amortized optimization：1 篇

## 必引文献速览（must-cite）

- **Cross-Modality Fusion Transformer (CFT)** — Fang, Han, Wang, 2021, arXiv · https://arxiv.org/abs/2111.00273
- **C2Former: Calibrated and Complementary Transformer** — Yuan & Wei, 2024, IEEE TGRS · https://arxiv.org/abs/2306.16175
- **DAMSDet** — Guo, Gao, Liu, Meng, Gao, 2024, ECCV · https://eccv.ecva.net/virtual/2024/poster/801
- **YOLOv11-RGBT** — Wan et al., 2025, arXiv · https://arxiv.org/abs/2506.14696
- **Fusion-Mamba** — Dong et al., 2025, IEEE TMM · https://doi.org/10.1109/TMM.2025.3599020
- **Confidence-Aware Fusion via Dempster–Shafer (CMPD)** — Li, Zhang, Hu, Fu, Zhu, 2023, IEEE TMM · (IEEE TMM 25:3420–3431)
- **Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance** — Tian, Yang, Zhu, Wang, He, 2025, Pattern Recognition Letters · https://arxiv.org/abs/2505.22154
- **Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF)** — Zhang et al., 2023, ICML · https://arxiv.org/abs/2306.02050
- **Multimodal Fusion on Low-quality Data: A Comprehensive Survey** — Zhang et al., 2024, arXiv · https://arxiv.org/abs/2404.18947
- **MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion** — Park, Kim, Kim, Choi, 2025, CVPR · https://arxiv.org/abs/2503.19776
- **OGM-GE** — Peng, Wei, Deng, Wang, Hu, 2022, CVPR (Oral) · https://arxiv.org/abs/2203.15332
- **ProbEn** — Chen, Shi, Ye, Mertz, Ramanan, Kong, 2022, ECCV · https://arxiv.org/abs/2104.02904

## 两个最重要的结论

1. **最接近的先行工作是 Tian et al. 2025**（*Pattern Recognition Letters*，《Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance》）：质量掩码 + 训练时伪退化 + EMA 一致性。必须引用并专门对比——它是训练时加固，本文是推理时、最小幅度的任务约束局部修正，且明确区分 corrupted 与 missing。
2. **YOLOv11-RGBT (arXiv:2506.14696) 是直接的架构前身**：同一 YOLO11 骨干与 P3 中层融合，LLVIP + FLIR，审稿人很可能追问为何未引。

> 注意：稿件所引 “TARDet” 未能核实，对应的核实工作是 **TarDAL**（CVPR 2022，也是 M3FD 论文），详见 bibliography.md 末尾的未核实清单。部分二手数字已在表中标注，正式引用前请回原文核对。
