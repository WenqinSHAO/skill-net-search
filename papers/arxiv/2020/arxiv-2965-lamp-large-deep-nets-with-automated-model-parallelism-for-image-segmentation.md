---
id: arxiv-2965
title: "LAMP: Large Deep Nets with Automated Model Parallelism for Image Segmentation"
conference: arXiv 2020
date: 2020-10
authors:
  - name: "Can Zhao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wenqi Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Holger Roth"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ziyue Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daguang Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wentao Zhu"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Medical_imaging
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Medical"
external_links:
  - name: "Code"
    url: "https://monai.io/research/lamp-automated-model-parallelism"
abstract: "Deep Learning (DL) models are becoming larger, because the increase in model size might offer significant accuracy gain. To enable the training of large deep networks, data parallelism and model parallelism are two well-known approaches for parallel training. However, data parallelism does not help "
url: "https://research.nvidia.com/publication/2020-10_lamp-large-deep-nets-automated-model-parallelism-image-segmentation"
status: new
---

# LAMP: Large Deep Nets with Automated Model Parallelism for Image Segmentation

## 摘要

Deep Learning (DL) models are becoming larger, because the increase in model size might offer significant accuracy gain. To enable the training of large deep networks, data parallelism and model parallelism are two well-known approaches for parallel training. However, data parallelism does not help reduce memory footprint per device. In this work, we introduce Large deep 3D ConvNets with Automated Model Parallelism (LAMP) and investigate the impact of both input's and deep 3D ConvNets' size on segmentation accuracy. Through automated model parallelism, it is feasible to train large deep 3D ConvNets with a large input patch, even the whole image. Extensive experiments demonstrate that, facilitated by the automated model parallelism, the segmentation accuracy can be improved through increasing model size and input context size, and large input yields significant inference speedup compared with sliding window of small patches in the inference. Code is available\footnote{https://monai.io/research/lamp-automated-model-parallelism}.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
