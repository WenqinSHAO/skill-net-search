---
id: "siggraph-0031"
title: "Domain-Agnostic Tuning-Encoder for Fast Personalization of Text-To-Image Models"
conference: "SIGGRAPH 2023"
date: "2023-12"
authors:
  - name: "Moab Arar"
    affiliation: "Tel-Aviv University"
    is_industry: false
  - name: "Rinon Gal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Cohen-Or"
    affiliation: "Tel-Aviv University"
    is_industry: false
  - name: "Ariel Shamir"
    affiliation: "Reichman University"
    is_industry: false
  - name: "Amit Bermano"
    affiliation: "Tel-Aviv University"
    is_industry: false
topics:
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2307.06925"
abstract: "Text-to-image (T2I) personalization allows users to guide the creative image generation process by combining their own visual concepts in natural language prompts. Recently, encoder-based techniques have emerged as a new effective approach for T2I personalization, reducing the need for multiple imag"
url: "https://research.nvidia.com/publication/2023-12_domain-agnostic-tuning-encoder-fast-personalization-text-image-models"
status: "new"
---

# Domain-Agnostic Tuning-Encoder for Fast Personalization of Text-To-Image Models

## 摘要

Text-to-image (T2I) personalization allows users to guide the creative image generation process by combining their own visual concepts in natural language prompts. Recently, encoder-based techniques have emerged as a new effective approach for T2I personalization, reducing the need for multiple images and long training times. However, most existing encoders are limited to a single-class domain, which hinders their ability to handle diverse concepts. In this work, we propose a domain-agnostic method that does not require any specialized dataset or prior information about the personalized concepts. We introduce a novel contrastive-based regularization technique to maintain high fidelity to the target concept characteristics while keeping the predicted embeddings close to editable regions of the latent space, by pushing the predicted tokens toward their nearest existing CLIP tokens. Our experimental results demonstrate the effectiveness of our approach and show how the learned tokens are more semantic than tokens predicted by unregularized models. This leads to a better representation that achieves state-of-the-art performance while being more flexible than previous methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
