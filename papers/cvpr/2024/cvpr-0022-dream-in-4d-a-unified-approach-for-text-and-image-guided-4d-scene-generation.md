---
id: cvpr-0022
title: "Dream-in-4D: A Unified Approach for Text- and Image-guided 4D Scene Generation"
conference: CVPR 2024
date: 2024-06
authors:
  - name: "Xueting Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yufeng Zheng"
    affiliation: ""
    is_industry: false
  - name: "Otmar Hilliges"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "World Simulation"
external_links:
  - name: "Code"
    url: "https://github.com/NVlabs/dream-in-4d"
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/nxp/dream-in-4d/"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2311.16854"
abstract: "Large-scale diffusion generative models are greatly simplifying image, video and 3D asset creation from userprovided text prompts and images. However, the challenging problem of text-to-4D dynamic 3D scene generation with diffusion guidance remains largely unexplored. We propose Dream-in-4D, which f"
url: "https://research.nvidia.com/publication/2024-06_dream-4d-unified-approach-text-and-image-guided-4d-scene-generation"
status: new
---

# Dream-in-4D: A Unified Approach for Text- and Image-guided 4D Scene Generation

## 摘要

Large-scale diffusion generative models are greatly simplifying image, video and 3D asset creation from userprovided text prompts and images. However, the challenging problem of text-to-4D dynamic 3D scene generation with diffusion guidance remains largely unexplored. We propose Dream-in-4D, which features a novel two-stage approach for text-to-4D synthesis, leveraging (1) 3D and 2D diffusion guidance to effectively learn a high-quality static 3D asset in the first stage; (2) a deformable neural radiance field that explicitly disentangles the learned static asset from its deformation, preserving quality during motion learning; and (3) a multi-resolution feature grid for the deformation field with a displacement total variation loss to effectively learn motion with video diffusion guidance in the second stage. Through a user preference study, we demonstrate that our approach significantly advances image and motion quality, 3D consistency and text fidelity for text-to4D generation compared to baseline approaches. Thanks to its motion-disentangled representation, Dream-in-4D can also be easily adapted for controllable generation where appearance is defined by one or multiple images, without the need to modify the motion learning stage. Thus, our method offers, for the first time, a unified approach for textto-4D, image-to-4D and personalized 4D generation tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
