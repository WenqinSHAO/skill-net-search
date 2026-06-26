---
id: "icra-0025"
title: "Single-Stage Keypoint-Based Category-Level Object Pose Estimation from an RGB Image"
conference: "ICRA 2022"
date: "2022-02"
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
  - name: "arXiv"
    url: "https://arxiv.org/abs/2109.06161"
  - name: "code"
    url: "https://github.com/NVlabs/CenterPose"
abstract: "Prior work on 6-DoF object pose estimation has largely focused on instance-level processing, in which a textured CAD model is available for each object being detected. Category-level 6-DoF pose estimation represents an important step toward developing robotic vision systems that operate in unstructu"
url: "https://research.nvidia.com/publication/2022-02_single-stage-keypoint-based-category-level-object-pose-estimation-rgb-image"
status: "new"
---

# Single-Stage Keypoint-Based Category-Level Object Pose Estimation from an RGB Image

## 摘要

Prior work on 6-DoF object pose estimation has largely focused on instance-level processing, in which a textured CAD model is available for each object being detected. Category-level 6-DoF pose estimation represents an important step toward developing robotic vision systems that operate in unstructured, real-world scenarios. In this work, we propose a single-stage, keypoint-based approach for category-level object pose estimation that operates on unknown object instances within a known category using a single RGB image as input. The proposed network performs 2D object detection, detects 2D keypoints, estimates 6-DoF pose, and regresses relative bounding cuboid dimensions. These quantities are estimated in a sequential fashion, leveraging the recent idea of convGRU for propagating information from easier tasks to those that are more difficult. We favor simplicity in our design choices: generic cuboid vertex coordinates, single-stage network, and monocular RGB input. We conduct extensive experiments on the challenging Objectron benchmark, outperforming state-of-the-art methods on the 3D IoU metric (27.6% higher than the MobilePose single-stage approach and 7.1% higher than the related two-stage approach).

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
