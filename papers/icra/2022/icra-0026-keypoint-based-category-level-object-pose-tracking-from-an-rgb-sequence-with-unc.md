---
id: "icra-0026"
title: "Keypoint-Based Category-Level Object Pose Tracking from an RGB Sequence with Uncertainty Estimation"
conference: "ICRA 2022"
date: "2022-01"
authors:
  - name: "Yunzhi Lin"
    affiliation: "NVIDIA, Georgia Institute of Technology"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tyree"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Patricio A. Vela"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "code"
    url: "https://github.com/NVlabs/CenterPose"
abstract: "We propose a single-stage, category-level 6-DoF pose estimation algorithm that simultaneously detects and tracks instances of objects within a known category. &nbsp;Our method takes as input the previous and current frame from a monocular RGB video, as well as predictions from the previous frame, to"
url: "https://research.nvidia.com/publication/2022-01_keypoint-based-category-level-object-pose-tracking-rgb-sequence-uncertainty"
status: "new"
---

# Keypoint-Based Category-Level Object Pose Tracking from an RGB Sequence with Uncertainty Estimation

## 摘要

We propose a single-stage, category-level 6-DoF pose estimation algorithm that simultaneously detects and tracks instances of objects within a known category. &nbsp;Our method takes as input the previous and current frame from a monocular RGB video, as well as predictions from the previous frame, to predict the bounding cuboid and 6-DoF pose (up to scale). &nbsp;Internally, a deep network predicts distributions over object keypoints (vertices of the bounding cuboid) in image coordinates, after which a novel probabilistic filtering process integrates across estimates before computing the final pose using PnP. &nbsp;Our framework allows the system to take previous uncertainties into consideration when predicting the current frame, resulting in predictions that are more accurate and stable than single frame methods. &nbsp;Extensive experiments show that our method outperforms existing approaches on the challenging Objectron benchmark of annotated object videos. &nbsp;We also demonstrate the usability of our work in an augmented reality setting.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
