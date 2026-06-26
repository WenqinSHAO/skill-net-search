---
id: "iccv-0007"
title: "ATT3D: Amortized Text-To-3D Object Synthesis"
conference: "ICCV 2023"
date: "2023-10"
authors:
  - name: "Jonathan Lorraine"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kevin Xie"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xiaohui Zeng"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chen-Hsuan Lin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Towaki Takikawa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nicholas Sharp"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tsung-Yi Lin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ming-Yu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "James Lucas"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/ATT3D/"
  - name: "Paper"
    url: "https://arxiv.org/abs//2306.07349"
abstract: "Text-to-3D modeling has seen exciting progress by combining generative text-to-image models with image-to-3D methods like Neural Radiance Fields. DreamFusion recently achieved high-quality results but requires a lengthy, per-prompt optimization to create 3D objects. To address this, we amortize opti"
url: "https://research.nvidia.com/publication/2023-10_att3d-amortized-text-3d-object-synthesis"
status: "new"
---

# ATT3D: Amortized Text-To-3D Object Synthesis

## 摘要

Text-to-3D modeling has seen exciting progress by combining generative text-to-image models with image-to-3D methods like Neural Radiance Fields. DreamFusion recently achieved high-quality results but requires a lengthy, per-prompt optimization to create 3D objects. To address this, we amortize optimization over text prompts by training on many prompts simultaneously with a unified model, instead of separately. With this, we share computation across a prompt set, training in less time than per-prompt optimization. Our framework - Amortized Text-to-3D (ATT3D) - enables sharing of knowledge between prompts to generalize to unseen setups and smooth interpolations between text for novel assets and simple animations.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
