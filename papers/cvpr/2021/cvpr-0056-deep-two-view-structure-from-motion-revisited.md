---
id: "cvpr-0056"
title: "Deep Two-View Structure-from-Motion Revisited"
conference: "CVPR 2021"
date: "2021-06"
authors:
  - name: "Jianyuan Wang"
    affiliation: ""
    is_industry: false
  - name: "Yiran Zhong"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuchao Dai"
    affiliation: ""
    is_industry: false
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kaihao Zhang"
    affiliation: ""
    is_industry: false
  - name: "Nikolai Smolyanskiy"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hongdong Li"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2104.00556"
abstract: "Two-view structure-from-motion (SfM) is the cornerstone of 3D reconstruction and visual SLAM. Existing deep learning-based approaches formulate the problem by either recovering absolute pose scales from two consecutive frames or predicting a depth map from a single image, both of which are ill-posed"
url: "https://research.nvidia.com/publication/2021-06_deep-two-view-structure-motion-revisited"
status: "new"
---

# Deep Two-View Structure-from-Motion Revisited

## 摘要

Two-view structure-from-motion (SfM) is the cornerstone of 3D reconstruction and visual SLAM. Existing deep learning-based approaches formulate the problem by either recovering absolute pose scales from two consecutive frames or predicting a depth map from a single image, both of which are ill-posed problems. In contrast, we propose to revisit the problem of deep two-view SfM by leveraging the well-posedness of the classic pipeline. Our method consists of 1) an optical flow estimation network that predicts dense correspondences between two frames; 2) a normalized pose estimation module that computes relative camera poses from the 2D optical flow correspondences, and 3) a scale-invariant depth estimation network that leverages epipolar geometry to reduce the search space, refine the dense correspondences, and estimate relative depth maps. Extensive experiments show that our method outperforms all state-of-the-art two-view SfM methods by a clear margin on KITTI depth, KITTI VO, MVS, Scenes11, and SUN3D datasets in both relative pose and depth estimation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
