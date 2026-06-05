---
id: cvpr-0048
title: "GroupViT: Semantic Segmentation Emerges from Text Supervision"
conference: CVPR 2022
date: 2022-06
authors:
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Breuel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiarui Xu"
    affiliation: ""
    is_industry: false
  - name: "Xiaolong Wang"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Code"
    url: "https://github.com/NVlabs/GroupViT"
  - name: "Hugging Face Demo"
    url: "https://huggingface.co/spaces/xvjiarui/GroupViT"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2202.11094"
  - name: "Jiarui Xu&#039;s Project Page"
    url: "https://jerryxu.net/GroupViT/"
abstract: "Grouping and recognition are important components of visual scene understanding, e.g., for object detection and semantic segmentation. With end-to-end deep learning systems, grouping of image regions usually happens implicitly via top-down supervision from pixel-level recognition labels. Instead, in"
url: "https://research.nvidia.com/publication/2022-06_groupvit-semantic-segmentation-emerges-text-supervision"
status: new
---

# GroupViT: Semantic Segmentation Emerges from Text Supervision

## 摘要

Grouping and recognition are important components of visual scene understanding, e.g., for object detection and semantic segmentation. With end-to-end deep learning systems, grouping of image regions usually happens implicitly via top-down supervision from pixel-level recognition labels. Instead, in this paper, we propose to bring back the grouping mechanism into deep networks, which allows semantic segments to emerge automatically with only text supervision. We propose a hierarchical Grouping Vision Transformer (GroupViT), which goes beyond the regular grid structure representation and learns to group image regions into progressively larger arbitrary-shaped segments. We train GroupViT jointly with a text encoder on a large-scale image-text dataset via contrastive losses. With only text supervision and without any pixel-level annotations, GroupViT learns to group together semantic regions and successfully transfers to the task of semantic segmentation in a zero-shot manner, i.e., without any further fine-tuning. It achieves a zero-shot accuracy of 52.3% mIoU on the PASCAL VOC 2012 and 22.4% mIoU on PASCAL Context datasets, and performs competitively to state-of-the-art transfer-learning methods requiring greater levels of supervision. We open-source our code at https://github.com/NVlabs/GroupViT.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
