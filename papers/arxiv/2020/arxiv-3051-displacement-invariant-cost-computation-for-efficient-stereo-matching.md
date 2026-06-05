---
id: arxiv-3051
title: "Displacement-Invariant Cost Computation for Efficient Stereo Matching"
conference: arXiv 2020
date: 2020-01
authors:
  - name: "Charles Loop"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Breuel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yiran Zhong"
    affiliation: ""
    is_industry: false
  - name: "Yuchao Dai"
    affiliation: ""
    is_industry: false
  - name: "Kaihao Zhang"
    affiliation: ""
    is_industry: false
  - name: "Alexey Kamenev"
    affiliation: ""
    is_industry: false
  - name: "Hongdong Li"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2012.00899"
abstract: "Although deep learning-based methods have dominated stereo matching leaderboards by yielding unprecedented disparity accuracy, their inference time is typically slow, on the order of seconds for a pair of 540p images. The main reason is that the leading methods employ time-consuming 3D convolutions "
url: "https://research.nvidia.com/publication/2020-01_displacement-invariant-cost-computation-efficient-stereo-matching"
status: new
---

# Displacement-Invariant Cost Computation for Efficient Stereo Matching

## 摘要

Although deep learning-based methods have dominated stereo matching leaderboards by yielding unprecedented disparity accuracy, their inference time is typically slow, on the order of seconds for a pair of 540p images. The main reason is that the leading methods employ time-consuming 3D convolutions applied to a 4D feature volume. A common way to speed up the computation is to downsample the feature volume, but this loses high-frequency details. To overcome these challenges, we propose a \emph{displacement-invariant cost computation module} to compute the matching costs without needing a 4D feature volume. Rather, costs are computed by applying the same 2D convolution network on each disparity-shifted feature map pair independently. Unlike previous 2D convolution-based methods that simply perform context mapping between inputs and disparity maps, our proposed approach learns to match features between the two images. We also propose an entropy-based refinement strategy to refine the computed disparity map, which further improves speed by avoiding the need to compute a second disparity map on the right image. Extensive experiments on standard datasets (SceneFlow, KITTI, ETH3D, and Middlebury) demonstrate that our method achieves competitive accuracy with much less inference time. On typical image sizes, our method processes over 100 FPS on a desktop GPU, making our method suitable for time-critical applications such as autonomous driving. We also show that our approach generalizes well to unseen datasets, outperforming 4D-volumetric methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
