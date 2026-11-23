<!-- Generated from papers.csv by tools/generate.py — do not edit by hand. -->
# awesome-RGBT-ObjectDetection

A curated collection of **RGBT object detection** resources — papers, datasets, and code.

RGBT (also written RGB-T, RGB-Thermal, multispectral, or visible–infrared) object detection fuses a visible-light image with a thermal (LWIR) image to detect objects under conditions where either modality alone fails — darkness, glare, smoke, or adverse weather.

**Scope.** Object detection only: general, pedestrian, vehicle, and aerial/UAV detection with paired visible–thermal imagery. Segmentation, salient object detection, crowd counting, and tracking are out of scope (see Related Lists).

**How this list is organised — one axis only.** Papers in the main list are RGBT detection papers, classified by *technical route*: the level at which the two modalities are fused (pixel → feature → decision), with architecture families as subsections of feature-level fusion. Challenges such as misalignment, degradation, or missing modalities are **tags** (shown in italics, and a column in papers.csv), not sections — so every paper has exactly one home. Work that is not RGBT detection but transfers to it (general multimodal fusion, imbalance/missing-modality learning, test-time methods, driving robustness) lives in a separate Appendix, clearly marked, instead of being mixed into the main list.

**Single source of truth.** The paper list lives in [papers.csv](papers.csv); README.md, bibliography.md and references.bib are generated from it by [tools/generate.py](tools/generate.py) and checked by tools/validate.py. Edit the CSV, never the generated files.

## News

- [2026-11-04] Classification audit and repair (see [CLASSIFICATION.md](CLASSIFICATION.md)): the single-axis rule is now enforced in the data, not just stated. The Quality- & Conflict-Aware subsection was dissolved into the architecture subsections (quality/conflict mechanisms are tags again); Decision-Level Fusion holds only true decision-level fusion (the evidential CNN fusions moved to feature level); WiSE-OD moved to Surveys & Benchmarks; the appendix was regrouped by contribution type (surveys / benchmarks & evaluation / general methods / test-time paradigms).
- [2026-10-26] Tooling: papers.csv is now the single source of truth — README, bibliography and BibTeX are generated and validated automatically. Tag vocabulary consolidated.
- [2026-10-25] Reclassified by technical route (fusion level + architecture family), with challenge tags and a separate appendix for non-RGBT related work. 42 papers: 21 core RGBT detection, 21 appendix.
- [2026-10-25] Initial general, detection-only structure: datasets first, themed paper list, structured data files (CSV / BibTeX), detailed bibliography, learning roadmap.

## Contents

