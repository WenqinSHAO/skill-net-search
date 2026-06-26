---
id: "corl-0013"
title: "RVT: Robotic View Transformer for 3D Object Manipulation"
conference: "CoRL 2023"
date: "2023-11"
authors:
  - name: "Ankit Goyal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yijie Guo"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Valts Blukis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Project Page"
    url: "https://robotic-view-transformer.github.io/"
abstract: "For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at a large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transfo"
url: "https://research.nvidia.com/publication/2023-11_rvt-robotic-view-transformer-3d-object-manipulation"
status: "new"
---

# RVT: Robotic View Transformer for 3D Object Manipulation

## 摘要

For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at a large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few (∼10) demonstrations per task. Visual results, code, and trained model are provided at: https://robotic-view-transformer.github.io/.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
