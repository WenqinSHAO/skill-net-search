---
id: arxiv-2512
title: "3D-GENERALIST: Vision-Language-Action Models for Crafting 3D Worlds"
conference: arXiv 2026
date: 2026-03
authors:
  - name: "Alex Zook"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Valts Blukis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fan-Yun Sun"
    affiliation: ""
    is_industry: false
  - name: "Shengguang Wu"
    affiliation: ""
    is_industry: false
  - name: "Christian Jacobsen"
    affiliation: ""
    is_industry: false
  - name: "Thomas Yim"
    affiliation: ""
    is_industry: false
  - name: "Haoming Zou"
    affiliation: ""
    is_industry: false
  - name: "Shangru Li"
    affiliation: ""
    is_industry: false
  - name: "Yu-Hsin Chou"
    affiliation: ""
    is_industry: false
  - name: "Ethem Can"
    affiliation: ""
    is_industry: false
  - name: "Xunlei Wu"
    affiliation: ""
    is_industry: false
  - name: "Clemens Eppner"
    affiliation: ""
    is_industry: false
  - name: "Jiajun Wu"
    affiliation: ""
    is_industry: false
  - name: "Nick Haber"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
  - "Physical AI"
external_links:
  - name: "arxiv version"
    url: "https://arxiv.org/abs/2507.06484"
abstract: "Despite large-scale pretraining endowing models with language and vision reasoning capabilities, improving their spatial reasoning capability remains challenging due to the lack of data grounded in the 3D world. While it is possible for humans to manually create immersive and interactive worlds thro"
url: "https://research.nvidia.com/publication/2026-03%5F3d-generalist-vision-language-action-models-crafting-3d-worlds"
status: new
---

# 3D-GENERALIST: Vision-Language-Action Models for Crafting 3D Worlds

## 摘要

Despite large-scale pretraining endowing models with language and vision reasoning capabilities, improving their spatial reasoning capability remains challenging due to the lack of data grounded in the 3D world. While it is possible for humans to manually create immersive and interactive worlds through 3D graphics, as seen in applications such as VR, gaming, and robotics, this process remains highly labor-intensive. In this paper, we propose a scalable method for generating high-quality 3D environments that can serve as training data for foundation models. We recast 3D environment building as a sequential decision-making problem, employing Vision-Language-Models (VLMs) as policies that output actions to jointly craft a 3D environment's layout, materials, lighting, and assets. Our proposed framework, 3D-Generalist, trains VLMs to generate more prompt-aligned 3D environments via self-improvement fine-tuning. We demonstrate the effectiveness of 3D-Generalist and the proposed training strategy in generating simulation-ready 3D environments. Furthermore, we demonstrate its quality and scalability in synthetic data generation by pretraining a vision foundation model on the generated data. After fine-tuning the pre-trained model on downstream tasks, we show that it surpasses models pre-trained on meticulously human-crafted synthetic data and approaches results achieved with real data orders of magnitude larger.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
