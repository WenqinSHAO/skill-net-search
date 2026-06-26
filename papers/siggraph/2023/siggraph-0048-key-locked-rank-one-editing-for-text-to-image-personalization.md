---
id: "siggraph-0048"
title: "Key-Locked Rank One Editing for Text-to-Image Personalization"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Yoad Tewel"
    affiliation: "NVIDIA, Tel-Aviv University"
    is_industry: true
  - name: "Rinon Gal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2305.01644"
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/par/Perfusion/"
abstract: "Text-to-image models (T2I) offer a new level of flexibility by allowing users to guide the creative process through natural language. However, personalizing these models to align with user-provided visual concepts remains a challenging problem. The task of T2I personalization poses multiple hard cha"
url: "https://research.nvidia.com/publication/2023-08_key-locked-rank-one-editing-text-image-personalization"
status: "new"
---

# Key-Locked Rank One Editing for Text-to-Image Personalization

## 摘要

Text-to-image models (T2I) offer a new level of flexibility by allowing users to guide the creative process through natural language. However, personalizing these models to align with user-provided visual concepts remains a challenging problem. The task of T2I personalization poses multiple hard challenges, such as maintaining high visual fidelity while allowing creative control, combining multiple personalized concepts in a single image, and keeping a small model size. We present&nbsp;Perfusion, a T2I personalization method that addresses these challenges using dynamic rank-1 updates to the underlying T2I model. Perfusion avoids overfitting by introducing a new mechanism that "locks" new concepts' cross-attention Keys to their superordinate concept. Additionally, we develop a&nbsp;gated&nbsp;rank-1 approach that enables us to control the influence of a learned concept during inference time and to combine multiple concepts. This allows runtime efficient balancing of visual-fidelity and textual-alignment with a single 100KB trained model. Importantly, it can span different operating points across the Pareto front without additional training. We compare our approach to strong baselines and demonstrate its qualitative and quantitative strengths.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
