---
id: iclr-0016
title: "Energy-Based Diffusion Language Models for Text Generation"
conference: ICLR 2025
date: 2025-01
authors:
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Minkai Xu"
    affiliation: ""
    is_industry: false
  - name: "Weili Nie"
    affiliation: ""
    is_industry: false
  - name: "Yilun Xu"
    affiliation: ""
    is_industry: false
  - name: "Jure Leskovec"
    affiliation: ""
    is_industry: false
  - name: "Stefano Ermon"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2410.21357"
abstract: "Despite remarkable progress in autoregressive language models, alternative generative paradigms beyond left-to-right generation are still being actively explored. Discrete diffusion models, with the capacity for parallel generation, have recently emerged as a promising alternative. Unfortunately, th"
url: "https://research.nvidia.com/publication/2025-01_energy-based-diffusion-language-models-text-generation"
status: new
---

# Energy-Based Diffusion Language Models for Text Generation

## 摘要

Despite remarkable progress in autoregressive language models, alternative generative paradigms beyond left-to-right generation are still being actively explored. Discrete diffusion models, with the capacity for parallel generation, have recently emerged as a promising alternative. Unfortunately, these models still underperform the autoregressive counterparts, with the performance gap increasing when reducing the number of sampling steps. Our analysis reveals that this degradation is a consequence of an imperfect approximation used by diffusion models. In this work, we propose Energy-based Diffusion Language Model (EDLM), an energy-based model operating at the full sequence level for each diffusion step, introduced to improve the underlying approximation used by diffusion models. More specifically, we introduce an EBM in a residual form, and show that its parameters can be obtained by leveraging a pretrained autoregressive model or by finetuning a bidirectional transformer via noise contrastive estimation. We also propose an efficient generation algorithm via parallel important sampling. Comprehensive experiments on language modeling benchmarks show that our model can consistently outperform state-of-the-art diffusion models by a significant margin, and approaches autoregressive models’ perplexity. We further show that, without any generation performance drop, our framework offers a 1.3x sampling speedup over existing diffusion models. Reproduced code is available at https://github.com/MinkaiXu/Energy-Diffusion-LLM.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
