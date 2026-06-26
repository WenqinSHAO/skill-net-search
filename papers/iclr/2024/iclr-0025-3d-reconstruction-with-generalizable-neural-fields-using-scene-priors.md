---
id: "iclr-0025"
title: "3D Reconstruction with Generalizable Neural Fields using Scene Priors"
conference: "ICLR 2024"
date: "2024-05"
authors:
  - name: "Yang Fu"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xueting Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Amey Kulkarni"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xiaolong Wang"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Sifei Liu"
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
    url: "https://oasisyang.github.io/neural-prior/"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2309.15164v2"
  - name: "Video"
    url: "https://youtu.be/cqVzTk3U6e4"
abstract: "High-fidelity 3D scene reconstruction has been substantially advanced by recent progress in neural fields. However, most existing methods train a separate network from scratch for each individual scene. This is not scalable, inefficient, and unable to yield good results given limited views. While le"
url: "https://research.nvidia.com/publication/2024-05_3d-reconstruction-generalizable-neural-fields-using-scene-priors"
status: "new"
---

# 3D Reconstruction with Generalizable Neural Fields using Scene Priors

## 摘要

High-fidelity 3D scene reconstruction has been substantially advanced by recent progress in neural fields. However, most existing methods train a separate network from scratch for each individual scene. This is not scalable, inefficient, and unable to yield good results given limited views. While learning-based multi-view stereo methods alleviate this issue to some extent, their multi-view setting makes it less flexible to scale up and to broad applications. Instead, we introduce training generalizable Neural Fields incorporating scene Priors (NFPs). The NFP network maps any single-view RGB-D image into signed distance and radiance values. A complete scene can be reconstructed by merging individual frames in the volumetric space WITHOUT a fusion module, which provides better flexibility. The scene priors can be trained on large-scale datasets, allowing for fast adaptation to the reconstruction of a new scene with fewer views. NFP not only demonstrates SOTA scene reconstruction performance and efficiency, but it also supports single-image novel-view synthesis, which is under-explored in neural fields. More qualitative results are available at: https://oasisyang.github.io/neural-prior.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