1. [Datasets](#datasets)
2. [Surveys & Benchmarks](#surveys--benchmarks)
3. [Pixel-Level Fusion for Detection](#pixel-level-fusion-for-detection)
4. [Feature-Level Fusion](#feature-level-fusion)
5. [Decision-Level Fusion](#decision-level-fusion)
6. [Appendix — Related Work Beyond RGBT Detection](#appendix--related-work-beyond-rgbt-detection)
7. [Repository Files](#repository-files)
8. [Adding an Entry](#adding-an-entry)
9. [Related Lists](#related-lists)

## Datasets

Full tables with tools and robustness benchmarks are in [datasets.md](datasets.md). Summary of the main benchmarks:

| Dataset | Year | Modalities | Images | Classes |
|---|---|---|---|---|
| [KAIST](https://soonminhwang.github.io/rgbt-ped-detection/) | 2015 | RGB, LWIR | 95K | 1 |
| [CVC-14](http://adas.cvc.uab.es/elektra/enigma-portfolio/cvc-14-visible-fir-day-night-pedestrian-sequence-dataset/) | 2016 | RGB, LWIR | 8K | 1 |
| [FLIR](https://www.flir.cn/oem/adas/adas-dataset-form/) | 2018 | RGB, LWIR | 20K | 5 |
| [FLIR-aligned](https://github.com/zonaqiu/FLIR-align) | 2020 | RGB, LWIR | 5K | 3 |
| [Utokyo](https://www.mi.t.u-tokyo.ac.jp/static/projects/mil_multispectral/) | 2017 | RGB, NIR, MIR, FIR | 7K | 5 |
| [LLVIP](https://bupt-ai-cz.github.io/LLVIP/) | 2021 | RGB, LWIR | 15K | 1 |
| [M<sup>3</sup>FD](https://github.com/dlut-dimt/TarDAL) | 2022 | RGB, LWIR | 4K | 6 |
| [Multi-Spectral Stereo](https://github.com/UkcheolShin/MS2-MultiSpectralStereoDataset) | 2023 | RGB, NIR, LWIR | 195K | 4 |
| [SMOD](https://www.kaggle.com/datasets/zizhaochen6/sjtu-multispectral-object-detection-smod-dataset) | 2024 | RGB, LWIR | 8K | 4 |
| [MMPD](https://github.com/jin-s13/MMPD-Dataset) | 2024 | RGB, LWIR | 260K | 1 |
| [InfraParis](https://ensta-u2is-ai.github.io/infraParis/) | 2024 | RGB, LWIR, Depth | 7K | 19 |
| [MFAD](https://github.com/hukefy/EI2Det) | 2025 | RGB, LWIR | 12K | 6 |
| [MMVIP](https://github.com/yyppptjr/MMVIP) | 2026 | RGB, LWIR | 128K | 2 |
| [RGBT-Ground](https://github.com/crazyxiaoxi/RGBTVG) | 2026 | RGB, LWIR | 40K | 5 |

| Dataset | Year | Modalities | Images | Classes | Alignment |
|---|---|---|---|---|---|
| [DroneVehicle](https://github.com/VisDrone/DroneVehicle) | 2021 | RGB, LWIR | 56K | 5 | Partially |
| [VEDAI](https://downloads.greyc.fr/vedai/) | 2014 | RGB, NIR | 1K | 9 | Strictly |
| [NII-CU](https://www.nii-cu-multispectral.org/) | 2022 | RGB, LWIR | 5K | 1 | Strictly |
| [DVTOD](https://github.com/VDT-2048/DVTOD) | 2024 | RGB, LWIR | 2K | 3 | Misaligned |
| [VTSaR](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10833840) | 2024 | RGB, LWIR | 40K | 1 | Strictly |
| [RGBT-Tiny](https://github.com/XinyiYing/RGBT-Tiny) | 2025 | RGB, LWIR | 93K | 7 | Partially |
| [ATR-UMOD](https://github.com/supercpy/ATR-UMOD) | 2025 | RGB, LWIR | 13K | 11 | Partially |
| [MODA](https://github.com/shuaihao-han/MODA) | 2026 | RGB, NIR | 13K | 8 | Strictly |
| [Tri-Modal Dataset](https://github.com/radlab-sketch/trimodal-uav-det.git) | 2026 | RGB, LWIR, Event | 10K | 1 | Partially |
| [DRTV30K](https://github.com/Vehicle-AHU/DRTV30K) | 2026 | RGB, LWIR | 30K | 9 | Partially |

> Dataset statistics below are compiled from the datasets' official pages and the public list [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) (accessed 2026-10-25); always confirm numbers on the official page before citing them.

## Surveys & Benchmarks

1. Camo-M3FD: A New Benchmark Dataset for Cross-Spectral Camouflaged Pedestrian Detection, arXiv 2026, Velesaca, Mero, Castillo, Sappa [[Paper](https://arxiv.org/abs/2604.16582)] — *benchmark; pedestrian*
2. DSERT-RoLL: Robust Multi-Modal Perception for Diverse Driving Conditions with Stereo Event-RGB-Thermal Cameras, 4D Radar, and Dual-LiDAR, CVPR 2026, Cho, Kang, Jeong, Yang, Lee, Kim, Yoon [[Paper](https://arxiv.org/abs/2604.03685)] — *benchmark*
3. Early versus Late RGB-Infrared Fusion for Counter-UAV Detection: A Comparative Study, IEEE Access 2026, De Zan, Tavaris, Foresti, Scagnetto [[Paper](https://doi.org/10.1109/ACCESS.2026.3735919)] — *benchmark*
4. G-MAD: A Game-Based Data Generation Framework for Multi-View RGB-T Aerial Object Detection, arXiv 2026, Kim, Park, Yoon, Jung, Jeon [[Paper](https://arxiv.org/abs/2607.19942)] — *benchmark; aerial*
5. UAV-CB: A Complex-Background RGB-T Dataset and Local Frequency Bridge Network for UAV Detection, CVPR 2026, Huang et al. [[Paper](https://arxiv.org/abs/2603.17492)] — *benchmark; aerial; frequency-domain*
6. WiSE-OD: Benchmarking Robustness in Infrared Object Detection, WACV 2026, Medeiros, Belal, Aminbeidokhti, Granger, Pedersoli [[Paper](https://arxiv.org/abs/2507.18925)] [[Code](https://github.com/heitorrapela/wiseod)] — *degraded-modality; benchmark; thermal-only-inference*
7. Fusion Meets Diverse Conditions: A High-diversity Benchmark and Baseline for UAV-based Multimodal Object Detection with Condition Cues, ICCV 2025, Chen et al. [[Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Fusion_Meets_Diverse_Conditions_A_High-diversity_Benchmark_and_Baseline_for_ICCV_2025_paper.pdf)] — *benchmark; aerial; degraded-modality*
8. Infrared and Visible Image Fusion: From Data Compatibility to Task Adaption, IEEE TPAMI 2025, Liu, Wu, Liu, Wang, Jiang, Ma, Zhong, Fan, Liu [[Paper](https://arxiv.org/abs/2501.10761)] — *survey*
9. Visible-Thermal Tiny Object Detection: A Benchmark Dataset and Baselines (RGBT-Tiny), IEEE TPAMI 2025, Ying et al. [[Paper](https://arxiv.org/abs/2406.14482)] [[Code](https://github.com/XinyiYing/RGBT-Tiny)] — *aerial; benchmark*
10. Misaligned Visible-Thermal Object Detection: A Drone-based Benchmark and Baseline (DVTOD), IEEE TIV 2024, Song et al. [[Paper](https://doi.org/10.1109/TIV.2024.3398429)] [[Code](https://github.com/VDT-2048/DVTOD)] — *benchmark; aerial; alignment*
11. Optimizing Multispectral Object Detection: A Bag of Tricks and Comprehensive Benchmarks, arXiv 2024, Zhou, Cheng, Fang, Zhang, Yan, Jia, Xu, Wang, Cao [[Paper](https://arxiv.org/abs/2411.18288)] — *benchmark*
12. When Pedestrian Detection Meets Multi-Modal Learning: Generalist Model and Benchmark Dataset (MMPedestron), ECCV 2024, Zhang et al. [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06487.pdf)] [[Code](https://github.com/BubblyYi/MMPedestron)] — *benchmark; pedestrian; foundation-model*

## Pixel-Level Fusion for Detection

1. SGLDet: Spectral-aware Global-Local Dynamic Modeling for Multispectral Aerial Object Detection, IEEE TGRS 2026, Zhang, Han, Xu, Li [[Paper](https://arxiv.org/abs/2610.27883)] — *aerial*
2. TriDifNet: A Unified Three-Task Diffusion Network for End-to-End RGB-T Perception, arXiv 2026, He, Liu, Li, Tian [[Paper](https://arxiv.org/abs/2610.37097)] — *alignment; pedestrian; image-fusion*
3. DDFD: Diffusion-Based Denoising Fusion for Object Detection in Infrared-Visible Images, ACM MM 2025, Dang et al. [[Paper](https://dl.acm.org/doi/10.1145/3746027.3755183)] — *image-fusion; task-coupled; degraded-modality*
4. E2E-MFD: Towards End-to-End Synchronous Multimodal Fusion Detection, NeurIPS 2024, Zhang et al. [[Paper](https://arxiv.org/abs/2403.09323)] [[Code](https://github.com/icey-zhang/EfficientMFD)] — *image-fusion; task-coupled; aerial*
5. CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion, CVPR 2023, Zhao, Bai, Zhang, Zhang, Xu, Lin, Timofte, Van Gool [[Paper](https://arxiv.org/abs/2211.14461)] — *image-fusion; task-coupled*
6. MetaFusion: Infrared and Visible Image Fusion via Meta-Feature Embedding from Object Detection, CVPR 2023, Zhao, Xie, Zhao, He, Lu [[Paper](https://doi.org/10.1109/CVPR52729.2023.01341)] — *image-fusion; task-coupled*
7. SuperYOLO: Super Resolution Assisted Object Detection in Multimodal Remote Sensing Imagery, IEEE TGRS 2023, Zhang et al. [[Paper](https://doi.org/10.1109/TGRS.2023.3258666)] [[Code](https://github.com/icey-zhang/SuperYOLO)] — *image-fusion; aerial; yolo; efficiency*
8. DetFusion: A Detection-driven Infrared and Visible Image Fusion Network, ACM MM 2022, Sun et al. [[Paper](https://dl.acm.org/doi/pdf/10.1145/3503161.3547902)] [[Code](https://github.com/SunYM2020/DetFusion)] — *image-fusion; task-coupled*
9. TarDAL: Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection, CVPR 2022, Liu, Fan, Huang, Wu, Liu, Zhong, Luo [[Paper](https://arxiv.org/abs/2203.16220)] [[Code](https://github.com/JinyuanLiu-CV/TarDAL)] — *image-fusion; task-coupled*

## Feature-Level Fusion

### Attention, Transformers & Foundation Models

1. Balanced Multi-Modality Knowledge Mining for RGB-Infrared Object Detection, Neural Networks 2026, Ma, Zhang, Mao, Chai, Wang [[Paper](https://doi.org/10.1016/j.neunet.2025.108421)] — *transformer*
2. Bridging Multimodal Fusion and Expert Routing via Spectral Reliability Descriptors for Robust Object Detection, arXiv 2026, Wu [[Paper](https://arxiv.org/abs/2606.01173)] — *quality-aware; expert-routing; degraded-modality; aerial*
3. DEF-Net: A dual-modal feature enhancement and fusion network for infrared and visible object detection, PLOS One 2026, Guo, Yang, Ji [[Paper](https://doi.org/10.1371/journal.pone.0345815)] — *cross-attention; transformer*
4. DETR Is Secretly a Multispectral Detector: Zero-Parameter Adaptation via Semantic Alignment (ZPA-MDETR), ECCV 2026, Li, Tian, Jiang, Jin, Niu, Liu [[Paper](https://doi.org/10.1007/978-3-032-37038-9_22)] — *alignment; transformer; detr; efficiency*
5. DMPFDet: An End-to-End Deformable Mutual-Promotion Learning Network for Multispectral Visible-Infrared Fusion Detection, Neural Networks 2026, Zheng, Liu, Zeng [[Paper](https://doi.org/10.1016/j.neunet.2026.108654)] — *transformer; detr*
6. Distribution-Aligned Multimodal Fusion for Robust Object Detection, CVPR 2026, Hao, Pu, Wang, She [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Hao_Distribution-Aligned_Multimodal_Fusion_for_Robust_Object_Detection_CVPR_2026_paper.pdf)] — *degraded-modality; quality-aware*
7. Dual Sparse Aggregation Transformer for Multispectral Object Detection, arXiv 2026, Wu, Zhang, Yin, Zhang, Zhang [[Paper](https://arxiv.org/abs/2606.31015)] — *transformer*
8. DyFCLT: Dynamic Frequency-Decoupled Cross-Modal Learning Transformer for Multimodal Tiny Object Detection, CVPR 2026, Li, Dai, Li, Yao, Jiang, Zheng [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_DyFCLT_Dynamic_Frequency-Decoupled_Cross-Modal_Learning_Transformer_for_Multimodal_Tiny_Object_CVPR_2026_paper.pdf)] — *transformer; frequency-domain; aerial*
9. FreDFT: Frequency Domain Fusion Transformer for Visible-Infrared Object Detection, IEEE TMM 2026, Wu, Zhang, Yin, Dai, Zhang, Zhang [[Paper](https://doi.org/10.1109/TMM.2026.3712630)] — *frequency-domain; transformer*
10. LF-DETR: a Laplacian frequency enhanced DETR for aerial RGB-infrared pedestrian detection, Remote Sensing 2026, Qi, Qin, Xiang, Yang, Tan [[Paper](https://doi.org/10.3390/rs18030531)] — *frequency-domain; detr; pedestrian; aerial*
11. Learning to Correct Cross-Modality Bounding Box Shifts in Drone-Based RGBT Object Detection, IEEE TCSVT 2026, Zhang, Yang, Xu, Hu, Xu, Xia [[Paper](https://doi.org/10.1109/TCSVT.2026.3690161)] — *alignment; aerial*
12. MAFTNet: Multimodal Adaptive Fusion-Based Transformer Network for Infrared and Visible Image UAV Object Detection, IEEE Sensors Journal 2026, Liu, Ni, Zhang, Gu, Yang [[Paper](https://doi.org/10.1109/JSEN.2025.3649961)] — *aerial*
13. MSAFusion: A Lightweight Multispectral Pedestrian Detection Network with Multi-Scale and Adaptive Feature Fusion, Journal of Imaging 2026, Song, Zuo, Qu, Qian, Jiang [[Paper](https://doi.org/10.3390/jimaging12060246)] — *pedestrian; efficiency*
14. Modality-Decoupled RGB-Thermal Object Detector via Query Fusion, arXiv 2026, Tian et al. [[Paper](https://arxiv.org/abs/2601.08458)] — *detr; transformer; dual-stream*
15. RegisterBridgeMM: A Register-Centric Framework for RGB-Infrared Object Detection, arXiv 2026, Wang, Liang, Chen, Li, Guo, Liu, Gu [[Paper](https://arxiv.org/abs/2608.04833)] — *foundation-model; efficiency*
16. Residual Optimal Transport-Based Experts Collaboration Towards Modality-Aware Infrared-Visible Object Detection, arXiv 2026, Zhao, Yu, Zhao, Zhang, Gong, Mei, Hu, Li, Qin [[Paper](https://arxiv.org/abs/2609.03516)] — *missing-modality; expert-routing*
17. Thermal-Det: Language-Guided Cross-Modal Distillation for Open-Vocabulary Thermal Object Detection, CVPR 2026, Ranasinghe et al. [[Paper](https://arxiv.org/abs/2605.10130)] — *foundation-model; distillation; thermal-only-inference*
18. Tri-Modal Fusion Transformers for UAV-based Object Detection, arXiv 2026, Iaboni, Abichandani [[Paper](https://arxiv.org/abs/2604.16630)] — *aerial*
19. Visible-Infrared Fusion Based on CNN and Deformable Transformer, Journal of Imaging 2026, Wang, Gu, Li, Zhang, Yang, Fu [[Paper](https://doi.org/10.3390/jimaging12060219)] — *transformer*
20. WD-FQDet: Multispectral Detection Transformer via Wavelet Decomposition and Frequency-aware Query Learning, arXiv 2026, Yang, Zhang, Xiao, Meng [[Paper](https://arxiv.org/abs/2605.13621)] — *frequency-domain; detr*
21. M-SpecGene: Generalized Foundation Model for RGBT Multispectral Vision, ICCV 2025, Zhou et al. [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_M-SpecGene_Generalized_Foundation_Model_for_RGBT_Multispectral_Vision_ICCV_2025_paper.html)] [[Code](https://github.com/CalayZhou/M-SpecGene)] — *foundation-model*
22. Mixed Patch Visible-Infrared Modality Agnostic Object Detection (MiPa), WACV 2025, Medeiros et al. [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Medeiros_Mixed_Patch_Visible-Infrared_Modality_Agnostic_Object_Detection_WACV_2025_paper.html)] [[Code](https://github.com/heitorrapela/MiPa)] — *missing-modality; modality-imbalance; transformer*
23. SAM-Guided Semantic Knowledge Fusion for Visible-Infrared Object Detection, ACM MM 2025, Li et al. [[Paper](https://dl.acm.org/doi/10.1145/3746027.3755718)] [[Code](https://github.com/liting1018/SemFusion)] — *foundation-model*
24. Towards a Generalizable Fusion Architecture for Multimodal Object Detection, ICCV Workshops 2025, Berjawi, Dupas, Cérin [[Paper](https://arxiv.org/abs/2510.17078)] [[Code](https://github.com/jadberjawi/FMCAF)] — *cross-attention; frequency-domain*
25. UniRGB-IR: A Unified Framework for Visible-Infrared Semantic Tasks via Adapter Tuning, ACM MM 2025, Yuan, Cui, Zhao, Wang, Fu, Yang, Wei [[Paper](https://arxiv.org/abs/2404.17360)] — *foundation-model; adapter*
26. C2Former: Calibrated and Complementary Transformer, IEEE TGRS 2024, Yuan & Wei [[Paper](https://arxiv.org/abs/2306.16175)] [[Code](https://github.com/yuanmaoxun/C2Former)] — *alignment; cross-attention; transformer*
27. CF-Deformable DETR: An End-to-End Alignment-Free Model for Weakly Aligned Visible-Infrared Object Detection, IJCAI 2024, Fu et al. [[Paper](https://www.ijcai.org/proceedings/2024/0084.pdf)] [[Code](https://github.com/116508/CF-Deformable-DETR)] — *detr; alignment; transformer*
28. DAMSDet: Dynamic Adaptive Multispectral Detection Transformer with Competitive Query Selection and Adaptive Feature Fusion, ECCV 2024, Guo, Gao, Liu, Meng, Gao [[Paper](https://eccv.ecva.net/virtual/2024/poster/801)] [[Code](https://github.com/gjj45/DAMSDet)] — *transformer; detr*
29. GM-DETR, CVPR Workshops 2024, Xiao, Meng, Wu, Xu, He, Li [[Paper](https://openaccess.thecvf.com/content/CVPR2024W/JRDB/papers/Xiao_GM-DETR_Generalized_Muiltispectral_DEtection_TRansformer_with_Efficient_Fusion_Encoder_for_CVPRW_2024_paper.pdf)] — *transformer; detr; efficiency*
30. ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection, Pattern Recognition 2024, Shen, Chen, Liu, Zuo, Fan, Yang [[Paper](https://doi.org/10.1016/j.patcog.2023.109913)] [[Code](https://github.com/chanchanchan97/ICAFusion)] — *cross-attention*
31. Improving RGB-Infrared Object Detection with Cascade Alignment-Guided Transformer (CAGT), Information Fusion 2024, Yuan, Shi, Wang, Wang, Wei [[Paper](https://doi.org/10.1016/j.inffus.2024.102246)] — *alignment; aerial; transformer; cross-attention*
32. Cross-Modality Fusion Transformer (CFT), arXiv 2021, Fang, Han, Wang [[Paper](https://arxiv.org/abs/2111.00273)] — *cross-attention; transformer*
33. Guided Attentive Feature Fusion for Multispectral Pedestrian Detection (GAFF), WACV 2021, Zhang, Fromont, Lefèvre, Avignon [[Paper](https://openaccess.thecvf.com/content/WACV2021/html/Zhang_Guided_Attentive_Feature_Fusion_for_Multispectral_Pedestrian_Detection_WACV_2021_paper.html)] — *pedestrian; cross-attention; efficiency*
34. Cross-Modality Interactive Attention Network for Multispectral Pedestrian Detection (CIAN), Information Fusion 2019, Zhang et al. [[Paper](https://doi.org/10.1016/j.inffus.2018.09.015)] — *pedestrian; cross-attention*

### Dual-Stream CNN & YOLO-Based Detectors

1. ACSE: Advantage Complementation and Salient Feature-Enhanced Fusion for Visible-Infrared Object Detection, Journal of King Saud University - Computer and Information Sciences 2026, Zhu, Song, Zhou, Gong, Zhu [[Paper](https://doi.org/10.1007/s44443-026-00732-4)] — *cross-attention; dual-stream*
2. Aligned Consensus Teaching for Label-Efficient Oriented Object Detection in Weakly-Aligned Visible-Infrared Imagery, arXiv 2026, Ming, Yuan, Zhou, Li, Zhao, Huang, Fang, Huang, Pizurica [[Paper](https://arxiv.org/abs/2609.18124)] — *alignment; aerial*
3. Boundary-Guided Dual-Perspective Cross-Modal Fusion Network for RGB-IR Object Detection (BDPNet), Remote Sensing 2026, Lin, Fu, Chen, Feng [[Paper](https://doi.org/10.3390/rs18183175)] — *quality-aware*
4. Bridging Severe Cross-Modal Misalignment: End-to-End Visible-Infrared Object Detection via Explicit Feature-Domain Affine Registration, arXiv 2026, Ming et al. [[Paper](https://arxiv.org/abs/2608.10680)] — *alignment; aerial*
5. Bridging the RGB-IR Gap: Consensus and Discrepancy Modeling for Text-Guided Multispectral Detection, arXiv 2026, Wu, Wang, Huang, Shen, Wang, Yue, Pu, Huang [[Paper](https://arxiv.org/abs/2604.11234)] — *alignment*
6. CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection, arXiv 2026, Hatami, Faez, Sharifian, Amindavar [[Paper](https://arxiv.org/abs/2608.06205)] — *yolo*
7. DDEF-Net: A Difference-Guided Detail Enhancement Fusion Network for UAV-Based RGB-T Object Detection, Remote Sensing 2026, Li, Chen, Ma, Xu [[Paper](https://doi.org/10.3390/rs18173032)] — *aerial*
8. DICFNet: Dual Information Complementary Fusion Network for Multispectral Pedestrian Detection, Machines 2026, Wang, Li [[Paper](https://doi.org/10.3390/machines14111354)] — *pedestrian*
9. DRPFNet: Dual-domain Residual Progressive Fusion Network for RGB-Thermal Object Detection, arXiv 2026, Wang, Li [[Paper](https://arxiv.org/abs/2608.03370)] — *frequency-domain; yolo*
10. Dual-Correlation Hypergraph Network for Unaligned RGBT Video Object Detection and A Large-scale Benchmark, arXiv 2026, Wang, Li, Tu, Li, Luo [[Paper](https://arxiv.org/abs/2607.08191)] — *alignment*
11. Efficient RGB-T Object Detection via Sparse Cross-Modality Fusion, arXiv 2026, Tian et al. [[Paper](https://arxiv.org/abs/2606.30215)] — *efficiency*
12. F2Net: Mitigating Spectral Imbalance and Detail Attenuation in RGB-Thermal Object Detection via Frequency-Guided Multimodal Fusion, Sensors 2026, Du, Zhao, Song, Hu, Wang, Wu [[Paper](https://doi.org/10.3390/s26134145)] — *frequency-domain; yolo*
13. FSMF: A reliability-guided RGB-IR object detection network with complementary information decoupling for autonomous driving, Scientific Reports 2026, Yang, Guo, Cheng, Fang [[Paper](https://doi.org/10.1038/s41598-026-71402-8)] — *quality-aware*
14. FoCal: Frequency-Oriented Cross-Modal Interaction and Spectral Calibration for Aerial Visible-Infrared Object Detection, arXiv 2026, Liang, Sui, Bai, Liu, Li, Sui, Chen [[Paper](https://arxiv.org/abs/2609.29125)] — *frequency-domain; aerial*
15. GEM-YOLO: A Lightweight and Real-Time RGBT Object Detector with Gated Multimodal Fusion, Sensors 2026, Wang, Bao, Lu [[Paper](https://doi.org/10.3390/s26072035)] — *yolo; efficiency*
16. HAFM: A Post-Fusion Gating Module for Haze-Aware RGB-Thermal Object Detection, CVPR Findings 2026, Saeteros, Arevalo, Vintimilla [[Paper](https://openaccess.thecvf.com/content/CVPR2026F/papers/Saeteros_HAFM_A_Post-Fusion_Gating_Module_for_Haze-Aware_RGB-Thermal_Object_Detection_CVPRF_2026_paper.pdf)] — *degraded-modality; quality-aware*
17. IRDFusion: Iterative Relation-map Difference Guided Feature Fusion for Multispectral Object Detection, Pattern Recognition 2026, Shen et al. [[Paper](https://doi.org/10.1016/j.patcog.2026.113189)] — *dual-stream*
18. InfraNet: Quality-Aware RGB Guidance for Infrared Object Detection, ECCV 2026, Feng, Zhu, Yang, Xu, Ren, Yang, Liu, Zhang, Wang, Yang, Zhang [[Paper](https://eccv.ecva.net/virtual/2026/poster/3873)] — *quality-aware; missing-modality*
19. LDFE: Laplacian Decoupled Feature Enhancement Block for Dual-Stream CNN-based RGB-IR Object Detection, Pattern Recognition 2026, Dong, Luo, Yang, Zhu, Shi, Guo, Zhang [[Paper](https://doi.org/10.1016/j.patcog.2026.113935)] — *frequency-domain; dual-stream*
20. LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection, arXiv 2026, Hou et al. [[Paper](https://arxiv.org/abs/2605.20667)] — *alignment; expert-routing; aerial; yolo; quality-aware*
21. LMB-Net: Light-Aware Modality Balancing Network for Multimodal Pedestrian Detection, Mathematics 2026, Fu, Zhang, Li [[Paper](https://doi.org/10.3390/math14091567)] — *pedestrian; alignment*
22. LMDENet: A Lightweight RGB-IR Object Detection Network for Low-Light Remote Sensing Images, Sensors 2026, Weng, Niu [[Paper](https://doi.org/10.3390/s26041130)] — *efficiency*
23. M2I2HA: Multi-modal Object Detection Based on Intra- and Inter-Modal Hypergraph Attention, arXiv 2026, Yang, Liu, Pan, Chu, Zhang, Zhao, Man, Cao [[Paper](https://arxiv.org/abs/2601.14776)] — *alignment*
24. MDCFT-HSM: Modality-Shift-Aware RGB-T Small-Object Detection for Low-Altitude UAV Remote Sensing, Sensors 2026, Long, Wang, Yuan, Zhang, Ma, Zhou, Wang, Wang [[Paper](https://doi.org/10.3390/s26165146)] — *degraded-modality; missing-modality; aerial*
25. Modality Dominance-Aware Optimization for Embodied RGB-Infrared Perception, arXiv 2026, Liu, Jiang, Xie, Lin, Liu [[Paper](https://arxiv.org/abs/2601.00598)] — *modality-imbalance*
26. Progressive Pixel-Neighborhood Deformable Cross-Attention for Multispectral Object Detection, Sensors 2026, Qiu, Shen, Zuo [[Paper](https://doi.org/10.3390/s26123825)] — *alignment*
27. ProtoHGF-Net: Prototype HyperGraph Fusion with Intra-modal Calibration for RGBT Object Detection, ACM MM 2026, Chen, Zhang, Yang, Zhao, Zhang, Wang, Chen, Wang, Peng, Zheng [[Paper](https://arxiv.org/abs/2608.11595)] — *distillation; aerial*
28. Removal Then Selection: A Coarse-to-Fine Fusion Perspective for RGB-Infrared Object Detection, IEEE TITS 2026, Zhao, Yuan, Jiang, Wang, Wei [[Paper](https://arxiv.org/abs/2401.10731)] — *conflict-aware; quality-aware*
29. Robust Pedestrian Detection with Uncertain Modality (AUNet), AAAI 2026, Bie, Wang, Yang, Yu, Chen, Xu [[Paper](https://arxiv.org/abs/2602.06363)] — *missing-modality; pedestrian; expert-routing*
30. SCAFusion: RGB-T Cross-Modal Fusion for Object Detection, SSRN 2026, Zhang, Wang [[Paper](https://doi.org/10.2139/ssrn.6988597)] — *yolo; dynamic-fusion; quality-aware*
31. Small Target Detection Based on Mask-Enhanced Attention Fusion of Visible and Infrared Remote Sensing Images, arXiv 2026, Zhang, Jia, Abdelmoniem, Zhou, An [[Paper](https://arxiv.org/abs/2603.06925)] — *aerial*
32. ZOS-Net: A Lightweight RGB-T Object Detection Network With Cross-Modal Relation Enhancement and Selective Target Awareness, Remote Sensing 2026, Dai, Guo, Yue [[Paper](https://doi.org/10.3390/rs18183112)] — *efficiency*
33. EI²Det: Edge-Guided Illumination-Aware Interactive Learning for Visible-Infrared Object Detection, IEEE TCSVT 2025, Hu et al. [[Paper](https://doi.org/10.1109/TCSVT.2025.3539625)] [[Code](https://github.com/hukefy/EI2Det)] — *quality-aware*
34. Efficient Multispectral Object Detection with Attentive Feature Aggregation Leveraging Zero-Shot Implicit Illumination Guidance, Information Fusion 2025, Xiong et al. [[Paper](https://doi.org/10.1016/j.inffus.2025.102939)] — *efficiency; quality-aware*
35. Learning a Robust RGB-Thermal Detector for Extreme Modality Imbalance, Pattern Recognition Letters 2025, Tian, Yang, Zhu, Wang, He [[Paper](https://arxiv.org/abs/2505.22154)] — *degraded-modality; quality-aware; modality-imbalance*
36. Representation Space Constrained Learning with Modality Decoupling for Multimodal Object Detection, arXiv 2025, Shao, Shi [[Paper](https://arxiv.org/abs/2511.15433)] [[Code](https://github.com/yikangshao/RSC-MD)] — *negative-fusion; modality-imbalance*
37. Rethinking Multi-modal Object Detection from the Perspective of Mono-Modality Feature Learning (M2D-LIF), ICCV 2025, Zhao et al. [[Paper](https://arxiv.org/abs/2503.11780)] [[Code](https://github.com/Zhao-Tian-yi/M2D-LIF)] — *modality-imbalance; distillation*
38. TFDet: Target-Aware Fusion for RGB-T Pedestrian Detection, IEEE TNNLS 2025, Zhang et al. [[Paper](https://arxiv.org/abs/2305.16580)] — *pedestrian; task-coupled*
39. Weakly Aligned Feature Fusion for Multimodal Object Detection, IEEE TNNLS 2025, Zhang et al. [[Paper](https://doi.org/10.1109/TNNLS.2021.3105143)] — *alignment; dual-stream*
40. YOLOv11-RGBT: Towards a Comprehensive Single-Stage Multispectral Object Detection Framework, arXiv 2025, Wan, Lu, Fang, Lang, Shu, Chen, Shen, Xu, Ye [[Paper](https://arxiv.org/abs/2506.14696)] [[Code](https://github.com/wandahangFY/YOLOv11-RGBT)] — *yolo; efficiency*
41. Causal Mode Multiplexer: A Novel Framework for Unbiased Multispectral Pedestrian Detection, CVPR 2024, Kim et al. [[Paper](https://arxiv.org/abs/2403.01300)] [[Code](https://github.com/ssbin0914/Causal-Mode-Multiplexer)] — *pedestrian; modality-imbalance*
42. DEYOLO: Dual-Feature-Enhancement YOLO for Cross-Modality Object Detection, ICPR 2024, Chen, Wang, Guo, Zhu, He, Liu, Yuan [[Paper](https://arxiv.org/abs/2412.04931)] — *yolo; dual-stream*
43. LRAF-Net: Long-Range Attention Fusion Network for Visible–Infrared Object Detection, IEEE TNNLS 2024, Fu, Wang, Duan, Xiao, Dian, Li, Li [[Paper](https://doi.org/10.1109/TNNLS.2023.3266452)] — *dual-stream; modality-imbalance*
44. Multiscale Cross-modal Homogeneity Enhancement and Confidence-aware Fusion for Multispectral Pedestrian Detection, IEEE TMM 2024, Li et al. [[Paper](https://doi.org/10.1109/TMM.2023.3272471)] [[Code](https://github.com/RimXidian/MCHE-CF-for-Multispectral-Pedestrian-Detection)] — *pedestrian; quality-aware*
45. Stabilizing Multispectral Pedestrian Detection with Evidential Hybrid Fusion, IEEE TCSVT 2024, Li, Zhang, Hu, Zhu, Fu, Chen [[Paper](https://doi.org/10.1109/TCSVT.2023.3306870)] — *evidential; pedestrian*
46. Weakly Misalignment-free Adaptive Feature Alignment for UAVs-based Multimodal Object Detection (OAFA), CVPR 2024, Chen et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_Weakly_Misalignment-free_Adaptive_Feature_Alignment_for_UAVs-based_Multimodal_Object_Detection_CVPR_2024_paper.pdf)] — *alignment; aerial*
47. CALNet (Cross-Modal Conflict-Aware Learning), ACM MM 2023, He, Tang, Zou, Zhang [[Paper](https://doi.org/10.1145/3581783.3612651)] [[Code](https://github.com/hexiao0275/CALNet-Dronevehicle)] — *conflict-aware; aerial*
48. Confidence-Aware Fusion via Dempster–Shafer (CMPD), IEEE TMM 2023, Li, Zhang, Hu, Fu, Zhu [[Paper](https://ieeexplore.ieee.org/document/9739079)] — *evidential; pedestrian*
49. BAANet: Learning Bi-Directional Adaptive Attention Gates for Multispectral Pedestrian Detection, ICRA 2022, Yang, Qian, Zhu, Wang, Yang [[Paper](https://arxiv.org/abs/2112.02277)] — *pedestrian; quality-aware*
50. Drone-Based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning (UA-CMDet), IEEE TCSVT 2022, Sun, Cao, Zhu, Hu [[Paper](https://doi.org/10.1109/TCSVT.2022.3168279)] [[Code](https://github.com/VisDrone/DroneVehicle)] — *aerial; quality-aware*
51. Learning a Dynamic Cross-Modal Network for Multispectral Pedestrian Detection (DCMNet), ACM MM 2022, Xie et al. [[Paper](https://doi.org/10.1145/3503161.3547895)] — *pedestrian; dynamic-fusion*
52. Translation, Scale and Rotation: Cross-Modal Alignment Meets RGB-Infrared Vehicle Detection (TSFADet), ECCV 2022, Yuan, Wang, Wei [[Paper](https://arxiv.org/abs/2209.13801)] — *alignment; aerial*
53. MLPD: Multi-Label Pedestrian Detector in Multispectral Domain, IEEE RA-L 2021, Kim et al. [[Paper](https://doi.org/10.1109/LRA.2021.3099870)] — *pedestrian; alignment*
54. Improving Multispectral Pedestrian Detection by Addressing Modality Imbalance Problems (MBNet), ECCV 2020, Zhou, Chen, Cao [[Paper](https://arxiv.org/abs/2008.03043)] [[Code](https://github.com/CalayZhou/MBNet)] — *modality-imbalance; pedestrian; alignment*
55. Fusion of Multispectral Data Through Illumination-Aware Deep Neural Networks for Pedestrian Detection (IATDNN), Information Fusion 2019, Guan et al. [[Paper](https://arxiv.org/abs/1802.09972)] — *pedestrian; quality-aware*
56. Illumination-Aware Faster R-CNN for Robust Multispectral Pedestrian Detection, Pattern Recognition 2019, Li, Song, Tong, Tang [[Paper](https://doi.org/10.1016/j.patcog.2018.08.005)] — *pedestrian; quality-aware*
57. Weakly Aligned Cross-Modal Learning for Multispectral Pedestrian Detection (AR-CNN), ICCV 2019, Zhang et al. [[Paper](https://arxiv.org/abs/1901.02645)] [[Code](https://github.com/luzhang16/AR-CNN)] — *alignment; pedestrian*
58. Multispectral Pedestrian Detection via Simultaneous Detection and Segmentation (MSDS-RCNN), BMVC 2018, Li, Song, Tong, Tang [[Paper](https://arxiv.org/abs/1808.04818)] — *pedestrian; dual-stream*
59. Multispectral Deep Neural Networks for Pedestrian Detection (Halfway Fusion), BMVC 2016, Liu, Zhang, Wang, Metaxas [[Paper](https://arxiv.org/abs/1611.02644)] — *pedestrian; dual-stream*

### State-Space Models (Mamba)

1. DHMD: Harnessing the Power of State Space Models for Advanced Vehicle-Aware RGB-T Object Detection in Spatial-Frequency Domain, IEEE TGRS 2026, Yu, Li, Lv, Gong, Fu, Huang, Yu, Jiang [[Paper](https://doi.org/10.1109/TGRS.2026.3739095)] — *mamba; frequency-domain*
2. DLRMamba: Distilling Low-Rank Mamba for Edge Multispectral Fusion Object Detection, arXiv 2026, Zhang, Tabaro, Abdelmoniem, An [[Paper](https://arxiv.org/abs/2603.06920)] — *efficiency; mamba*
3. MWEFDet: Mamba and Wavelet Enhanced Fusion Toward Multispectral Object Detection, Multimedia Systems 2026, Yang, Xue, Li, Wang, Luan [[Paper](https://doi.org/10.1007/s00530-026-02549-7)] — *mamba; frequency-domain*
4. Multispectral State-Space Feature Fusion: Bridging Shared and Cross-Parametric Interactions for Object Detection, Information Fusion 2026, Shen et al. [[Paper](https://doi.org/10.1016/j.inffus.2025.103895)] — *mamba*
5. WIM-Net: Wavelet Interactive Mamba Fusion Network for UAV Small Object Detection with Visible-Thermal Data, Sensors 2026, Gao, Guo [[Paper](https://doi.org/10.3390/s26206625)] — *mamba; frequency-domain; aerial*
6. Contextually-Guided State Space Fusion for Misaligned Multi-Spectral Object Detection (CSSFDet), ACM MM 2025, Jin et al. [[Paper](https://dl.acm.org/doi/10.1145/3746027.3754550)] — *mamba; alignment; aerial*
7. Fusion-Mamba for Cross-modality Object Detection, IEEE TMM 2025, Dong, Zhu, Lin, Luo, Shen, Liu, Zhang, Guo, Zhang [[Paper](https://doi.org/10.1109/TMM.2025.3599020)] — *mamba*
8. Pseudo Visible Feature Fine-Grained Fusion for Thermal Object Detection (PFGF), CVPR 2025, Li et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Pseudo_Visible_Feature_Fine-Grained_Fusion_for_Thermal_Object_Detection_CVPR_2025_paper.pdf)] [[Code](https://github.com/liting1018/PFGF)] — *mamba; missing-modality; thermal-only-inference*
9. WaveMamba: Wavelet-Driven Mamba Fusion for RGB-Infrared Object Detection, ICCV 2025, Zhu, Dong, Yang, Li, Yang, Ren, Zhu, Feng, Li, Lin, Wang, Luo, Zhang [[Paper](https://arxiv.org/abs/2507.18173)] [[Code](https://github.com/EhanDong/WaveMamba)] — *mamba; frequency-domain*
10. Mask-Guided Mamba Fusion for Drone-based Visible-Infrared Vehicle Detection, IEEE TGRS 2024, Wang et al. [[Paper](https://doi.org/10.1109/TGRS.2024.3452550)] — *mamba; aerial*

## Decision-Level Fusion

1. Training-Free Post-Inference Fusion for RGB-Thermal Object Detection: An Evaluation with a Negative Result for Reliability-Aware Rules, Technologies 2026, Alotaibi, Alanizi, Haq, Khan [[Paper](https://doi.org/10.3390/technologies14110720)] — *negative-fusion; yolo*
2. Multimodal Object Detection via Probabilistic Ensembling, ECCV 2022, Chen, Shi, Ye, Mertz, Ramanan, Kong [[Paper](https://arxiv.org/abs/2104.02904)] — *missing-modality; ensemble; pedestrian*

## Appendix — Related Work Beyond RGBT Detection

Not RGBT detection papers. They are collected because their methods or protocols transfer directly (quality-aware fusion, imbalance and missing-modality learning, corruption benchmarks, test-time intervention). They are deliberately kept out of the main list above.

### Surveys (General Multimodal)

1. Deep Multimodal Learning with Missing Modality: A Survey, TMLR 2026, Wu, Wang, Chen, Carneiro [[Paper](https://arxiv.org/abs/2409.07825)] — *survey; missing-modality*
2. Multimodal Fusion on Low-quality Data: A Comprehensive Survey, arXiv 2024, Zhang, Wei, Han, Fu, Peng, Deng, Hu, Xu, Wen, Hu, Zhang [[Paper](https://arxiv.org/abs/2404.18947)] — *survey; degraded-modality; missing-modality*

### Benchmarks & Evaluation Studies

1. 3D on-road object detection based on fusion of RGB and infrared images, Infrared Physics & Technology 2026, Tian, Huang, Deng, Yu [[Paper](https://www.sciencedirect.com/science/article/abs/pii/S1350449526001556)] — *benchmark*
2. MODA: The First Challenging Benchmark for Multispectral Object Detection in Aerial Images, AAAI 2026, Han et al. [[Paper](https://arxiv.org/abs/2512.09489)] [[Code](https://github.com/shuaihao-han/MODA)] — *benchmark; aerial*
3. Multimodal Object Detection Under Sparse Forest-Canopy Occlusion, arXiv 2026, Jain, Kothari [[Paper](https://arxiv.org/abs/2605.15326)] — *lidar-camera; yolo*
4. Physical Adversarial Clothing Evades Visible-Thermal Detectors via Non-Overlapping RGB-T Pattern, CVPR 2026, Zhu, Zeng, Hu, Zhu, Hu [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_Physical_Adversarial_Clothing_Evades_Visible-Thermal_Detectors_via_Non-Overlapping_RGB-T_Pattern_CVPR_2026_paper.pdf)] [[Code](https://github.com/zxp555/RGBT-Clothing)] — *corruption*
5. MultiCorrupt: A Multi-Modal Robustness Dataset and Benchmark of LiDAR-Camera Fusion for 3D Object Detection, IEEE IV 2024, Beemelmanns, Zhang, Geller, Eckstein [[Paper](https://arxiv.org/abs/2402.11677)] — *benchmark; corruption*
6. Benchmarking Robustness of 3D Object Detection to Common Corruptions, CVPR 2023, Dong, Kang, Zhang, Zhu, Wang, Yang, Su, Wei, Zhu [[Paper](https://arxiv.org/abs/2303.11040)] — *benchmark; corruption*

### Robust & Dynamic Fusion (General Multimodal)

1. Evidential Deep Learning for Multi-Modal Anti-UAV Detection, arXiv 2026, Golovchits, Ziabari, Alsahag [[Paper](https://arxiv.org/abs/2609.01742)] — *evidential*
2. Fully Rotation-Equivariant Spectral-Spatial Learning for Multispectral Object Detection, ECCV 2026, Zhang, Xu, Han, Li [[Paper](https://arxiv.org/abs/2607.05148)] — *quality-aware*
3. S3E-Det: A Strict Spatial-Spectral Equivariant Detector for Multispectral Object Detection, IEEE Sensors Journal 2026, Zhang, Xu, Sui, Tian, Li [[Paper](https://arxiv.org/abs/2610.27882)] — *aerial*
4. SB-BEVFusion: Enhancing the Robustness against Sensor Malfunction and Corruptions, arXiv (ICIP 2026) 2026, Essl, Moscati, Noman, Zaheer, Naseem, Nawaz, Schedl [[Paper](https://arxiv.org/abs/2605.11799)] — *degraded-modality; lidar-camera*
5. SM3Det: A Unified Model for Multi-Modal Remote Sensing Object Detection, AAAI 2026, Li et al. [[Paper](https://arxiv.org/abs/2412.20665)] [[Code](https://github.com/zcablii/SM3Det)] — *aerial; expert-routing*
6. Resilient Sensor Fusion Under Adverse Sensor Failures via Multi-Modal Expert Fusion, CVPR 2025, Park, Kim, Kim, Choi [[Paper](https://arxiv.org/abs/2503.19776)] — *expert-routing; degraded-modality; lidar-camera*
7. Robust Multimodal 3D Object Detection via Modality-Agnostic Decoding and Proximity-based Modality Ensemble, arXiv 2024, Cha, Joo, Park, Lee, Kim, Kim [[Paper](https://arxiv.org/abs/2407.19156)] — *negative-fusion; degraded-modality*
8. Dynamic Multimodal Fusion, CVPR Workshops 2023, Xue & Marculescu [[Paper](https://arxiv.org/abs/2204.00102)] — *dynamic-fusion; efficiency*
9. Provable Dynamic Fusion for Low-Quality Multimodal Data (QMF), ICML 2023, Zhang, Wu, Zhang, Hu, Fu, Zhou, Peng [[Paper](https://arxiv.org/abs/2306.02050)] — *quality-aware; degraded-modality*
10. Trusted Multi-View Classification (TMC), ICLR 2021, Han, Zhang, Fu, Zhou [[Paper](https://arxiv.org/abs/2102.02051)] — *evidential*

### Modality Imbalance & Missing-Modality Learning (General)

1. Contrastive Knowledge Distillation for Robust Multimodal Sentiment Analysis, arXiv 2024, Sang, Funakoshi, Okumura [[Paper](https://arxiv.org/abs/2410.08692)] — *missing-modality; distillation*
2. MMPareto: Boosting Multimodal Learning with Innocent Unimodal Assistance, ICML 2024, Wei & Hu [[Paper](https://arxiv.org/abs/2405.17730)] — *modality-imbalance*
3. ReconBoost: Boosting Can Achieve Modality Reconcilement, ICML 2024, Hua, Xu, Bao, Yang, Huang [[Paper](https://proceedings.mlr.press/v235/hua24a.html)] — *modality-imbalance*
4. Multi-modal Learning with Missing Modality via Shared-Specific Feature Modelling, CVPR 2023, Wang, Chen, Ma, Avery, Hull, Carneiro [[Paper](https://arxiv.org/abs/2307.14126)] — *missing-modality*
5. PMR: Prototypical Modal Rebalance, CVPR 2023, Fan, Xu, Wang, Wang, Guo [[Paper](https://doi.org/10.1109/CVPR52729.2023.01918)] — *modality-imbalance*
6. Balanced Multimodal Learning via On-the-fly Gradient Modulation, CVPR (Oral) 2022, Peng, Wei, Deng, Wang, Hu [[Paper](https://arxiv.org/abs/2203.15332)] — *modality-imbalance*
7. SMIL: Multimodal Learning with Severely Missing Modality, AAAI 2021, Ma, Ren, Zhao, Tulyakov, Wu, Peng [[Paper](https://arxiv.org/abs/2103.05677)] — *missing-modality*

### Test-Time Adaptation, Intervention & Amortized Optimization

1. CD-Buffer: Complementary Dual-Buffer Framework for Test-Time Adaptation in Adverse Weather Object Detection, CVPR 2026, Song, Kim, Hwang [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Song_CD-Buffer_Complementary_Dual-Buffer_Framework_for_Test-Time_Adaptation_in_Adverse_Weather_CVPR_2026_paper.pdf)] [[Code](https://github.com/wkfsksdl99/cd_buffer)] — *test-time-adaptation; corruption*
2. Shifting Focus by Reliability: Geometric Fusion Modulation for Robust RGB-T Detection, arXiv 2026, Shi, Li, He [[Paper](https://arxiv.org/abs/2610.41204)] — *degraded-modality; quality-aware*
3. Smoothing the Shift: Towards Stable Test-Time Adaptation under Complex Multimodal Noises, ICLR 2025, Guo, Jin [[Paper](https://arxiv.org/abs/2503.02616)] [[Code](https://github.com/zrguo/SuMi)] — *test-time-adaptation; degraded-modality*
4. Test-time Adaptation against Multi-modal Reliability Bias, ICLR 2024, Yang, Li, Zhang, Hu, Peng [[Paper](https://iclr.cc/virtual/2024/poster/18574)] [[Code](https://github.com/XLearning-SCU/2024-ICLR-READ)] — *test-time-adaptation; quality-aware*
5. Inference-Time Intervention (ITI), NeurIPS Spotlight 2023, Li, Patel, Viégas, Pfister, Wattenberg [[Paper](https://arxiv.org/abs/2306.03341)] — *test-time-intervention*
6. MEMO: Test Time Robustness via Adaptation and Augmentation, NeurIPS 2022, Zhang, Levine, Finn [[Paper](https://arxiv.org/abs/2110.09506)] — *test-time-adaptation*
7. MM-TTA: Multi-Modal Test-Time Adaptation for 3D Semantic Segmentation, CVPR 2022, Shin et al. [[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shin_MM-TTA_Multi-Modal_Test-Time_Adaptation_for_3D_Semantic_Segmentation_CVPR_2022_paper.html)] — *test-time-adaptation*
8. Tent: Fully Test-time Adaptation by Entropy Minimization, ICLR 2021, Wang, Shelhamer, Liu, Olshausen, Darrell [[Paper](https://arxiv.org/abs/2006.10726)] — *test-time-adaptation*
9. OptNet: Differentiable Optimization as a Layer in Neural Networks, ICML 2017, Amos & Kolter [[Paper](https://arxiv.org/abs/1703.00443)] — *test-time-intervention*

## Repository Files

- [papers.csv](papers.csv) — **the single source of truth**: section, subsection, tags, links, DOI, contribution, notes
- [CLASSIFICATION.md](CLASSIFICATION.md) — the classification rules: one axis (fusion stage, then architecture family), mechanisms as tags, appendix grouped by contribution type
- [datasets.md](datasets.md) — dataset tables (generated from datasets.csv), KAIST tools, and robustness benchmarks
- [datasets.csv](datasets.csv) — the structured dataset source (REQ-06): modalities, pair counts, splits, metrics, protocols per dataset
- [protocols.csv](protocols.csv) — robustness evaluation protocols: degradation types, severities, single- vs dual-modality scope, metrics
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
