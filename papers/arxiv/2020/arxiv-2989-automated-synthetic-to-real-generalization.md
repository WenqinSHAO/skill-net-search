---
id: "arxiv-2989"
title: "Automated Synthetic-to-Real Generalization"
conference: "arXiv 2020"
date: "2020-07"
authors:
  - name: "Wuyang Chen"
    affiliation: "Texas A&M"
    is_industry: false
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhangyang Wang"
    affiliation: "Texas A&M"
    is_industry: false
  - name: "Anima Anandkumar"
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
  - name: "Project Page"
    url: "https://sites.google.com/nvidia.com/asg"
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/2007.06965"
  - name: "Code"
    url: "https://github.com/NVlabs/ASG"
  - name: "Slides"
    url: "https://chrisding.github.io/publications/ICML20b_Slides.pdf"
abstract: "Models trained on synthetic images often face degraded generalization to real data. As a convention, these models are often initialized with ImageNet pre-trained representation. Yet the role of ImageNet knowledge is seldom discussed despite common practices that leverage this knowledge to maintain t"
url: "https://research.nvidia.com/publication/2020-07_automated-synthetic-real-generalization"
status: "new"
---

# Automated Synthetic-to-Real Generalization

## 摘要

Models trained on synthetic images often face degraded generalization to real data. As a convention, these models are often initialized with ImageNet pre-trained representation. Yet the role of ImageNet knowledge is seldom discussed despite common practices that leverage this knowledge to maintain the generalization ability. An example is the careful hand-tuning of early stopping and layer-wise learning rates, which is shown to improve synthetic-to-real generalization but is also laborious and heuristic. In this work, we explicitly encourage the synthetically trained model to maintain similar representations with the ImageNet pre-trained model, and propose a learning-to-optimize (L2O)&nbsp;strategy to automate the selection of layer-wise learning rates. We demonstrate that the proposed framework can significantly improve the synthetic-to-real generalization performance without seeing and training on real data, while also benefiting downstream tasks such as domain adaptation. Code is available at: https://github.com/NVlabs/ASG.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
