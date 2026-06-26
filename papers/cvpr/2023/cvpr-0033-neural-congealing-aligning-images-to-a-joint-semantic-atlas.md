---
id: "cvpr-0033"
title: "Neural Congealing: Aligning Images to a Joint Semantic Atlas"
conference: "CVPR 2023"
date: "2023-06"
authors:
  - name: "Dolev Ofri-Amar"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Michal Geyer"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Yoni Kasten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tali Dekel"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://neural-congealing.github.io/"
abstract: "We present Neural Congealing -- a zero-shot self-supervised framework for detecting and jointly aligning semantically-common content across a given set of images. Our approach harnesses the power of pre-trained DINO-ViT features to learn: (i) a joint semantic atlas -- a 2D grid that captures the mod"
url: "https://research.nvidia.com/publication/2023-06_neural-congealing-aligning-images-joint-semantic-atlas"
status: "new"
---

# Neural Congealing: Aligning Images to a Joint Semantic Atlas

## 摘要

We present Neural Congealing -- a zero-shot self-supervised framework for detecting and jointly aligning semantically-common content across a given set of images. Our approach harnesses the power of pre-trained DINO-ViT features to learn: (i) a joint semantic atlas -- a 2D grid that captures the mode of DINO-ViT features in the input set, and (ii) dense mappings from the unified atlas to each of the input images. We derive a new robust self-supervised framework that optimizes the atlas representation and mappings per image set, requiring only a few real-world images as input without any additional input information (e.g., segmentation masks). Notably, we design our losses and training paradigm to account only for the shared content under severe variations in appearance, pose, background clutter or other distracting objects. We demonstrate results on a plethora of challenging image sets including sets of mixed domains (e.g., aligning images depicting sculpture and artwork of cats), sets depicting related yet different object categories (e.g., dogs and tigers), or domains for which large-scale training data is scarce (e.g., coffee mugs). We thoroughly evaluate our method and show that our test-time optimization approach performs favorably compared to a state-of-the-art method that requires extensive training on large-scale datasets.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
