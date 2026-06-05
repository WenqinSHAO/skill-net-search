---
id: arxiv-2931
title: "Online Adaptation for Consistent Mesh Reconstruction in the Wild"
conference: arXiv 2020
date: 2020-12
authors:
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xueting Li"
    affiliation: ""
    is_industry: false
  - name: "Kihwan Kim"
    affiliation: ""
    is_industry: false
  - name: "Xiaolong Wang"
    affiliation: ""
    is_industry: false
  - name: "Ming-Hsuan Yang"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://sites.google.com/nvidia.com/vmr-2020"
  - name: "arXiv"
    url: "https://arxiv.org/abs/2012.03196"
abstract: "This paper presents an algorithm to reconstruct temporally consistent 3D meshes of deformable object instances from videos in the wild. Without requiring annotations of 3D mesh, 2D keypoints, or camera pose for each video frame, we pose video-based reconstruction as a self-supervised online adaptati"
url: "https://research.nvidia.com/publication/2020-12_online-adaptation-consistent-mesh-reconstruction-wild"
status: new
---

# Online Adaptation for Consistent Mesh Reconstruction in the Wild

## 摘要

This paper presents an algorithm to reconstruct temporally consistent 3D meshes of deformable object instances from videos in the wild. Without requiring annotations of 3D mesh, 2D keypoints, or camera pose for each video frame, we pose video-based reconstruction as a self-supervised online adaptation problem applied to any incoming test video. We first learn a category-specific 3D reconstruction model from a collection of single-view images of the same category that jointly predicts the shape, texture, and camera pose of an image. Then, at inference time, we adapt the model to a test video over time using self-supervised regularization terms that exploit temporal consistency of an object instance to enforce that all reconstructed meshes share a common texture map, a base shape, as well as parts. We demonstrate that our algorithm recovers temporally consistent and reliable 3D structures from videos of non-rigid objects including those of animals captured in the wild -- an extremely challenging task rarely addressed before.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
