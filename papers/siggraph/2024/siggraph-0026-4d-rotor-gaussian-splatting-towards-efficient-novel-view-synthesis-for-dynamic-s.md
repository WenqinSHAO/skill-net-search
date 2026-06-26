---
id: "siggraph-0026"
title: "4D-Rotor Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes"
conference: "SIGGRAPH 2024"
date: "2024-02"
authors:
  - name: "Yuanxing Duan"
    affiliation: "Peking University"
    is_industry: false
  - name: "Fangyin Wei"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Qiyu Dai"
    affiliation: "Peking University, State Key Laboratory of General AI China"
    is_industry: false
  - name: "Yuhang He"
    affiliation: "Peking University"
    is_industry: false
  - name: "Wenzheng Chen"
    affiliation: "NVIDIA, Peking University"
    is_industry: true
  - name: "Baoquan Chen"
    affiliation: "Peking University, State Key Laboratory of General AI China"
    is_industry: false
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "We consider the problem of novel-view synthesis (NVS) for dynamic scenes. Recent neural approaches have accomplished exceptional NVS results for static 3D scenes, but extensions to 4D time-varying scenes remain non-trivial. Prior efforts often encode dynamics by learning a canonical space plus impli"
url: "https://research.nvidia.com/publication/2024-02_4d-rotor-gaussian-splatting-towards-efficient-novel-view-synthesis-dynamic"
status: "new"
---

# 4D-Rotor Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes

## 摘要

We consider the problem of novel-view synthesis (NVS) for dynamic scenes. Recent neural approaches have accomplished exceptional NVS results for static 3D scenes, but extensions to 4D time-varying scenes remain non-trivial. Prior efforts often encode dynamics by learning a canonical space plus implicit or explicit deformation fields, which struggle in challenging scenarios like sudden movements or generating high-fidelity renderings. In this paper, we introduce 4D Gaussian Splatting (4DRotorGS), a novel method that represents dynamic scenes with anisotropic 4D XYZT Gaussians, inspired by the success of 3D Gaussian Splatting in static scenes. We model dynamics at each timestamp by temporally slicing the 4D Gaussians, which naturally compose dynamic 3D Gaussians and can be seamlessly projected into images. As an explicit spatial-temporal representation, 4DRotorGS demonstrates powerful capabilities for modeling complicated dynamics and fine details--especially for scenes with abrupt motions. We further implement our temporal slicing and splatting techniques in a highly optimized CUDA acceleration framework, achieving real-time inference rendering speeds of up to 277 FPS on an RTX 3090 GPU and 583 FPS on an RTX 4090 GPU. Rigorous evaluations on scenes with diverse motions showcase the superior efficiency and effectiveness of 4DRotorGS, which consistently outperforms existing methods both quantitatively and qualitatively.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
