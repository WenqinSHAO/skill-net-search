---
id: neurips-0016
title: "QUEEN: QUantized Efficient ENcoding for Streaming Free-viewpoint Videos"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Tianye Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Amrita Mazumdar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Luebke"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sharath Girish"
    affiliation: ""
    is_industry: false
  - name: "Abhinav Shrivastava"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - Robotics_autonomous
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Physical AI"
  - "World Simulation"
external_links:
  - name: "Code"
    url: "https://github.com/nvlabs/queen"
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/amri/projects/queen/"
  - name: "Video"
    url: "https://research.nvidia.com/labs/amri/projects/queen/media/videos/neurips_2024_queen_supp_video.mp4"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2412.04469"
abstract: "Online free-viewpoint video (FVV) streaming is a challenging problem, which is relatively under-explored. It requires incremental on-the-fly updates to a volumetric representation, fast training and rendering to satisfy realtime constraints and a small memory footprint for efficient transmission. If"
url: "https://research.nvidia.com/publication/2024-12_queen-quantized-efficient-encoding-streaming-free-viewpoint-videos"
status: new
---

# QUEEN: QUantized Efficient ENcoding for Streaming Free-viewpoint Videos

## 摘要

Online free-viewpoint video (FVV) streaming is a challenging problem, which is relatively under-explored. It requires incremental on-the-fly updates to a volumetric representation, fast training and rendering to satisfy realtime constraints and a small memory footprint for efficient transmission. If acheived, it can enhance user experience by enabling novel applications, e.g., 3D video conferencing and live volumetric video broadcast, among others. In this work, we propose a novel framework for QUantized and Efficient ENcoding (QUEEN) for streaming FVV using 3D Gaussian Splatting (3D-GS). QUEEN directly learns Gaussian attribute residuals between consecutive frames at each time-step without imposing any structural constraints on them, allowing for high quality reconstruction and generalizability. To efficiently store the residuals, we further propose a quantization-sparsity framework, which contains a learned latent-decoder for effectively quantizing attribute residuals other than Gaussian positions and a learned gating module to sparsify position residuals. We propose to use the Gaussian viewspace gradient difference vector as a signal to separate the static and dynamic content of the scene. It acts as a guide for effective sparsity learning and speeds up training. On diverse FVV benchmarks, QUEEN outperforms the state-of-the-art online FVV methods on all metrics. Notably, for several highly dynamic scenes, it reduces the model size to just 0.7 MB per frame while training in under 5 sec and rendering at ~350 FPS.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
