---
id: cvpr-0041
title: "Magic3D: High-Resolution Text-to-3D Content Creation"
conference: CVPR 2023
date: 2023-06
authors:
  - name: "Chen-Hsuan Lin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ming-Yu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tsung-Yi Lin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jun Gao"
    affiliation: ""
    is_industry: false
  - name: "Luming Tang"
    affiliation: ""
    is_industry: false
  - name: "Towaki Takikawa"
    affiliation: ""
    is_industry: false
  - name: "Xiaohui Zeng"
    affiliation: ""
    is_industry: false
  - name: "Xun Huang"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/dir/magic3d"
abstract: "DreamFusion has recently demonstrated the utility of a pre-trained text-to-image diffusion model to optimize Neural Radiance Fields (NeRF), achieving remarkable text-to-3D synthesis results. However, the method has two inherent limitations: (a) extremely slow optimization of NeRF and (b) low-resolut"
url: "https://research.nvidia.com/publication/2023-06_magic3d-high-resolution-text-3d-content-creation"
status: new
---

# Magic3D: High-Resolution Text-to-3D Content Creation

## 摘要

DreamFusion has recently demonstrated the utility of a pre-trained text-to-image diffusion model to optimize Neural Radiance Fields (NeRF), achieving remarkable text-to-3D synthesis results. However, the method has two inherent limitations: (a) extremely slow optimization of NeRF and (b) low-resolution image space supervision on NeRF, leading to low-quality 3D models with a long processing time. In this paper, we address these limitations by utilizing a two-stage optimization framework. First, we obtain a coarse model using a low-resolution diffusion prior and accelerate with a sparse 3D hash grid structure. Using the coarse representation as the initialization, we further optimize a textured 3D mesh model with an efficient differentiable renderer interacting with a high-resolution latent diffusion model. Our method, dubbed Magic3D, can create high quality 3D mesh models in 40 minutes, which is 2× faster than DreamFusion (reportedly taking 1.5 hours on average), while also achieving higher resolution. User studies show 61.7% raters to prefer our approach over DreamFusion. Together with the image-conditioned generation capabilities, we provide users with new ways to control 3D synthesis, opening up new avenues to various creative applications.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
