---
id: "neurips-0009"
title: "Minitron-SSM: Efficient Hybrid Language Model Compression through Group-Aware SSM Pruning"
conference: "NeurIPS 2025"
date: "2025-04"
authors:
  - name: "Ali Taghibakhshi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sharath Turuvekere Sreenivas"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Saurav Muralidharan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marcin Chochowski"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yashaswi Karnati"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Raviraj Joshi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ameya Sunil Mahabaleshwarkar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zijia Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yoshi Suhara"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oluwatobi Olabiyi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Korzekwa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mostofa Patwary"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mohammad Shoeybi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bryan Catanzaro"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ashwath Aithal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nima Tajbakhsh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "Natural Language Processing"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2504.11409"
abstract: "Hybrid LLM architectures that combine Attention and State Space Models (SSMs) achieve state-of-the-art accuracy and runtime performance. Recent work has demonstrated that applying compression and distillation to Attention-only models yields smaller, more accurate models at a fraction of the training"
url: "https://research.nvidia.com/publication/2025-04_minitron-ssm-efficient-hybrid-language-model-compression-through-group-aware"
status: "new"
---

# Minitron-SSM: Efficient Hybrid Language Model Compression through Group-Aware SSM Pruning

## 摘要

Hybrid LLM architectures that combine Attention and State Space Models (SSMs) achieve state-of-the-art accuracy and runtime performance. Recent work has demonstrated that applying compression and distillation to Attention-only models yields smaller, more accurate models at a fraction of the training cost. In this work, we explore the effectiveness of compressing Hybrid architectures. We introduce a novel group-aware pruning strategy that preserves the structural integrity of SSM blocks and their sequence modeling capabilities. Furthermore, we demonstrate the necessity of such SSM pruning to achieve improved accuracy and inference speed compared to traditional approaches. Our compression recipe combines SSM, FFN, embedding dimension, and layer pruning, followed by knowledge distillation-based retraining, similar to the MINITRON technique. Using this approach, we compress the Nemotron-H 8B Hybrid model down to 4B parameters with up to 40x fewer training tokens. The resulting model surpasses the accuracy of similarly-sized models while achieving 2x faster inference, significantly advancing the Pareto frontier.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
