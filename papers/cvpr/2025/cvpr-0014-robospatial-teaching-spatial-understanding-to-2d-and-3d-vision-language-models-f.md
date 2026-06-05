---
id: cvpr-0014
title: "RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics"
conference: CVPR 2025
date: 2025-06
authors:
  - name: "Valts Blukis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tyree"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chan Hee Song"
    affiliation: ""
    is_industry: false
  - name: "Yu Su"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "paper"
    url: "https://arxiv.org/abs/2411.16537"
  - name: "webpage"
    url: "https://chanh.ee/RoboSpatial/"
abstract: "Spatial understanding is a crucial capability that enables robots to perceive their surroundings, reason about their environment, and interact with it meaningfully. In modern robotics, these capabilities are increasingly provided by vision-language models. However, these models face significant chal"
url: "https://research.nvidia.com/publication/2025-06_robospatial-teaching-spatial-understanding-2d-and-3d-vision-language-models"
status: new
---

# RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics

## 摘要

Spatial understanding is a crucial capability that enables robots to perceive their surroundings, reason about their environment, and interact with it meaningfully. In modern robotics, these capabilities are increasingly provided by vision-language models. However, these models face significant challenges in spatial reasoning tasks, as their training data are based on general-purpose image datasets that often lack sophisticated spatial understanding. For example, datasets frequently do not capture reference frame comprehension, yet effective spatial reasoning requires understanding whether to reason from ego-, world-, or object-centric perspectives. To address this issue, we introduce RoboSpatial, a large-scale dataset for spatial understanding in robotics. It consists of real indoor and tabletop scenes, captured as 3D scans and egocentric images, and annotated with rich spatial information relevant to robotics. The dataset includes 1M images, 5k 3D scans, and 3M annotated spatial relationships, and the pairing of 2D egocentric images with 3D scans makes it both 2D- and 3D- ready. Our experiments show that models trained with RoboSpatial outperform baselines on downstream tasks such as spatial affordance prediction, spatial relationship prediction, and robot manipulation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
