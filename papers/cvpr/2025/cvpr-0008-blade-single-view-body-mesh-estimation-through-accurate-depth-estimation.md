---
id: cvpr-0008
title: "BLADE: Single-view Body Mesh Estimation through Accurate Depth Estimation"
conference: CVPR 2025
date: 2025-06
authors:
  - name: "Jiefeng Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tianye Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Stengel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shengze Wang"
    affiliation: ""
    is_industry: false
  - name: "Henry Fuchs"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Human Computer Interaction"
  - "VR, AR and Display Technology"
external_links:
  - name: "Code"
    url: "https://github.com/NVlabs/blade"
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/amri/projects/blade/"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2412.08640"
abstract: "Single-image human mesh recovery is a challenging task due to the ill-posed nature of simultaneous body shape, pose, and camera estimation. Existing estimators work well on images taken from afar, but they break down as the person moves close to the camera. Moreover, current methods fail to achieve "
url: "https://research.nvidia.com/publication/2025-06_blade-single-view-body-mesh-estimation-through-accurate-depth-estimation"
status: new
---

# BLADE: Single-view Body Mesh Estimation through Accurate Depth Estimation

## 摘要

Single-image human mesh recovery is a challenging task due to the ill-posed nature of simultaneous body shape, pose, and camera estimation. Existing estimators work well on images taken from afar, but they break down as the person moves close to the camera. Moreover, current methods fail to achieve both accurate 3D pose and 2D alignment at the same time. Error is mainly introduced by inaccurate perspective projection heuristically derived from orthographic parameters. To resolve this long-standing challenge, we present our method BLADE which accurately recovers perspective parameters from a single image without heuristic assumptions. We start from the inverse relationship between perspective distortion and the person’s Z-translation Tz, and we show that Tz can be reliably estimated from the image. We then discuss the important role of Tz for accurate human mesh recovery estimated from closerange images. Finally, we show that, once Tz and the 3D human mesh are estimated, one can accurately recover the focal length and full 3D translation. Extensive experiments on standard benchmarks and real-world close-range images show that our method accurately recovers projection parameters from a single image, and consequently attains state-of-the-art accuracy on both 3D pose estimation and 2D alignment for a wide range of images.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
