<!-- Generated from papers.csv by tools/generate.py — do not edit by hand. -->
# awesome-RGBT-ObjectDetection

A curated collection of **RGBT object detection** resources — papers, datasets, and code.

RGBT (also written RGB-T, RGB-Thermal, multispectral, or visible–infrared) object detection fuses a visible-light image with a thermal (LWIR) image to detect objects under conditions where either modality alone fails — darkness, glare, smoke, or adverse weather.

**Scope.** Object detection only: general, pedestrian, vehicle, and aerial/UAV detection with paired visible–thermal imagery. Segmentation, salient object detection, crowd counting, and tracking are out of scope (see Related Lists).

**How this list is organised — one axis only.** Papers in the main list are RGBT detection papers, classified by *technical route*: the level at which the two modalities are fused (pixel → feature → decision), with architecture families as subsections of feature-level fusion. Challenges such as misalignment, degradation, or missing modalities are **tags** (shown in italics, and a column in papers.csv), not sections — so every paper has exactly one home. Work that is not RGBT detection but transfers to it (general multimodal fusion, imbalance/missing-modality learning, test-time methods, driving robustness) lives in a separate Appendix, clearly marked, instead of being mixed into the main list.

**Single source of truth.** The paper list lives in [papers.csv](papers.csv); README.md, bibliography.md and references.bib are generated from it by [tools/generate.py](tools/generate.py) and checked by tools/validate.py. Edit the CSV, never the generated files.

## News

