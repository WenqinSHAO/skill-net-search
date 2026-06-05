---
id: neurips-0023
title: "Generalizable One-shot 3D Neural Head Avatar"
conference: NeurIPS 2023
date: 2023-12
authors:
  - name: "Xueting Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Umar Iqbal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/lpr/one-shot-avatar/"
  - name: "Code"
    url: "https://github.com/NVlabs/GOHA"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2306.08768"
abstract: "We present a method that reconstructs and animates a 3D head avatar from a single-view portrait image. Existing methods either involve time-consuming optimization for a specific person with multiple images, or they struggle to synthesize intricate appearance details beyond the facial region. To addr"
url: "https://research.nvidia.com/publication/2023-12_generalizable-one-shot-3d-neural-head-avatar"
status: new
---

# Generalizable One-shot 3D Neural Head Avatar

## 摘要

We present a method that reconstructs and animates a 3D head avatar from a single-view portrait image. Existing methods either involve time-consuming optimization for a specific person with multiple images, or they struggle to synthesize intricate appearance details beyond the facial region. To address these limitations, we propose a framework that not only generalizes to unseen identities based on a single-view image without requiring person-specific optimization, but also captures characteristic details within and beyond the face area (e.g. hairstyle, accessories, etc.). At the core of our method are three branches that produce three tri-planes representing the coarse 3D geometry, detailed appearance of a source image, as well as the expression of a target image. By applying volumetric rendering to the combination of the three tri-planes followed by a super-resolution module, our method yields a high fidelity image of the desired identity, expression and pose. Once trained, our model enables efficient 3D head avatar reconstruction and animation via a single forward pass through a network. Experiments show that the proposed approach generalizes well to unseen validation datasets, surpassing SOTA baseline methods by a large margin on head avatar reconstruction and animation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
