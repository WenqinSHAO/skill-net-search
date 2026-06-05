---
id: arxiv-2971
title: "UNAS: Differentiable Architecture Search Meets Reinforcement Learning"
conference: arXiv 2020
date: 2020-08
authors:
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ming-Yu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arun Mallya"
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
abstract: "Neural architecture search (NAS) aims to discover network architectures with desired properties such as high accuracy or low latency. Recently, differentiable NAS (DNAS) has demonstrated promising results while maintaining a search cost orders of magnitude lower than reinforcement learning (RL) base"
url: "https://research.nvidia.com/publication/2020-08_unas-differentiable-architecture-search-meets-reinforcement-learning"
status: new
---

# UNAS: Differentiable Architecture Search Meets Reinforcement Learning

## 摘要

Neural architecture search (NAS) aims to discover network architectures with desired properties such as high accuracy or low latency. Recently, differentiable NAS (DNAS) has demonstrated promising results while maintaining a search cost orders of magnitude lower than reinforcement learning (RL) based NAS. However, DNAS models can only optimize differentiable loss functions in search, and they require an accurate differentiable approximation of non-differentiable criteria. In this work, we present UNAS, a unified framework for NAS, that encapsulates recent DNAS and RL-based approaches under one framework. Our framework brings the best of both worlds, and it enables us to search for architectures with both differentiable and non-differentiable criteria in one unified framework while maintaining a low search cost. Further, we introduce a new objective function for search based on the generalization gap that prevents the selection of architectures prone to overfitting. We present extensive experiments on the CIFAR-10, CIFAR-100, and ImageNet datasets and we perform search in two fundamentally different search spaces. We show that UNAS obtains the state-of-the-art average accuracy on all three datasets when compared to the architectures searched in the DARTS space. Moreover, we show that UNAS can find an efficient and accurate architecture in the ProxylessNAS search space, that outperforms existing MobileNetV2 based architectures. The source code is available at&nbsp;this https URL&nbsp;.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
