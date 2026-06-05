---
id: siggraph-0032
title: "Adaptive Shells for Efficient Neural Radiance Field Rendering"
conference: SIGGRAPH 2023
date: 2023-12
authors:
  - name: "Merlin Nimier-David"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zian Wang"
    affiliation: ""
    is_industry: false
  - name: "Tianchang Shen"
    affiliation: ""
    is_industry: false
  - name: "Nicholas Sharp"
    affiliation: ""
    is_industry: false
  - name: "Jun Gao"
    affiliation: ""
    is_industry: false
  - name: "Zan Gojcic"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
external_links:
  - name: "Project page"
    url: "https://research.nvidia.com/labs/toronto-ai/adaptive-shells/"
abstract: "Neural radiance fields achieve unprecedented quality for novel view synthesis, but their volumetric formulation remains expensive, requiring a huge number of samples to render high-resolution images. Volumetric encodings are essential to represent fuzzy geometry such as foliage and hair, and they ar"
url: "https://research.nvidia.com/publication/2023-12_adaptive-shells-efficient-neural-radiance-field-rendering"
status: new
---

# Adaptive Shells for Efficient Neural Radiance Field Rendering

## 摘要

Neural radiance fields achieve unprecedented quality for novel view synthesis, but their volumetric formulation remains expensive, requiring a huge number of samples to render high-resolution images. Volumetric encodings are essential to represent fuzzy geometry such as foliage and hair, and they are well-suited for stochastic optimization. Yet, many scenes ultimately consist largely of solid surfaces which can be accurately rendered by a single sample per pixel. Based on this insight, we propose a neural radiance formulation that smoothly transitions between volumetric- and surface-based rendering, greatly accelerating rendering speed and even improving visual fidelity. Our method constructs an explicit mesh envelope which spatially bounds a neural volumetric representation. In solid regions, the envelope nearly converges to a surface and can often be rendered with a single sample. To this end, we generalize the NeuS [Wang et al. 2021] formulation with a learned spatially-varying kernel size which encodes the spread of the density, fitting a wide kernel to volume-like regions and a tight kernel to surface-like regions. We then extract an explicit mesh of a narrow band around the surface, with width determined by the kernel size, and fine-tune the radiance field within this band. At inference time, we cast rays against the mesh and evaluate the radiance field only within the enclosed region, greatly reducing the number of samples required. Experiments show that our approach enables efficient rendering at very high fidelity. We also demonstrate that the extracted envelope enables downstream applications such as animation and simulation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
