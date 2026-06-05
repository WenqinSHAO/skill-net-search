---
id: arxiv-2570
title: "Semantic Prompt Learning for Weakly-Supervised Semantic Segmentation"
conference: arXiv 2025
date: 2025-02
authors:
  - name: "Frank Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ci-Siang Lin"
    affiliation: ""
    is_industry: false
  - name: "Chien-Yi Wang"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Natural Language Processing"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2401.11791"
  - name: "Code"
    url: "https://github.com/NVlabs/SemPLeS"
  - name: "Project page"
    url: "https://projectdisr.github.io/semples/"
abstract: "Weakly-Supervised Semantic Segmentation (WSSS) aims to train segmentation models using image data with only image-level supervision. Since precise pixel-level annotations are not accessible, existing methods typically focus on producing pseudo masks for training segmentation models by refining CAM-l"
url: "https://research.nvidia.com/publication/2025-02_semantic-prompt-learning-weakly-supervised-semantic-segmentation"
status: new
---

# Semantic Prompt Learning for Weakly-Supervised Semantic Segmentation

## 摘要

Weakly-Supervised Semantic Segmentation (WSSS) aims to train segmentation models using image data with only image-level supervision. Since precise pixel-level annotations are not accessible, existing methods typically focus on producing pseudo masks for training segmentation models by refining CAM-like heatmaps. However, the produced heatmaps may capture only the discriminative image regions of object categories or the associated co-occurring backgrounds. To address the issues, we propose a Semantic Prompt Learning for WSSS (SemPLeS) framework, which learns to effectively prompt the CLIP latent space to enhance the semantic alignment between the segmented regions and the target object categories. More specifically, we propose Contrastive Prompt Learning and Prompt-guided Semantic Refinement to learn the prompts that adequately describe and suppress the co-occurring backgrounds associated with each object category. In this way, SemPLeS can perform better semantic alignment between object regions and class labels, resulting in desired pseudo masks for training segmentation models. The proposed SemPLeS framework achieves competitive performance on standard WSSS benchmarks, PASCAL VOC 2012 and MS COCO 2014, and shows compatibility with other WSSS methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
