---
id: "cvpr-0030"
title: "FreeNeRF: Improving Few-shot Neural Rendering with Free Frequency Regularization"
conference: "CVPR 2023"
date: "2023-06"
authors:
  - name: "Jiawei Yang"
    affiliation: "UCLA"
    is_industry: false
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yue Wang"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2303.07418"
  - name: "Code"
    url: "https://github.com/Jiawei-Yang/FreeNeRF"
  - name: "Website"
    url: "https://jiawei-yang.github.io/FreeNeRF/"
abstract: "Novel view synthesis with sparse inputs is a challenging problem for neural radiance fields (NeRF). Recent efforts alleviate this challenge by introducing external supervision, such as pre-trained models and extra depth signals, and by non-trivial patch-based rendering. In this paper, we present Fre"
url: "https://research.nvidia.com/publication/2023-06_freenerf-improving-few-shot-neural-rendering-free-frequency-regularization"
status: "new"
---

# FreeNeRF: Improving Few-shot Neural Rendering with Free Frequency Regularization

## 摘要

Novel view synthesis with sparse inputs is a challenging problem for neural radiance fields (NeRF). Recent efforts alleviate this challenge by introducing external supervision, such as pre-trained models and extra depth signals, and by non-trivial patch-based rendering. In this paper, we present Frequency regularized NeRF (FreeNeRF), a surprisingly simple baseline that outperforms previous methods with minimal modifications to the plain NeRF. We analyze the key challenges in few-shot neural rendering and find that frequency plays an important role in NeRF’s training. Based on the analysis, we propose two regularization terms. One is to regularize the frequency range of NeRF’s inputs, while the other is to penalize the near-camera density fields. Both techniques are "free lunches" at no additional computational cost. We demonstrate that even with one line of code change, the original NeRF can achieve similar performance as other complicated methods in the few-shot setting. FreeNeRF achieves state-of-the-art performance across diverse datasets, including Blender, DTU, and LLFF. We hope this simple baseline will motivate a rethinking of the fundamental role of frequency in NeRF’s training under the low-data regime and beyond.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
