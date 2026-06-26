---
id: "arxiv-2766"
title: "Interaction-Dynamics-Aware Perception Zones for Obstacle Detection Safety Evaluation"
conference: "arXiv 2022"
date: "2022-06"
authors:
  - name: "Sever Topan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karen Leung"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuxiao Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pritish Tupekar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Edward Schmerling"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonas Nilsson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Cox"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Computer Vision"
  - "Resilience and Safety"
external_links:
  - name: "Paper"
    url: "https://ieeexplore.ieee.org/document/9827409"
abstract: "To enable safe autonomous vehicle (AV) operations, it is critical that an AV’s obstacle detection module can reliably detect obstacles that pose a safety threat (i.e., are safety-critical). It is therefore desirable that the evaluation metric for the perception system captures the safety-criticality"
url: "https://research.nvidia.com/publication/2022-06_interaction-dynamics-aware-perception-zones-obstacle-detection-safety"
status: "new"
---

# Interaction-Dynamics-Aware Perception Zones for Obstacle Detection Safety Evaluation

## 摘要

To enable safe autonomous vehicle (AV) operations, it is critical that an AV’s obstacle detection module can reliably detect obstacles that pose a safety threat (i.e., are safety-critical). It is therefore desirable that the evaluation metric for the perception system captures the safety-criticality of objects. Unfortunately, existing perception evaluation metrics tend to make strong assumptions about the objects and ignore the dynamic interactions between agents, and thus do not accurately capture the safety risks in reality. To address these shortcomings, we introduce an interaction-dynamics-aware obstacle detection evaluation metric by accounting for closed-loop dynamic interactions between an ego vehicle and obstacles in the scene. By borrowing existing theory from optimal control theory, namely Hamilton-Jacobi reachability, we present a computationally tractable method for constructing a ‘‘safety zone’’: a region in state space that defines where safety-critical obstacles lie for the purpose of defining safety metrics. Our proposed safety zone is mathematically complete, and can be easily computed to reflect a variety of safety requirements. Using an off-the-shelf detection algorithm from the nuScenes detection challenge leaderboard, we demonstrate that our approach is computationally lightweight, and can better capture safety-critical perception errors than a baseline approach.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
