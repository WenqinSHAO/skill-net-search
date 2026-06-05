---
id: neurips-0006
title: "RaySt3R: Predicting Novel Depth Maps for Zero-Shot Object Completion"
conference: NeurIPS 2025
date: 2025-12
authors:
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bardienus P. Duisterhof"
    affiliation: ""
    is_industry: false
  - name: "Jan Oberst"
    affiliation: ""
    is_industry: false
  - name: "Deva Ramanan"
    affiliation: ""
    is_industry: false
  - name: "Jeffrey Ichnowski"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "paper"
    url: "https://arxiv.org/abs/2506.05285"
  - name: "website"
    url: "https://rayst3r.github.io/"
abstract: "3D shape completion has broad applications in robotics, digital twin reconstruction, and extended reality (XR). Although recent advances in 3D object and scene completion have achieved impressive results, existing methods lack 3D consistency, are computationally expensive, and struggle to capture sh"
url: "https://research.nvidia.com/publication/2025-12_rayst3r-predicting-novel-depth-maps-zero-shot-object-completion"
status: new
---

# RaySt3R: Predicting Novel Depth Maps for Zero-Shot Object Completion

## 摘要

3D shape completion has broad applications in robotics, digital twin reconstruction, and extended reality (XR). Although recent advances in 3D object and scene completion have achieved impressive results, existing methods lack 3D consistency, are computationally expensive, and struggle to capture sharp object boundaries. Our work (RaySt3R) addresses these limitations by recasting 3D shape completion as a novel view synthesis problem. Specifically, given a single RGB-D image and a novel viewpoint (encoded as a collection of query rays), we train a feedforward transformer to predict depth maps, object masks, and per-pixel confidence scores for those query rays. RaySt3R fuses these predictions across multiple query views to reconstruct complete 3D shapes. We evaluate RaySt3R on synthetic and real-world datasets, and observe it achieves state-of-the-art performance, outperforming the baselines on all datasets by up to 44% in 3D chamfer distance.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
