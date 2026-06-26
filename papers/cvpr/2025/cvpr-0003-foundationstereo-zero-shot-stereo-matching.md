---
id: "cvpr-0003"
title: "FoundationStereo: Zero-Shot Stereo Matching"
conference: "CVPR 2025"
date: "2025-06"
authors:
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matthew Trepte"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joseph Aribido"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Orazio Gallo"
    affiliation: "NVIDIA"
    is_industry: true
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
  - name: "paper"
    url: "https://arxiv.org/abs/2501.09898"
  - name: "website"
    url: "https://nvlabs.github.io/FoundationStereo/"
abstract: "Tremendous progress has been made in deep stereo matching to excel on benchmark datasets through per-domain fine-tuning. However, achieving strong zero-shot generalization - a hallmark of foundation models in other computer vision tasks - remains challenging for stereo matching. We introduce Foundat"
url: "https://research.nvidia.com/publication/2025-06_foundationstereo-zero-shot-stereo-matching"
status: "new"
---

# FoundationStereo: Zero-Shot Stereo Matching

## 摘要

Tremendous progress has been made in deep stereo matching to excel on benchmark datasets through per-domain fine-tuning. However, achieving strong zero-shot generalization - a hallmark of foundation models in other computer vision tasks - remains challenging for stereo matching. We introduce FoundationStereo, a foundation model for stereo depth estimation designed to achieve strong zero-shot generalization. To this end, we first construct a large-scale (1M stereo pairs) synthetic training dataset featuring large diversity and high photorealism, followed by an automatic self-curation pipeline to remove ambiguous samples. We then design a number of network architecture components to enhance scalability, including a side-tuning feature backbone that adapts rich monocular priors from vision foundation models to mitigate the sim-to-real gap, and long-range context reasoning for effective cost volume filtering. Together, these components lead to strong robustness and accuracy across domains, establishing a new standard in zero-shot stereo depth estimation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
