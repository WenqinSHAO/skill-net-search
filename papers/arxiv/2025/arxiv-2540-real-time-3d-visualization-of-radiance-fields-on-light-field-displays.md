---
id: arxiv-2540
title: "Real-time 3D Visualization of Radiance Fields on Light Field Displays"
conference: arXiv 2025
date: 2025-08
authors:
  - name: "Jonghyun Kim"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Cheng Sun"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Stengel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Luebke"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matthew Chan"
    affiliation: ""
    is_industry: false
  - name: "Andrew Russell"
    affiliation: ""
    is_industry: false
  - name: "Jaehyun Jung"
    affiliation: ""
    is_industry: false
  - name: "Wil Braithewaite"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "VR, AR and Display Technology"
external_links:
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2508.18540"
abstract: "Radiance fields have revolutionized photo-realistic 3D scene visualization by enabling high-fidelity reconstruction of complex environments, making them an ideal match for light field displays. However, integrating these technologies presents significant computational challenges, as light field disp"
url: "https://research.nvidia.com/publication/2025-08_real-time-3d-visualization-radiance-fields-light-field-displays"
status: new
---

# Real-time 3D Visualization of Radiance Fields on Light Field Displays

## 摘要

Radiance fields have revolutionized photo-realistic 3D scene visualization by enabling high-fidelity reconstruction of complex environments, making them an ideal match for light field displays. However, integrating these technologies presents significant computational challenges, as light field displays require multiple high-resolution renderings from slightly shifted viewpoints, while radiance fields rely on computationally intensive volume rendering. In this paper, we propose a unified and efficient framework for real-time radiance field rendering on light field displays. Our method supports a wide range of radiance field representations, including NeRFs, 3D Gaussian Splatting, and Sparse Voxels, within a shared architecture based on a single-pass plane sweeping strategy and caching of shared, non-directional components. The framework generalizes across different scene formats without retraining, and avoids redundant computation across views. We further demonstrate a real-time interactive application on a Looking Glass display, achieving 200+ FPS at 512p across 45 views, enabling seamless, immersive 3D interaction. On standard benchmarks, our method achieves up to 22x speedup compared to independently rendering each view, while preserving image quality.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
