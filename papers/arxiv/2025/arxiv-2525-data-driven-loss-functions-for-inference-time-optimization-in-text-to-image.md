---
id: arxiv-2525
title: "Data-Driven Loss Functions for Inference-Time Optimization in Text-to-Image"
conference: arXiv 2025
date: 2025-11
authors:
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sapir Yflah"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Project Page"
    url: "https://learn-to-steer-paper.github.io/"
abstract: "Text-to-image diffusion models can generate stunning visuals, yet they often fail at tasks children find trivial - like placing a dog to the right of a teddy bear rather than to the left. When combinations get more unusual - a giraffe above an airplane—these failures become even more pronounced. Exi"
url: "https://research.nvidia.com/publication/2025-11_data-driven-loss-functions-inference-time-optimization-text-image"
status: new
---

# Data-Driven Loss Functions for Inference-Time Optimization in Text-to-Image

## 摘要

Text-to-image diffusion models can generate stunning visuals, yet they often fail at tasks children find trivial - like placing a dog to the right of a teddy bear rather than to the left. When combinations get more unusual - a giraffe above an airplane—these failures become even more pronounced. Existing methods attempt to fix these spatial reasoning failures through model fine-tuning or test-time optimization with handcrafted losses that are suboptimal. Rather than imposing our assumptions about spatial encoding, we propose learning these objectives directly from the model’s internal representations. We introduce Learn-to-Steer, a novel framework that learns data-driven objectives for test-time optimization rather than handcrafting them. Our key insight is to train a lightweight classifier that decodes spatial relationships from the diffusion model’s cross-attention maps, then deploy this classifier as a learned loss function during inference. Training such classifiers poses a surprising challenge: they can take shortcuts by detecting linguistic tracesrather than learning true spatial patterns. We solve this with a dual-inversion strategy that enforces geometric understanding. Our method dramatically improves spatial accuracy: from 0.20 to 0.61 on FLUX.1-dev and from 0.07 to 0.54 on SD2.1 across standard benchmarks. Moreover, our approach generalizes to multiple relations and significantly improves accuracy.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
