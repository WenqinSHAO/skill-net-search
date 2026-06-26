---
id: "arxiv-2894"
title: "RGB-D Local Implicit Function for Depth Completion of Transparent Objects"
conference: "arXiv 2021"
date: "2021-03"
authors:
  - name: "Luyang Zhu"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu Xiang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hammad Mazhar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jozef van Eenbergen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shoubhik Debnath"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
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
  - name: "Paper"
    url: "https://arxiv.org/pdf/2104.00622.pdf"
abstract: "Majority of the perception methods in robotics require depth information provided by RGB-D cameras. However, standard 3D sensors fail to capture depth of transparent objects due to refraction and absorption of light. In this paper, we introduce a new approach for depth completion of transparent obje"
url: "https://research.nvidia.com/publication/2021-03_rgb-d-local-implicit-function-depth-completion-transparent-objects"
status: "new"
---

# RGB-D Local Implicit Function for Depth Completion of Transparent Objects

## 摘要

Majority of the perception methods in robotics require depth information provided by RGB-D cameras. However, standard 3D sensors fail to capture depth of transparent objects due to refraction and absorption of light. In this paper, we introduce a new approach for depth completion of transparent objects from a single RGB-D image. Key to our approach is a local implicit neural representation built on ray-voxel pairs that allows our method to generalize to unseen objects and achieve fast inference speed. Based on this representation, we present a novel framework that can complete missing depth given noisy RGB-D input. We further improve the depth estimation iteratively using a self-correcting refinement model. To train the whole pipeline, we build a large scale synthetic dataset with transparent objects. Experiments demonstrate that our method performs significantly better than the current state-of-the-art methods on both synthetic and real world data. In addition, our approach improves the inference speed by a factor of 20 compared to the previous best method, ClearGrasp.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