- [2026-10-26] Tooling: papers.csv is now the single source of truth — README, bibliography and BibTeX are generated and validated automatically. Tag vocabulary consolidated.
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
|[DRTV30K](https://github.com/Vehicle-AHU/DRTV30K)|2026|RGB, LWIR|30K|9|Partially|

> Dataset statistics below are compiled from the datasets' official pages and the public list [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) (accessed 2026-10-25); always confirm numbers on the official page before citing them.

## Surveys & Benchmarks

1. Physical Adversarial Clothing Evades Visible-Thermal Detectors via Non-Overlapping RGB-T Pattern, CVPR 2026, Zhu, Zeng, Hu, Zhu, Hu [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Physical_Adversarial_Clothing_Evades_Visible-Thermal_Detectors_via_Non-Overlapping_RGB-T_Pattern_CVPR_2026_paper.pdf)] [[Code](https://github.com/zxp555/RGBT-Clothing)] — *corruption*
2. UAV-CB: A Complex-Background RGB-T Dataset and Local Frequency Bridge Network for UAV Detection, CVPR 2026, Huang et al. [[Paper](https://arxiv.org/abs/2603.17492)] — *benchmark; aerial; frequency-domain*
3. WiSE-OD, WACV 2026, Medeiros et al. [[Paper](https://arxiv.org/abs/2507.18925)] [[Code](https://github.com/heitorrapela/wiseod)] — *degraded-modality; benchmark*
4. Fusion Meets Diverse Conditions: A High-diversity Benchmark and Baseline for UAV-based Multimodal Object Detection with Condition Cues, ICCV 2025, Chen et al. [[Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Fusion_Meets_Diverse_Conditions_A_High-diversity_Benchmark_and_Baseline_for_ICCV_2025_paper.pdf)] — *benchmark; aerial; degraded-modality*
5. Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption, IEEE TPAMI 2025, Liu et al. [[Paper](https://arxiv.org/abs/2501.10761)] — *survey*
6. Visible-Thermal Tiny Object Detection: A Benchmark Dataset and Baselines (RGBT-Tiny), IEEE TPAMI 2025, Ying et al. [[Paper](https://arxiv.org/abs/2406.14482)] [[Code](https://github.com/XinyiYing/RGBT-Tiny)] — *aerial*
7. MSOD-Bench: Optimizing Multispectral Object Detection, arXiv 2024, Zhou et al. [[Paper](https://arxiv.org/abs/2411.18288)] — *benchmark*
8. Misaligned Visible-Thermal Object Detection: A Drone-based Benchmark and Baseline (DVTOD), IEEE TIV 2024, Song et al. [[Paper](https://doi.org/10.1109/TIV.2024.3398429)] [[Code](https://github.com/VDT-2048/DVTOD)] — *benchmark; aerial; alignment*
9. When Pedestrian Detection Meets Multi-Modal Learning: Generalist Model and Benchmark Dataset (MMPedestron), ECCV 2024, Zhang et al. [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06487.pdf)] [[Code](https://github.com/BubblyYi/MMPedestron)] — *benchmark; pedestrian; foundation-model*

## Pixel-Level Fusion for Detection

1. DDFD: Diffusion-Based Denoising Fusion for Object Detection in Infrared-Visible Images, ACM MM 2025, Dang et al. [[Paper](https://dl.acm.org/doi/10.1145/3746027.3755183)] — *image-fusion; task-coupled; degraded-modality*
2. E2E-MFD: Towards End-to-End Synchronous Multimodal Fusion Detection, NeurIPS 2024, Zhang et al. [[Paper](https://arxiv.org/abs/2403.09323)] [[Code](https://github.com/icey-zhang/EfficientMFD)] — *image-fusion; task-coupled; aerial*
3. CDDFuse, CVPR 2023, Zhao et al. [[Paper](https://arxiv.org/abs/2211.14461)] — *image-fusion; task-coupled*
4. MetaFusion, CVPR 2023, Zhao et al. [[Paper](https://doi.org/10.1109/CVPR52729.2023.01341)] — *image-fusion; task-coupled*
5. SuperYOLO: Super Resolution Assisted Object Detection in Multimodal Remote Sensing Imagery, IEEE TGRS 2023, Zhang et al. [[Paper](https://doi.org/10.1109/TGRS.2023.3258666)] [[Code](https://github.com/icey-zhang/SuperYOLO)] — *image-fusion; aerial; yolo; efficiency*
6. DetFusion: A Detection-driven Infrared and Visible Image Fusion Network, ACM MM 2022, Sun et al. [[Paper](https://dl.acm.org/doi/pdf/10.1145/3503161.3547902)] [[Code](https://github.com/SunYM2020/DetFusion)] — *image-fusion; task-coupled*
7. TarDAL: Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection, CVPR 2022, Liu et al. [[Paper](https://arxiv.org/abs/2203.16220)] [[Code](https://github.com/JinyuanLiu-CV/TarDAL)] — *image-fusion; task-coupled*

## Feature-Level Fusion

### Attention, Transformers & Foundation Models

1. DyFCLT: Dynamic Frequency-Decoupled Cross-Modal Learning Transformer for Multimodal Tiny Object Detection, CVPR 2026, Li, Dai, Li, Yao, Jiang, Zheng [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_DyFCLT_Dynamic_Frequency-Decoupled_Cross-Modal_Learning_Transformer_for_Multimodal_Tiny_Object_CVPR_2026_paper.pdf)] — *transformer; frequency-domain; aerial*
2. Modality-Decoupled RGB-Thermal Object Detector via Query Fusion, arXiv 2026, Tian et al. [[Paper](https://arxiv.org/abs/2601.08458)] — *detr; transformer; dual-stream*
3. Thermal-Det: Language-Guided Cross-Modal Distillation for Open-Vocabulary Thermal Object Detection, CVPR 2026, Ranasinghe et al. [[Paper](https://arxiv.org/abs/2605.10130)] — *foundation-model; distillation*
4. M-SpecGene: Generalized Foundation Model for RGBT Multispectral Vision, ICCV 2025, Zhou et al. [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_M-SpecGene_Generalized_Foundation_Model_for_RGBT_Multispectral_Vision_ICCV_2025_paper.html)] [[Code](https://github.com/CalayZhou/M-SpecGene)] — *foundation-model*
5. SAM-Guided Semantic Knowledge Fusion for Visible-Infrared Object Detection, ACM MM 2025, Li et al. [[Paper](https://dl.acm.org/doi/10.1145/3746027.3755718)] [[Code](https://github.com/liting1018/SemFusion)] — *foundation-model*
6. Towards a Generalizable Fusion Architecture for Multimodal Object Detection, ICCV Workshops 2025, Berjawi, Dupas, Cérin [[Paper](https://arxiv.org/abs/2510.17078)] [[Code](https://github.com/jadberjawi/FMCAF)] — *cross-attention; frequency-domain*
7. UniRGB-IR, ACM MM 2025, Yuan et al. [[Paper](https://arxiv.org/abs/2404.17360)] — *foundation-model; adapter*
8. C2Former: Calibrated and Complementary Transformer, IEEE TGRS 2024, Yuan & Wei [[Paper](https://arxiv.org/abs/2306.16175)] [[Code](https://github.com/yuanmaoxun/C2Former)] — *alignment; cross-attention; transformer*
9. CF-Deformable DETR: An End-to-End Alignment-Free Model for Weakly Aligned Visible-Infrared Object Detection, IJCAI 2024, Fu et al. [[Paper](https://www.ijcai.org/proceedings/2024/0084.pdf)] [[Code](https://github.com/116508/CF-Deformable-DETR)] — *detr; alignment; transformer*
10. DAMSDet, ECCV 2024, Guo, Gao, Liu, Meng, Gao [[Paper](https://eccv.ecva.net/virtual/2024/poster/801)] [[Code](https://github.com/gjj45/DAMSDet)] — *transformer; detr*
11. GM-DETR, CVPR Workshops 2024, Xiao et al. (CVPRW 2024, pp.5541–5549) — *transformer; detr; efficiency*
12. ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection, Pattern Recognition 2024, Shen et al. [[Paper](https://ieeexplore.ieee.org/abstract/document/10225383)] [[Code](https://github.com/chanchanchan97/ICAFusion)] — *cross-attention*
13. Improving RGB-Infrared Object Detection with Cascade Alignment-Guided Transformer (CAGT), Information Fusion 2024, Yuan, Shi, Wang, Wang, Wei [[Paper](https://doi.org/10.1016/j.inffus.2024.102246)] — *alignment; aerial; transformer; cross-attention*
14. Cross-Modality Fusion Transformer (CFT), arXiv 2021, Fang, Han, Wang [[Paper](https://arxiv.org/abs/2111.00273)] — *cross-attention; transformer*
15. Guided Attentive Feature Fusion for Multispectral Pedestrian Detection (GAFF), WACV 2021, Zhang, Fromont, Lefèvre, Avignon [[Paper](https://openaccess.thecvf.com/content/WACV2021/html/Zhang_Guided_Attentive_Feature_Fusion_for_Multispectral_Pedestrian_Detection_WACV_2021_paper.html)] — *pedestrian; cross-attention; efficiency*
16. Cross-Modality Interactive Attention Network for Multispectral Pedestrian Detection (CIAN), Information Fusion 2019, Zhang et al. [[Paper](https://doi.org/10.1016/j.inffus.2018.09.015)] — *pedestrian; cross-attention*

### Dual-Stream CNN & YOLO-Based Detectors

1. Bridging Severe Cross-Modal Misalignment: End-to-End Visible-Infrared Object Detection via Explicit Feature-Domain Affine Registration, arXiv 2026, Ming et al. [[Paper](https://arxiv.org/abs/2608.10680)] — *alignment; aerial*
2. Efficient RGB-T Object Detection via Sparse Cross-Modality Fusion, arXiv 2026, Tian et al. [[Paper](https://arxiv.org/abs/2606.30215)] — *efficiency*
3. IRDFusion: Iterative Relation-map Difference Guided Feature Fusion for Multispectral Object Detection, Pattern Recognition 2026, Shen et al. [[Paper](https://doi.org/10.1016/j.patcog.2026.113189)] — *dual-stream*
4. LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection, arXiv 2026, Hou et al. [[Paper](https://arxiv.org/abs/2605.20667)] — *alignment; expert-routing; aerial; yolo*
5. TFDet: Target-Aware Fusion for RGB-T Pedestrian Detection, IEEE TNNLS 2025, Zhang et al. [[Paper](https://arxiv.org/abs/2305.16580)] — *pedestrian; task-coupled*
6. Weakly Aligned Feature Fusion for Multimodal Object Detection, IEEE TNNLS 2025, Zhang et al. [[Paper](https://doi.org/10.1109/TNNLS.2021.3105143)] — *alignment; dual-stream*
7. YOLOv11-RGBT, arXiv 2025, Wan et al. [[Paper](https://arxiv.org/abs/2506.14696)] [[Code](https://github.com/wandahangFY/YOLOv11-RGBT)] — *yolo; efficiency*
8. DEYOLO, ICPR 2024, Chen et al. [[Paper](https://arxiv.org/abs/2412.04931)] — *yolo; dual-stream*
9. Weakly Misalignment-free Adaptive Feature Alignment for UAVs-based Multimodal Object Detection (OAFA), CVPR 2024, Chen et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_Weakly_Misalignment-free_Adaptive_Feature_Alignment_for_UAVs-based_Multimodal_Object_Detection_CVPR_2024_paper.pdf)] — *alignment; aerial*
10. LRAF-Net, IEEE TNNLS 2023, Fu et al. [[Paper](https://doi.org/10.1109/TNNLS.2023.3266452)] — *dual-stream; modality-imbalance*
11. BAANet: Learning Bi-Directional Adaptive Attention Gates for Multispectral Pedestrian Detection, ICRA 2022, Yang, Qian, Zhu, Wang, Yang [[Paper](https://arxiv.org/abs/2112.02277)] — *pedestrian; quality-aware*
12. Learning a Dynamic Cross-Modal Network for Multispectral Pedestrian Detection (DCMNet), ACM MM 2022, Xie et al. [[Paper](https://doi.org/10.1145/3503161.3547895)] — *pedestrian; dynamic-fusion*
13. Translation, Scale and Rotation: Cross-Modal Alignment Meets RGB-Infrared Vehicle Detection (TSFADet), ECCV 2022, Yuan, Wang, Wei [[Paper](https://arxiv.org/abs/2209.13801)] — *alignment; aerial*
14. MLPD: Multi-Label Pedestrian Detector in Multispectral Domain, IEEE RA-L 2021, Kim et al. [[Paper](https://doi.org/10.1109/LRA.2021.3099870)] — *pedestrian; alignment*
15. Weakly Aligned Cross-Modal Learning for Multispectral Pedestrian Detection (AR-CNN), ICCV 2019, Zhang et al. [[Paper](https://arxiv.org/abs/1901.02645)] [[Code](https://github.com/luzhang16/AR-CNN)] — *alignment; pedestrian*
16. Multispectral Pedestrian Detection via Simultaneous Detection and Segmentation (MSDS-RCNN), BMVC 2018, Li, Song, Tong, Tang [[Paper](https://arxiv.org/abs/1808.04818)] — *pedestrian; dual-stream*
17. Multispectral Deep Neural Networks for Pedestrian Detection (Halfway Fusion), BMVC 2016, Liu, Zhang, Wang, Metaxas [[Paper](https://arxiv.org/abs/1611.02644)] — *pedestrian; dual-stream*

### State-Space Models (Mamba)

1. Multispectral State-Space Feature Fusion: Bridging Shared and Cross-Parametric Interactions for Object Detection, Information Fusion 2026, Shen et al. [[Paper](https://doi.org/10.1016/j.inffus.2025.103895)] — *mamba*
2. Contextually-Guided State Space Fusion for Misaligned Multi-Spectral Object Detection (CSSFDet), ACM MM 2025, Jin et al. [[Paper](https://dl.acm.org/doi/10.1145/3746027.3754550)] — *mamba; alignment; aerial*
3. Fusion-Mamba, IEEE TMM 2025, Dong et al. [[Paper](https://doi.org/10.1109/TMM.2025.3599020)] — *mamba*
4. Pseudo Visible Feature Fine-Grained Fusion for Thermal Object Detection (PFGF), CVPR 2025, Li et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Pseudo_Visible_Feature_Fine-Grained_Fusion_for_Thermal_Object_Detection_CVPR_2025_paper.pdf)] [[Code](https://github.com/liting1018/PFGF)] — *mamba; missing-modality*
5. WaveMamba, ICCV 2025, Zhu et al. [[Paper](https://arxiv.org/abs/2507.18173)] [[Code](https://github.com/EhanDong/WaveMamba)] — *mamba; frequency-domain*
6. Mask-Guided Mamba Fusion for Drone-based Visible-Infrared Vehicle Detection, IEEE TGRS 2024, Wang et al. [[Paper](https://doi.org/10.1109/TGRS.2024.3452550)] — *mamba; aerial*

### Quality- & Conflict-Aware Fusion

1. Bridging Multimodal Fusion and Expert Routing via Spectral Reliability Descriptors for Robust Object Detection, arXiv 2026, Wu [[Paper](https://arxiv.org/abs/2606.01173)] — *quality-aware; expert-routing; degraded-modality; aerial*
2. Distribution-Aligned Multimodal Fusion for Robust Object Detection, CVPR 2026, Hao et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Hao_Distribution-Aligned_Multimodal_Fusion_for_Robust_Object_Detection_CVPR_2026_paper.pdf)] — *degraded-modality; quality-aware*
3. InfraNet: Quality-Aware RGB Guidance for Infrared Object Detection, ECCV 2026, Feng et al. [[Paper](https://eccv.ecva.net/virtual/2026/poster/3873)] — *quality-aware; missing-modality*
4. EI²Det: Edge-Guided Illumination-Aware Interactive Learning for Visible-Infrared Object Detection, IEEE TCSVT 2025, Hu et al. [[Paper](https://doi.org/10.1109/TCSVT.2025.3539625)] [[Code](https://github.com/hukefy/EI2Det)] — *quality-aware*
5. Efficient Multispectral Object Detection with Attentive Feature Aggregation Leveraging Zero-Shot Implicit Illumination Guidance, Information Fusion 2025, Xiong et al. [[Paper](https://doi.org/10.1016/j.inffus.2025.102939)] — *efficiency; quality-aware*
6. Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance, Pattern Recognition Letters 2025, Tian, Yang, Zhu, Wang, He [[Paper](https://arxiv.org/abs/2505.22154)] — *degraded-modality; quality-aware; modality-imbalance*
7. Mixed Patch Visible-Infrared Modality Agnostic Object Detection (MiPa), WACV 2025, Medeiros et al. [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Medeiros_Mixed_Patch_Visible-Infrared_Modality_Agnostic_Object_Detection_WACV_2025_paper.html)] [[Code](https://github.com/heitorrapela/MiPa)] — *missing-modality; modality-imbalance; transformer*
8. Removal and Selection: Improving RGB-Infrared Object Detection via Coarse-to-Fine Fusion, IEEE TITS 2025, Zhao, Yuan, Jiang, Wang, Wei [[Paper](https://arxiv.org/abs/2401.10731)] — *conflict-aware; quality-aware*
9. Representation Space Constrained Learning with Modality Decoupling for Multimodal Object Detection, arXiv 2025, Shao, Shi [[Paper](https://arxiv.org/abs/2511.15433)] [[Code](https://github.com/yikangshao/RSC-MD)] — *negative-fusion; modality-imbalance*
10. Rethinking Multi-modal Object Detection from the Perspective of Mono-Modality Feature Learning (M2D-LIF), ICCV 2025, Zhao et al. [[Paper](https://arxiv.org/abs/2503.11780)] [[Code](https://github.com/Zhao-Tian-yi/M2D-LIF)] — *modality-imbalance; distillation*
11. Causal Mode Multiplexer: A Novel Framework for Unbiased Multispectral Pedestrian Detection, CVPR 2024, Kim et al. [[Paper](https://arxiv.org/abs/2403.01300)] [[Code](https://github.com/ssbin0914/Causal-Mode-Multiplexer)] — *pedestrian; modality-imbalance*
12. CALNet (Cross-Modal Conflict-Aware Learning), ACM MM 2023, He, Tang, Zou, Zhang [[Paper](https://doi.org/10.1145/3581783.3612651)] — *conflict-aware; aerial*
13. Drone-Based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning (UA-CMDet), IEEE TCSVT 2022, Sun, Cao, Zhu, Hu [[Paper](https://doi.org/10.1109/TCSVT.2022.3168279)] [[Code](https://github.com/VisDrone/DroneVehicle)] — *aerial; quality-aware*
14. Improving Multispectral Pedestrian Detection by Addressing Modality Imbalance Problems (MBNet), ECCV 2020, Zhou, Chen, Cao [[Paper](https://arxiv.org/abs/2008.03043)] [[Code](https://github.com/CalayZhou/MBNet)] — *modality-imbalance; pedestrian; alignment*
15. Fusion of Multispectral Data Through Illumination-Aware Deep Neural Networks for Pedestrian Detection (IATDNN), Information Fusion 2019, Guan et al. [[Paper](https://arxiv.org/abs/1802.09972)] — *pedestrian; quality-aware*

## Decision-Level & Evidential Fusion

1. Multiscale Cross-modal Homogeneity Enhancement and Confidence-aware Fusion for Multispectral Pedestrian Detection, IEEE TMM 2024, Li et al. [[Paper](https://doi.org/10.1109/TMM.2023.3272471)] [[Code](https://github.com/RimXidian/MCHE-CF-for-Multispectral-Pedestrian-Detection)] — *decision-level; pedestrian*
2. Stabilizing Multispectral Pedestrian Detection with Evidential Hybrid Fusion, IEEE TCSVT 2024, Li et al. [[Paper](https://doi.org/10.1109/TCSVT.2023.3306870)] — *evidential; pedestrian*
3. Confidence-Aware Fusion via Dempster–Shafer (CMPD), IEEE TMM 2023, Li, Zhang, Hu, Fu, Zhu (IEEE TMM 25:3420–3431) — *evidential; decision-level; pedestrian*
4. ProbEn, ECCV 2022, Chen, Shi, Ye, Mertz, Ramanan, Kong [[Paper](https://arxiv.org/abs/2104.02904)] — *missing-modality; decision-level; ensemble; pedestrian*
5. Illumination-Aware Faster R-CNN for Robust Multispectral Pedestrian Detection, Pattern Recognition 2019, Li, Song, Tong, Tang [[Paper](https://doi.org/10.1016/j.patcog.2018.08.005)] — *pedestrian; quality-aware*

## Appendix — Related Work Beyond RGBT Detection

Not RGBT detection papers. They are collected because their methods or protocols transfer directly (quality-aware fusion, imbalance and missing-modality learning, corruption benchmarks, test-time intervention). They are deliberately kept out of the main list above.

### Robust & Dynamic Fusion (General Multimodal)

1. MODA: The First Challenging Benchmark for Multispectral Object Detection in Aerial Images, AAAI 2026, Han et al. [[Paper](https://arxiv.org/abs/2512.09489)] [[Code](https://github.com/shuaihao-han/MODA)] — *benchmark; aerial*
2. SM3Det: A Unified Model for Multi-Modal Remote Sensing Object Detection, AAAI 2026, Li et al. [[Paper](https://arxiv.org/abs/2412.20665)] [[Code](https://github.com/zcablii/SM3Det)] — *aerial; expert-routing*
3. MoME: Resilient Sensor Fusion via Multi-Modal Expert Fusion, CVPR 2025, Park, Kim, Kim, Choi [[Paper](https://arxiv.org/abs/2503.19776)] — *expert-routing; degraded-modality; lidar-camera*
4. MEFormer, arXiv 2024, Cha et al. [[Paper](https://arxiv.org/abs/2407.19156)] — *negative-fusion; degraded-modality*
5. Multimodal Fusion on Low-quality Data: A Comprehensive Survey, arXiv 2024, Zhang et al. [[Paper](https://arxiv.org/abs/2404.18947)] — *survey; degraded-modality; missing-modality*
6. DynMM, CVPR Workshops 2023, Xue & Marculescu [[Paper](https://arxiv.org/abs/2204.00102)] — *dynamic-fusion; efficiency*
7. Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF), ICML 2023, Zhang et al. [[Paper](https://arxiv.org/abs/2306.02050)] — *quality-aware; degraded-modality*
8. Trusted Multi-View Classification (TMC), ICLR 2021, Han, Zhang, Fu, Zhou [[Paper](https://arxiv.org/abs/2102.02051)] — *evidential*

### Corruption Robustness Benchmarks (Driving / 3D)

1. SB-BEVFusion, arXiv (ICIP 2026) 2026, Essl et al. [[Paper](https://arxiv.org/abs/2605.11799)] — *degraded-modality; lidar-camera*
2. MultiCorrupt, IEEE IV 2024, Beemelmanns, Zhang, Eckstein [[Paper](https://arxiv.org/abs/2402.11677)] — *benchmark; corruption*
3. Benchmarking Robustness of 3D Object Detection to Common Corruptions, CVPR 2023, Dong et al. [[Paper](https://arxiv.org/abs/2303.11040)] — *benchmark; corruption*

### Modality Imbalance & Missing-Modality Learning (General)

1. MM-CKD, arXiv 2024, Sang, Funakoshi, Okumura [[Paper](https://arxiv.org/abs/2410.08692)] — *missing-modality; distillation*
2. MMPareto, ICML 2024, Wei & Hu [[Paper](https://arxiv.org/abs/2405.17730)] — *modality-imbalance*
3. Multimodal Learning with Missing Modalities: A Survey, arXiv (TMLR) 2024, Wu, Wang, Chen [[Paper](https://arxiv.org/abs/2409.07825)] — *survey; missing-modality*
4. ReconBoost, ICML 2024, Hua, Xu, Bao, Yang, Huang [[Paper](https://proceedings.mlr.press/v235/hua24a.html)] — *modality-imbalance*
5. PMR: Prototypical Modal Rebalance, CVPR 2023, Fan, Xu, Wang, Wang, Guo [[Paper](https://doi.org/10.1109/CVPR52729.2023.01918)] — *modality-imbalance*
6. ShaSpec, CVPR 2023, Wang et al. [[Paper](https://arxiv.org/abs/2307.14126)] — *missing-modality*
7. OGM-GE, CVPR (Oral) 2022, Peng, Wei, Deng, Wang, Hu [[Paper](https://arxiv.org/abs/2203.15332)] — *modality-imbalance*
8. SMIL, AAAI 2021, Ma et al. [[Paper](https://arxiv.org/abs/2103.05677)] — *missing-modality*

### Test-Time Adaptation, Intervention & Amortized Optimization

1. CD-Buffer: Complementary Dual-Buffer Framework for Test-Time Adaptation in Adverse Weather Object Detection, CVPR 2026, Song, Kim, Hwang [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_CD-Buffer_Complementary_Dual-Buffer_Framework_for_Test-Time_Adaptation_in_Adverse_Weather_CVPR_2026_paper.pdf)] [[Code](https://github.com/wkfsksdl99/cd_buffer)] — *test-time-adaptation; corruption*
2. Smoothing the Shift: Towards Stable Test-Time Adaptation under Complex Multimodal Noises, ICLR 2025, Guo, Jin [[Paper](https://arxiv.org/abs/2503.02616)] [[Code](https://github.com/zrguo/SuMi)] — *test-time-adaptation; degraded-modality*
3. Test-time Adaptation against Multi-modal Reliability Bias, ICLR 2024, Yang, Li, Zhang, Hu, Peng [[Paper](https://iclr.cc/virtual/2024/poster/18574)] [[Code](https://github.com/XLearning-SCU/2024-ICLR-READ)] — *test-time-adaptation; quality-aware*
4. Inference-Time Intervention (ITI), NeurIPS Spotlight 2023, Li, Patel, Viégas, Pfister, Wattenberg [[Paper](https://arxiv.org/abs/2306.03341)] — *test-time-intervention*
5. MEMO, NeurIPS 2022, Zhang, Levine, Finn [[Paper](https://arxiv.org/abs/2110.09506)] — *test-time-adaptation*
6. MM-TTA: Multi-Modal Test-Time Adaptation for 3D Semantic Segmentation, CVPR 2022, Shin et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shin_MM-TTA_Multi-Modal_Test-Time_Adaptation_for_3D_Semantic_Segmentation_CVPR_2022_paper.html)] — *test-time-adaptation*
7. Tent, ICLR 2021, Wang, Shelhamer, Liu, Olshausen, Darrell [[Paper](https://arxiv.org/abs/2006.10726)] — *test-time-adaptation*
8. OptNet, ICML 2017, Amos & Kolter [[Paper](https://arxiv.org/abs/1703.00443)] — *test-time-intervention*

## Repository Files

- [papers.csv](papers.csv) — **the single source of truth**: section, subsection, tags, links, DOI, contribution, notes
- [datasets.md](datasets.md) — dataset tables, KAIST tools, and robustness benchmarks (hand-maintained)
- [bibliography.md](bibliography.md) — generated detailed table (contribution and notes), same classification as this README
- [references.bib](references.bib) — generated BibTeX for all entries
- [learning-roadmap.md](learning-roadmap.md) — a staged reading path through this list (stages 0–6); a reading order, separate from the classification above
- [tools/generate.py](tools/generate.py) / tools/validate.py — regenerate and validate the list from papers.csv

## Adding an Entry

Add one row to papers.csv (that is the only edit), then run `python3 tools/generate.py && python3 tools/validate.py`. Decide the section by fusion level first (pixel / feature / decision), then the architecture family; put challenges in tags (controlled vocabulary enforced by the validator), never in a new section. Non-RGBT work goes to the Appendix. Only add entries whose paper link you have verified.

## Related Lists

- [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) — the broader RGB-T fusion collection (pedestrian/aerial detection, segmentation, salient detection, crowd counting, tracking)
- [Awesome-RGBT](https://github.com/VisionVerse/Awesome-RGBT) — RGB-T fusion across tasks
- [MOD-ZOO](https://github.com/DocF/MOD-ZOO) — curated resources accompanying a multispectral object detection survey
