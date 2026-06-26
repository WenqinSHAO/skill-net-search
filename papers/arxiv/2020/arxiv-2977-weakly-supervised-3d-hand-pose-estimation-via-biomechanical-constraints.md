---
id: "arxiv-2977"
title: "Weakly-Supervised 3D Hand Pose Estimation via Biomechanical Constraints"
conference: "arXiv 2020"
date: "2020-08"
authors:
  - name: "Adrian Spurr"
    affiliation: "ETH Zurich"
    is_industry: false
  - name: "Umar Iqbal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Otmar Hilliges"
    affiliation: "ETH Zurich"
    is_industry: false
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Applied_perception
  - Computer Vision
  - Graphics_rendering
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Human Computer Interaction"
  - "Robotics"
  - "VR, AR and Display Technology"
external_links:
  - name: "ArXiv"
    url: "https://arxiv.org/pdf/2003.09282.pdf"
abstract: "Estimating 3D hand pose from 2D images is a difficult, inverse problem due to the inherent scale and depth ambiguities. Current stateof-the-art methods train fully supervised deep neural networks with 3D ground-truth data. However, acquiring 3D annotations is expensive, typically requiring calibrate"
url: "https://research.nvidia.com/publication/2020-08_weakly-supervised-3d-hand-pose-estimation-biomechanical-constraints"
status: "new"
---

# Weakly-Supervised 3D Hand Pose Estimation via Biomechanical Constraints

## 摘要

Estimating 3D hand pose from 2D images is a difficult, inverse problem due to the inherent scale and depth ambiguities. Current stateof-the-art methods train fully supervised deep neural networks with 3D ground-truth data. However, acquiring 3D annotations is expensive, typically requiring calibrated multi-view setups or labour intensive manual annotations. While annotations of 2D keypoints are much easier to obtain, how to efficiently leverage such weakly-supervised data to improve the task of 3D hand pose prediction remains an important open question. The key difficulty stems from the fact that direct application of additional 2D supervision mostly benefits the 2D proxy objective but does little to alleviate the depth and scale ambiguities. Embracing this challenge we propose a set of novel losses that constrain the prediction of a neural network to lie within the range of biomechanically feasible 3D hand configurations. We show by extensive experiments that our proposed constraints significantly reduce the depth ambiguity and allow the network to more effectively leverage additional 2D annotated images. For example, on the challenging freiHAND dataset, using additional 2D annotation without our proposed biomechanical constraints reduces the depth error by only 15%, whereas the error is reduced significantly by 50% when the proposed biomechanical constraints are used.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
