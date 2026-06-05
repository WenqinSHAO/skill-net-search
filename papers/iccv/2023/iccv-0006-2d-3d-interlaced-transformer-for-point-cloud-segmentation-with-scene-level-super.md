---
id: iccv-0006
title: "2D-3D Interlaced Transformer for Point Cloud Segmentation with Scene-Level Supervision"
conference: ICCV 2023
date: 2023-10
authors:
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Cheng-Kun Yang"
    affiliation: ""
    is_industry: false
  - name: "Yung-Yu Chaung"
    affiliation: ""
    is_industry: false
  - name: "Yen-Yu Lin"
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
  - name: "Project Website"
    url: "https://jimmy15923.github.io/mit_web/"
  - name: "arXiv"
    url: "https://arxiv.org/abs/2310.12817"
  - name: "Code"
    url: "https://github.com/jimmy15923/mit"
abstract: "We present a Multimodal Interlaced Transformer (MIT) that jointly considers 2D and 3D data for weakly supervised point cloud segmentation. Research studies have shown that 2D and 3D features are complementary for point cloud segmentation. However, existing methods require extra 2D annotations to ach"
url: "https://research.nvidia.com/publication/2023-10_2d-3d-interlaced-transformer-point-cloud-segmentation-scene-level-supervision"
status: new
---

# 2D-3D Interlaced Transformer for Point Cloud Segmentation with Scene-Level Supervision

## 摘要

We present a Multimodal Interlaced Transformer (MIT) that jointly considers 2D and 3D data for weakly supervised point cloud segmentation. Research studies have shown that 2D and 3D features are complementary for point cloud segmentation. However, existing methods require extra 2D annotations to achieve 2D-3D information fusion. Considering the high annotation cost of point clouds, effective 2D and 3D feature fusion based on weakly supervised learning is in great demand. To this end, we propose a transformer model with two encoders and one decoder for weakly supervised point cloud segmentation using only scene-level class tags. Specifically, the two encoders compute the self-attended features for 3D point clouds and 2D multi-view images, respectively. The decoder implements interlaced 2D-3D cross-attention and carries out implicit 2D and 3D feature fusion. We alternately switch the roles of queries and key-value pairs in the decoder layers. It turns out that the 2D and 3D features are iteratively enriched by each other. Experiments show that it performs favorably against existing weakly supervised point cloud segmentation methods by a large margin on the S3DIS and ScanNet benchmarks. The project page will be available at this https URL.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
