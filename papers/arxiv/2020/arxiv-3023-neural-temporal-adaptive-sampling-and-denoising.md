---
id: arxiv-3023
title: "Neural Temporal Adaptive Sampling and Denoising"
conference: arXiv 2020
date: 2020-05
authors:
  - name: "Jon Hasselgren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jacob Munkberg"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aaron Lefohn"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Salvi"
    affiliation: ""
    is_industry: false
  - name: "Anjul Patney"
    affiliation: ""
    is_industry: false
topics:
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "Still image quality comparisons"
    url: "https://diglib.eg.org/bitstream/handle/10.1111/cgf13919/image_comparisons.zip?sequence=3&amp;isAllowed=y"
abstract: "Despite recent advances in Monte Carlo path tracing at interactive rates, denoised image sequences generated with few samples per-pixel often yield temporally unstable results and loss of high-frequency details. We present a novel adaptive rendering method that increases temporal stability and image"
url: "https://research.nvidia.com/publication/2020-05_neural-temporal-adaptive-sampling-and-denoising"
status: new
---

# Neural Temporal Adaptive Sampling and Denoising

## 摘要

Despite recent advances in Monte Carlo path tracing at interactive rates, denoised image sequences generated with few samples per-pixel often yield temporally unstable results and loss of high-frequency details. We present a novel adaptive rendering method that increases temporal stability and image fidelity of low sample count path tracing by distributing samples via spatio-temporal joint optimization of sampling and denoising. Adding temporal optimization to the sample predictor enables it to learn spatio-temporal sampling strategies such as placing more samples in disoccluded regions, tracking specular highlights, etc; adding temporal feedback to the denoiser boosts the effective input sample count and increases temporal stability. The temporal approach also allows us to remove the initial uniform sampling step typically present in adaptive sampling algorithms. The sample predictor and denoiser are deep neural networks that we co-train end-to-end over multiple consecutive frames. Our approach is scalable, allowing trade-off between quality and performance, and runs at near real-time rates while achieving significantly better image quality and temporal stability than previous methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
