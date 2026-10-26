# Datasets — RGBT Object Detection

Datasets and tools for RGBT (visible + thermal/LWIR) object detection. For the paper list, see the [README](README.md).

## General & Pedestrian Detection

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

## Aerial / UAV Object Detection

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

## Note — Synthetic-Infrared Datasets

- **FusionRS** ([arXiv:2606.17020](https://arxiv.org/abs/2606.17020)) — 600K spatially aligned RGB / infrared-style / text triples for remote-sensing vision-language learning (retrieval, captioning, VQA). Its infrared channel is **generated from RGB images by style transfer / diffusion, not captured by a thermal sensor**, and it is not an object-detection benchmark, so it is deliberately not mixed into the detection tables above.

## KAIST Tools

Improved annotations and evaluation utilities for the KAIST benchmark:

- Improved KAIST Testing Annotations provided by Liu et al.[download](https://docs.google.com/forms/d/e/1FAIpQLSe65WXae7J_KziHK9cmX_lP_hiDXe7Dsl6uBTRL0AWGML0MZg/viewform?usp=pp_url&entry.1637202210&entry.1381600926&entry.718112205&entry.233811498)
- Sanitized KAIST Training Annotations provided by Li et al.[download](https://github.com/Li-Chengyang/MSDS-RCNN)
- Improved KAIST Training Annotations provided by Zhang et al.[download](https://github.com/luzhang16/AR-CNN)
- Evalutaion codes.[download](https://github.com/CalayZhou/MBNet/tree/master/KAISTdevkit-matlab-wrapper)
- Annotation: vbb format->xml format.[download](https://github.com/SoonminHwang/rgbt-ped-detection/tree/master/data/scripts)
- Evaluation [Website](https://eval.ai/web/challenges/challenge-page/1247/leaderboard/3137).

## Robustness Benchmarks

- **LLVIP-C / FLIR-C** — corruption versions of LLVIP and FLIR introduced by WiSE-OD (arXiv:2507.18925), reporting AP50 and mean performance under corruption (mPC).
- **KITTI-C / nuScenes-C / Waymo-C** — 27 common corruptions for 3D detection (Dong et al., CVPR 2023, arXiv:2303.11040); a protocol reference for severity-graded corruption evaluation.
- **MultiCorrupt** — 10 LiDAR-camera corruptions × 3 severities with a Resistance Ability metric (arXiv:2402.11677).

> Note: Dataset statistics below are compiled from the datasets' official pages and the public list [Awesome-RGBT-Fusion](https://github.com/yuanmaoxun/Awesome-RGBT-Fusion) (accessed 2026-10-25); always confirm numbers on the official page before citing them.
