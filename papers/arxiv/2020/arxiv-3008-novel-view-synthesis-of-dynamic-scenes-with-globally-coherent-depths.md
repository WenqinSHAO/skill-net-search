---
id: arxiv-3008
title: "Novel View Synthesis of Dynamic Scenes with Globally Coherent Depths"
conference: arXiv 2020
date: 2020-06
authors:
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jae shin Yoon"
    affiliation: ""
    is_industry: false
  - name: "Kihwan Kim"
    affiliation: ""
    is_industry: false
  - name: "Orazio Gallo"
    affiliation: ""
    is_industry: false
  - name: "Hyunsoo Park"
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
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2004.01294"
  - name: "Video (youtube)"
    url: "https://www.youtube.com/watch?v=S8_0V3fZIes"
abstract: "This paper presents a new method to synthesize an image from the arbitrary view and time given a collection of images of a dynamic scene. A key challenge for the synthesis arises from dynamic scene reconstruction where epipolar geometry does not apply to the local motion of dynamic contents. Our ins"
url: "https://research.nvidia.com/publication/2020-06_novel-view-synthesis-dynamic-scenes-globally-coherent-depths"
status: new
---

# Novel View Synthesis of Dynamic Scenes with Globally Coherent Depths

## 摘要

This paper presents a new method to synthesize an image from the arbitrary view and time given a collection of images of a dynamic scene. A key challenge for the synthesis arises from dynamic scene reconstruction where epipolar geometry does not apply to the local motion of dynamic contents. Our insight is that although its scale and quality is inconsistent with other views, the depth estimation from a single view can be used to reason about the geometry of the local motion. We propose to combine the depths from single view (DSV) and a view invariant depth reconstructed from multi-view stereo (DMV). We cast this problem as learning to correct the scale of DSV estimates, and to refine each depth with locally consistent motions between views to form a coherent depth estimation. We integrate these tasks into a depth fusion network in a self-supervised fashion. With the fused depth maps, we synthesize a photorealistic virtual view in a specific location and time using our deep blending network that completes the scene and renders the virtual view. We evaluate our method in depth estimation and view synthesis on a diverse real-world dynamic scenes and show the outstanding performance over existing methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
