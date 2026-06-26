---
id: "icra-0029"
title: "Fast Uncertainty Quantification for Deep Object Pose Estimation"
conference: "ICRA 2021"
date: "2021-05"
authors:
  - name: "Guanya Shi"
    affiliation: ""
    is_industry: false
  - name: "Yifeng Zhu"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabio Ramos"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuke Zhu"
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
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2011.07748"
  - name: "project website"
    url: "https://sites.google.com/view/fastuq"
abstract: "Deep learning-based object pose estimators are often unreliable and overconfident especially when the input image is outside the training domain, for instance, with sim2real transfer. Efficient and robust uncertainty quantification (UQ) in pose estimators is critically needed in many robotic tasks. "
url: "https://research.nvidia.com/publication/2021-05_fast-uncertainty-quantification-deep-object-pose-estimation"
status: "new"
---

# Fast Uncertainty Quantification for Deep Object Pose Estimation

## 摘要

Deep learning-based object pose estimators are often unreliable and overconfident especially when the input image is outside the training domain, for instance, with sim2real transfer. Efficient and robust uncertainty quantification (UQ) in pose estimators is critically needed in many robotic tasks. In this work, we propose a simple, efficient, and plug-and-play UQ method for 6-DoF object pose estimation. We ensemble 2-3 pre-trained models with different neural network architectures and/or training data sources, and compute their average pairwise disagreement against one another to obtain the uncertainty quantification. We propose four disagreement metrics, including a learned metric, and show that the average distance (ADD) is the best learning-free metric and it is only slightly worse than the learned metric, which requires labeled target data. Our method has several advantages compared to the prior art: 1) our method does not require any modification of the training process or the model inputs; and 2) it needs only one forward pass for each model. We evaluate the proposed UQ method on three tasks where our uncertainty quantification yields much stronger correlations with pose estimation errors than the baselines. Moreover, in a real robot grasping task, our method increases the grasping success rate from 35% to 90%.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
