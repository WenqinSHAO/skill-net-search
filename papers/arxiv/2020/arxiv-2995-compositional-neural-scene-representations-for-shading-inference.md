---
id: arxiv-2995
title: "Compositional Neural Scene Representations for Shading Inference"
conference: arXiv 2020
date: 2020-07
authors:
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Granskog"
    affiliation: ""
    is_industry: false
  - name: "Marios Papas"
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
  - name: "Code"
    url: "https://github.com/jonathangranskog/shading-scene-representations"
abstract: "We present a technique for adaptively partitioning neural scene representations. Our method disentangles lighting, material, and geometric information yielding a scene representation that preserves the orthogonality of these components, improves interpretability of the model, and allows compositing "
url: "https://research.nvidia.com/publication/2020-07_compositional-neural-scene-representations-shading-inference"
status: new
---

# Compositional Neural Scene Representations for Shading Inference

## 摘要

We present a technique for adaptively partitioning neural scene representations. Our method disentangles lighting, material, and geometric information yielding a scene representation that preserves the orthogonality of these components, improves interpretability of the model, and allows compositing new scenes by mixing components of existing ones. The proposed adaptive partitioning respects the uneven entropy of individual components and permits compressing the scene representation to lower its memory footprint and potentially reduce the evaluation cost of the model. Furthermore, the partitioned representation enables an in-depth analysis of existing image generators. We compare the flow of information through individual partitions, and by contrasting it to the impact of additional inputs (G-buffer), we are able to identify the roots of undesired visual artifacts, and propose one possible solution to remedy the poor performance. We also demonstrate the benefits of complementing traditional forward renderers by neural representations and synthesis, e.g. to infer expensive shading effects, and show how these could improve production rendering in the future if developed further.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
