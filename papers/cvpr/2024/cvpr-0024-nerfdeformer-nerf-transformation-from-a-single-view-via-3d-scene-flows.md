---
id: "cvpr-0024"
title: "NeRFDeformer: NeRF Transformation from a Single View via 3D Scene Flows"
conference: "CVPR 2024"
date: "2024-06"
authors:
  - name: "Zhenggang Tang"
    affiliation: "UIUC"
    is_industry: false
  - name: "Zhongzheng Ren"
    affiliation: "UIUC"
    is_industry: false
  - name: "Xiaoming Zhao"
    affiliation: "UIUC"
    is_industry: false
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexander Schwing"
    affiliation: "UIUC"
    is_industry: false
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "paper"
    url: "https://arxiv.org/abs/2406.10543"
  - name: "code"
    url: "https://github.com/nerfdeformer/nerfdeformer"
  - name: "video"
    url: "https://www.youtube.com/watch?v=oZsA6i9g_yM&amp;t=1s"
  - name: "website"
    url: "https://nerfdeformer.github.io/"
abstract: "We present a method for automatically modifying a NeRF representation based on a single observation of a non-rigid transformed version of the original scene. Our method defines the transformation as a 3D flow, specifically as a weighted linear blending of rigid transformations of 3D anchor points th"
url: "https://research.nvidia.com/publication/2024-06_nerfdeformer-nerf-transformation-single-view-3d-scene-flows"
status: "new"
---

# NeRFDeformer: NeRF Transformation from a Single View via 3D Scene Flows

## 摘要

We present a method for automatically modifying a NeRF representation based on a single observation of a non-rigid transformed version of the original scene. Our method defines the transformation as a 3D flow, specifically as a weighted linear blending of rigid transformations of 3D anchor points that are defined on the surface of the scene. In order to identify anchor points, we introduce a novel correspondence algorithm that first matches RGB-based pairs, then leverages multi-view information and 3D reprojection to robustly filter false positives in two steps. We also introduce a new dataset for exploring the problem of modifying a NeRF scene through a single observation. Our dataset contains 113 synthetic scenes leveraging 47 3D assets. We show that our proposed method outperforms NeRF editing methods as well as diffusion-based methods, and we also explore different methods for filtering correspondences.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
