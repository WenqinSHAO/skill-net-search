---
id: "siggraph-0025"
title: "Consolidating Attention Features for Multi-view Image Editing"
conference: "SIGGRAPH 2024"
date: "2024-02"
authors:
  - name: "Or Patashnik"
    affiliation: "Tel Aviv University"
    is_industry: false
  - name: "Rinon Gal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Cohen-Or"
    affiliation: "Tel Aviv University"
    is_industry: false
  - name: "Jun-Yan Zhu"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Fernando De la Torre"
    affiliation: "Carnegie Mellon University"
    is_industry: false
topics:
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
abstract: "Large-scale text-to-image models enable a wide range of image editing techniques, using text prompts or even spatial controls. However, applying these editing methods to multi-view images depicting a single scene leads to 3D-inconsistent results. In this work, we focus on spatial control-based geome"
url: "https://research.nvidia.com/publication/2024-02_consolidating-attention-features-multi-view-image-editing"
status: "new"
---

# Consolidating Attention Features for Multi-view Image Editing

## 摘要

Large-scale text-to-image models enable a wide range of image editing techniques, using text prompts or even spatial controls. However, applying these editing methods to multi-view images depicting a single scene leads to 3D-inconsistent results. In this work, we focus on spatial control-based geometric manipulations and introduce a method to consolidate the editing process across various views. We build on two insights: (1) maintaining consistent features throughout the generative process helps attain consistency in multi-view editing, and (2) the queries in self-attention layers significantly influence the image structure. Hence, we propose to improve the geometric consistency of the edited images by enforcing the consistency of the queries. To do so, we introduce QNeRF, a neural radiance field trained on the internal query features of the edited images. Once trained, QNeRF can render 3D-consistent queries, which are then softly injected back into the self-attention layers during generation, greatly improving multi-view consistency. We refine the process through a progressive, iterative method that better consolidates queries across the diffusion timesteps. We compare our method to a range of existing techniques and demonstrate that it can achieve better multi-view consistency and higher fidelity to the input scene. These advantages allow us to train NeRFs with fewer visual artifacts, that are better aligned with the target geometry.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
