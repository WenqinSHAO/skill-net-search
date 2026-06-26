---
id: "arxiv-3005"
title: "Instance-aware, Context-focused, and Memory-efficient Weakly Supervised Object Detection"
conference: "arXiv 2020"
date: "2020-06"
authors:
  - name: "Zhongzheng Ren"
    affiliation: "UIUC"
    is_industry: false
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xiaodong Yang"
    affiliation: "QCraft"
    is_industry: false
  - name: "Ming-Yu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yong Jae Lee"
    affiliation: "UC Davis"
    is_industry: false
  - name: "Alexander G. Schwing"
    affiliation: "UIUC"
    is_industry: false
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/2004.04725"
  - name: "Code"
    url: "https://github.com/NVlabs/wetectron"
  - name: "Slides"
    url: "https://chrisding.github.io/publications/CVPR20b_Slides.pdf"
abstract: "Weakly supervised learning has emerged as a compelling tool for object detection by reducing the need for strong supervision during training. However, major challenges remain: (1) differentiation of object instances can be ambiguous; (2) detectors tend to focus on discriminative parts rather than en"
url: "https://research.nvidia.com/publication/2020-06_instance-aware-context-focused-and-memory-efficient-weakly-supervised-object"
status: "new"
---

# Instance-aware, Context-focused, and Memory-efficient Weakly Supervised Object Detection

## 摘要

Weakly supervised learning has emerged as a compelling tool for object detection by reducing the need for strong supervision during training. However, major challenges remain: (1) differentiation of object instances can be ambiguous; (2) detectors tend to focus on discriminative parts rather than entire objects; (3) without ground truth, object proposals have to be redundant for high recalls, causing significant memory consumption. Addressing these challenges is difficult, as it often requires to eliminate uncertainties and trivial solutions. To target these issues we develop an instance-aware and context-focused unified framework. It employs an instance-aware self-training algorithm and a learnable Concrete DropBlock while devising a memory-efficient sequential batch back-propagation. Our proposed method achieves state-of-the-art results on COCO (12.1% AP, 24.8% AP50), VOC 2007 (54.9% AP), and VOC 2012 (52.1% AP), improving baselines by great margins. In addition, the proposed method is the first to benchmark ResNet based models and weakly supervised video object detection. Code, models, and more details will be made available at: https://github.com/NVlabs/wetectron.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
