---
id: neurips-0020
title: "Self-Taught Recognizer: Toward Unsupervised Adaptation for Speech Foundation Models"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuchen Hu"
    affiliation: ""
    is_industry: false
  - name: "Chen Chen"
    affiliation: ""
    is_industry: false
  - name: "Chengwei Qin"
    affiliation: ""
    is_industry: false
  - name: "Pin-Yu Chen"
    affiliation: ""
    is_industry: false
  - name: "Eng Siong Chng"
    affiliation: ""
    is_industry: false
  - name: "Chao Zhang"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Generative AI"
  - "Machine Translation"
  - "Natural Language Processing"
  - "Speech Processing"
abstract: "We propose an unsupervised adaptation framework, Self-TAught Recognizer (STAR), which leverages unlabeled data to enhance the robustness of automatic speech recognition (ASR) systems in diverse target domains, such as noise and accents. STAR is developed for prevalent speech foundation models based "
url: "https://research.nvidia.com/publication/2024-12_self-taught-recognizer-toward-unsupervised-adaptation-speech-foundation-models"
status: new
---

# Self-Taught Recognizer: Toward Unsupervised Adaptation for Speech Foundation Models

## 摘要

We propose an unsupervised adaptation framework, Self-TAught Recognizer (STAR), which leverages unlabeled data to enhance the robustness of automatic speech recognition (ASR) systems in diverse target domains, such as noise and accents. STAR is developed for prevalent speech foundation models based on Transformer-related architecture with auto-regressive decoding (e.g., Whisper, Canary). Specifically, we propose a novel indicator that empirically integrates step-wise information during decoding to assess the token-level quality of pseudo labels without ground truth, thereby guiding model updates for effective unsupervised adaptation. Experimental results show that STAR achieves an average of 13.5% relative reduction in word error rate across 14 target domains, and it sometimes even approaches the upper-bound performance of supervised adaptation. Surprisingly, we also observe that STAR prevents the adapted model from the common catastrophic forgetting problem without recalling source-domain data. Furthermore, STAR exhibits high data efficiency that only requires less than one-hour unlabeled data, and seamless generality to alternative large speech models and speech translation tasks

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
