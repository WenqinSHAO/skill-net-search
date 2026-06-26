---
id: "arxiv-2504"
title: "GalaxyDiT: Efficient Video Generation with Guidance Alignment and Adaptive Proxy in Diffusion Transformers"
conference: "arXiv 2026"
date: "2026-07"
authors:
  - name: "Zoey Song"
    affiliation: "Massachusetts Institute of Technology"
    is_industry: false
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
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
external_links:
  - name: "Paper text"
    url: "https://arxiv.org/abs/2512.03451"
abstract: "Diffusion models have revolutionized video generation, becoming essential tools in creative content generation and physical simulation. Transformer-based architectures (DiTs) and classifier-free guidance (CFG) are two cornerstones of this success, enabling strong prompt adherence and realistic video"
url: "https://research.nvidia.com/publication/2026-07%5Fgalaxydit-efficient-video-generation-guidance-alignment-and-adaptive-proxy"
status: "new"
---

# GalaxyDiT: Efficient Video Generation with Guidance Alignment and Adaptive Proxy in Diffusion Transformers

## 摘要

Diffusion models have revolutionized video generation, becoming essential tools in creative content generation and physical simulation. Transformer-based architectures (DiTs) and classifier-free guidance (CFG) are two cornerstones of this success, enabling strong prompt adherence and realistic video quality. Despite their versatility and superior performance, these models require intensive computation. Each video generation requires dozens of iterative steps, and CFG doubles the required compute. This inefficiency hinders broader adoption in downstream applications. We introduce GalaxyDiT, a training-free method to accelerate video generation with guidance alignment and systematic proxy selection for reuse metrics. Through rank-order correlation analysis, our technique identifies the optimal proxy for each video model, across model families and parameter scales, thereby ensuring optimal computational reuse. We achieve 1.87× and 2.37× speedup on Wan2.1-1.3B and Wan2.1-14B with only 0.97% and 0.72% drops on the VBench-2.0 benchmark. At high speedup rates, our approach maintains superior fidelity to the base model, exceeding prior state-of-the-art approaches by 5 to 10 dB in peak signal-to-noise ratio (PSNR).&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
