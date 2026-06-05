---
id: eccv-0004
title: "LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis"
conference: ECCV 2024
date: 2024-03
authors:
  - name: "Kevin Xie"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Lorraine"
    affiliation: ""
    is_industry: false
  - name: "Tianshi Cao"
    affiliation: ""
    is_industry: false
  - name: "Jun Gao"
    affiliation: ""
    is_industry: false
  - name: "James Lucas"
    affiliation: ""
    is_industry: false
  - name: "Antonio Torralba"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
  - name: "Xiaohui Zeng"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2403.15385"
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/LATTE3D/"
  - name: "30 Second Summary Video"
    url: "https://drive.google.com/file/d/12QkEj_PBBPTqSmiz0bkTbJIt_Ga4fR88/view?usp=drive_link"
  - name: "3 Minute Summary Video"
    url: "https://drive.google.com/file/d/1xUbWTk92NJ9ThQibmNs6LvOnkj47za7-/view?usp=drive_link"
abstract: "Recent text-to-3D generation approaches produce impressive 3D results but require time-consuming optimization that can take up to an hour per prompt. Amortized methods like ATT3D optimize multiple prompts simultaneously to improve efficiency, enabling fast text-to-3D synthesis. However, ATT3D cannot"
url: "https://research.nvidia.com/publication/2024-03_latte3d-large-scale-amortized-text-enhanced3d-synthesis"
status: new
---

# LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis

## 摘要

Recent text-to-3D generation approaches produce impressive 3D results but require time-consuming optimization that can take up to an hour per prompt. Amortized methods like ATT3D optimize multiple prompts simultaneously to improve efficiency, enabling fast text-to-3D synthesis. However, ATT3D cannot capture high-frequency geometry and texture details and struggles to scale to large prompt sets, so it generalizes poorly. We introduce Latte3D, addressing these limitations to achieve fast, high-quality generation on a significantly larger prompt set. Key to our method is 1) building a scalable architecture for amortized learning and 2) leveraging 3D data during optimization through 3D-aware diffusion priors, shape regularization, and model initialization to achieve robustness to diverse and complex training prompts. Latte3D amortizes both neural field generation and textured surface generation to produce highly detailed textured meshes in a single forward pass. Latte3D generates 3D objects in 400ms, and can be further enhanced with fast test-time optimization.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
