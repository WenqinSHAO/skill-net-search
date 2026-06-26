---
id: "icra-0004"
title: "SynH2R: Synthesizing Hand-Object Motions for Learning Human-to-Robot Handovers"
conference: "ICRA 2024"
date: "2024-05"
authors:
  - name: "Sammy Christen"
    affiliation: "ETH Zurich"
    is_industry: false
  - name: "Lan Feng"
    affiliation: "ETH Zurich"
    is_industry: false
  - name: "Wei Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Otmar Hilliges"
    affiliation: "ETH Zurich"
    is_industry: false
  - name: "Jie Song"
    affiliation: "ETH Zurich"
    is_industry: false
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
  - name: "Project Site"
    url: "https://eth-ait.github.io/synthetic-handovers"
abstract: "Vision-based human-to-robot handover is an important and challenging task in human-robot interaction. Recent work has attempted to train robot policies by interacting with dynamic virtual humans in simulated environments, where the policies can later be transferred to the real world. However, a majo"
url: "https://research.nvidia.com/publication/2024-05_synh2r-synthesizing-hand-object-motions-learning-human-robot-handovers"
status: "new"
---

# SynH2R: Synthesizing Hand-Object Motions for Learning Human-to-Robot Handovers

## 摘要

Vision-based human-to-robot handover is an important and challenging task in human-robot interaction. Recent work has attempted to train robot policies by interacting with dynamic virtual humans in simulated environments, where the policies can later be transferred to the real world. However, a major bottleneck is the reliance on human motion capture data, which is expensive to acquire and difficult to scale to arbitrary objects and human grasping motions. In this paper, we introduce a framework that can generate plausible human grasping motions suitable for training the robot. To achieve this, we propose a hand-object synthesis method that is designed to generate handover-friendly motions similar to humans. This allows us to generate synthetic training and testing data with 100x more objects than previous work. In our experiments, we show that our method trained purely with synthetic data is competitive with state-of-the-art methods that rely on real human motion data both in simulation and on a real system. In addition, we can perform evaluations on a larger scale compared to prior work. With our newly introduced test set, we show that our model can better scale to a large variety of unseen objects and human motions compared to the baselines.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
