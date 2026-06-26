---
id: "arxiv-2544"
title: "Identity-Motion Trade-offs in Text-to-Video Generation"
conference: "arXiv 2025"
date: "2025-07"
authors:
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rinon Gal"
    affiliation: ""
    is_industry: false
  - name: "Yoad Tewel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yoni Kasten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project page"
    url: "https://research.nvidia.com/labs/par/MotionByQueries/"
abstract: "Text-to-video diffusion models have shown remarkable progress in generating coherent video clips from textual descriptions. However, the interplay between motion, structure, and identity representations in these models remains under-explored. Here, we investigate how self-attention query (Q) feature"
url: "https://research.nvidia.com/publication/2025-07_identity-motion-trade-offs-text-video-generation"
status: "new"
---

# Identity-Motion Trade-offs in Text-to-Video Generation

## 摘要

Text-to-video diffusion models have shown remarkable progress in generating coherent video clips from textual descriptions. However, the interplay between motion, structure, and identity representations in these models remains under-explored. Here, we investigate how self-attention query (Q) features simultaneously govern motion, structure, and identity and examine the challenges arising when these representations interact. Our analysis reveals that Q affects not only layout, but that during denoising Q also has a strong effect on subject identity, making it hard to transfer motion without the side-effect of transferring identity. Understanding this dual role enabled us to control query feature injection (Q-injection) and demonstrate two applications: (1) a zero-shot motion transfer method — implemented with VideoCrafter2 and WAN 2.1 — that is 10x more efficient than existing approaches, and (2) a training-free technique for consistent multi-shot video generation, where characters maintain identity across multiple video shots while Q-injection enhances motion fidelity.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
