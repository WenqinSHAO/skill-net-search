---
id: iclr-0024
title: "FasterViT: Fast Vision Transformers with Hierarchical Attention"
conference: ICLR 2024
date: 2024-05
authors:
  - name: "Greg Heinrich"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ali Hatamizadeh"
    affiliation: ""
    is_industry: false
  - name: "Andrew Tao"
    affiliation: ""
    is_industry: false
  - name: "Jose M. Alvarez"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "https://arxiv.org/abs/2306.06189"
    url: "https://github.com/NVlabs/FasterViT"
abstract: "We design a new family of hybrid CNN-ViT neural networks, named FasterViT, with a focus on high image throughput for computer vision (CV) applications. FasterViT combines the benefits of fast local representation learning in CNNs and global modeling properties in ViT. Our newly introduced Hierarchic"
url: "https://research.nvidia.com/publication/2024-05_fastervit-fast-vision-transformers-hierarchical-attention"
status: new
---

# FasterViT: Fast Vision Transformers with Hierarchical Attention

## 摘要

We design a new family of hybrid CNN-ViT neural networks, named FasterViT, with a focus on high image throughput for computer vision (CV) applications. FasterViT combines the benefits of fast local representation learning in CNNs and global modeling properties in ViT. Our newly introduced Hierarchical Attention (HAT) approach decomposes global self-attention with quadratic complexity into a multi-level attention with reduced computational costs. We benefit from efficient window-based self-attention. Each window has access to dedicated carrier tokens that participate in local and global representation learning. At a high level, global self-attentions enable the efficient cross-window communication at lower costs. FasterViT achieves a SOTA Pareto-front in terms of accuracy and image throughput. We have extensively validated its effectiveness on various CV tasks including classification, object detection and segmentation. We also show that HAT can be used as a plug-and-play module for existing networks and enhance them. We further demonstrate significantly faster and more accurate performance than competitive counterparts for images with high resolution.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
