---
id: icml-0008
title: "DoRA: Weight-Decomposed Low-Rank Adaptation"
conference: ICML 2024
date: 2024-07
authors:
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Frank Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shih-Yang Liu"
    affiliation: ""
    is_industry: false
  - name: "Chien-Yi Wang"
    affiliation: ""
    is_industry: false
  - name: "Kwang-Ting Cheng"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
  - "Natural Language Processing"
external_links:
  - name: "Project Website"
    url: "https://nbasyl.github.io/DoRA-project-page/"
  - name: "arXiv"
    url: "https://arxiv.org/abs/2402.09353"
  - name: "Code"
    url: "https://github.com/NVlabs/DoRA"
  - name: "NVIDIA Tech Blog"
    url: "https://developer.nvidia.com/blog/introducing-dora-a-high-performing-alternative-to-lora-for-fine-tuning/"
abstract: "In this ICML'24 Oral paper, we first introduce a novel weight decomposition analysis to investigate the inherent differences between FT and LoRA. Aiming to resemble the learning capacity of FT from the findings, we propose Weight-Decomposed LowRank Adaptation (DoRA). DoRA decomposes the pre-trained "
url: "https://research.nvidia.com/publication/2024-07_dora-weight-decomposed-low-rank-adaptation"
status: new
---

# DoRA: Weight-Decomposed Low-Rank Adaptation

## 摘要

In this ICML'24 Oral paper, we first introduce a novel weight decomposition analysis to investigate the inherent differences between FT and LoRA. Aiming to resemble the learning capacity of FT from the findings, we propose Weight-Decomposed LowRank Adaptation (DoRA). DoRA decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning, specifically employing LoRA for directional updates to efficiently minimize the number of trainable parameters. By employing DoRA, we enhance both the learning capacity and training stability of LoRA while avoiding any additional inference overhead. DoRA consistently outperforms LoRA on fine-tuning LLaMA, LLaVA, and VL-BART on various downstream tasks, such as commonsense reasoning, visual instruction tuning, and image/video-text understanding. Code available at this https URL.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
