---
id: arxiv-2701
title: "Structural Pruning via Latency-Saliency Knapsack"
conference: arXiv 2022
date: 2022-11
authors:
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maying Shen"
    affiliation: ""
    is_industry: false
  - name: "Lei Mao"
    affiliation: ""
    is_industry: false
  - name: "Jianna Liu"
    affiliation: ""
    is_industry: false
  - name: "Jose M. Alvarez"
    affiliation: ""
    is_industry: false
topics:
  - CUDA_ecosystem
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Computer Vision"
abstract: "Structural pruning can simplify network architecture and improve inference speed. We propose Hardware-Aware Latency Pruning (HALP) that formulates structural pruning as a global resource allocation optimization problem, aiming at maximizing the accuracy while constraining latency under a predefined "
url: "https://research.nvidia.com/publication/2022-11_structural-pruning-latency-saliency-knapsack"
status: new
---

# Structural Pruning via Latency-Saliency Knapsack

## 摘要

Structural pruning can simplify network architecture and improve inference speed. We propose Hardware-Aware Latency Pruning (HALP) that formulates structural pruning as a global resource allocation optimization problem, aiming at maximizing the accuracy while constraining latency under a predefined budget on targeting&nbsp;device. For filter importance ranking, HALP leverages latency lookup table to track latency reduction potential and global saliency score to gauge accuracy drop. Both&nbsp;metrics can be evaluated very efficiently during pruning, allowing us to reformulate global structural pruning under a reward maximization problem given target&nbsp;constraint. This makes the problem solvable via our augmented knapsack solver, enabling HALP to surpass prior work in pruning efficacy and accuracy-efficiency&nbsp;trade-off. We examine HALP on both classification and detection tasks, over varying networks, on ImageNet and VOC datasets, on different platforms. In particular, for ResNet-50/-101 pruning on ImageNet, HALP improves network throughput&nbsp;by 1.60×/1.90× with +0.3%/−0.2% top-1 accuracy changes, respectively. For SSD pruning on VOC, HALP improves throughput by 1.94× with only a 0.56&nbsp;mAP drop. HALP consistently outperforms prior art, sometimes by large margins.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
