---
id: cvpr-0023
title: "FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects"
conference: CVPR 2024
date: 2024-06
authors:
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wei Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Applied_perception
  - Computer Vision
  - Graphics_rendering
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Computer Graphics"
  - "Computer Vision"
  - "Robotics"
  - "VR, AR and Display Technology"
external_links:
  - name: "project page"
    url: "https://nvlabs.github.io/FoundationPose/"
  - name: "paper"
    url: "https://arxiv.org/abs/2312.08344"
abstract: "We present FoundationPose, a unified foundation model for 6D object pose estimation and tracking, supporting both model-based and model-free setups. Our approach can be instantly applied at test-time to a novel object without fine-tuning, as long as its CAD model is given, or a small number of refer"
url: "https://research.nvidia.com/publication/2024-06_foundationpose-unified-6d-pose-estimation-and-tracking-novel-objects"
status: new
---

# FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

## 摘要

We present FoundationPose, a unified foundation model for 6D object pose estimation and tracking, supporting both model-based and model-free setups. Our approach can be instantly applied at test-time to a novel object without fine-tuning, as long as its CAD model is given, or a small number of reference images are captured. We bridge the gap between these two setups with a neural implicit representation that allows for effective novel view synthesis, keeping the downstream pose estimation modules invariant under the same unified framework. Strong generalizability is achieved via large-scale synthetic training, aided by a large language model (LLM), a novel transformer-based architecture, and contrastive learning formulation. Extensive evaluation on multiple public datasets involving challenging scenarios and objects indicate our unified approach outperforms existing methods specialized for each task by a large margin. In addition, it even achieves comparable results to instance-level methods despite the reduced assumptions.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
