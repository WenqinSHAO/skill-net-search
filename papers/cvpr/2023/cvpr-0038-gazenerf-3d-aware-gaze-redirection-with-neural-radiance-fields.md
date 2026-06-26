---
id: "cvpr-0038"
title: "GazeNeRF: 3D-Aware Gaze Redirection with Neural Radiance Fields"
conference: "CVPR 2023"
date: "2023-06"
authors:
  - name: "Alessandro Ruzzi"
    affiliation: "ETH Zürich"
    is_industry: false
  - name: "Xiangwei Shi"
    affiliation: "Delft University of Technology"
    is_industry: false
  - name: "Xi Wang"
    affiliation: "ETH Zürich"
    is_industry: false
  - name: "Gengyan Li"
    affiliation: "ETH Zürich"
    is_industry: false
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hyung Jin Chang"
    affiliation: "University of Birmingham"
    is_industry: false
  - name: "Xucong Zhang"
    affiliation: "Delft University of Technology"
    is_industry: false
  - name: "Otmar Hilliges"
    affiliation: "ETH Zürich"
    is_industry: false
topics:
  - Applied_perception
  - Computer Vision
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Human Computer Interaction"
  - "VR, AR and Display Technology"
external_links:
  - name: "Project Page"
    url: "https://x-shi.github.io/GazeNeRF.github.io/"
  - name: "Code"
    url: "https://github.com/AlessandroRuzzi/GazeNeRF"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2212.04823"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=JwqKbmUR3DE"
abstract: "We propose GazeNeRF, a 3D-aware method for the task of gaze redirection. Existing gaze redirection methods operate on 2D images and struggle to generate 3D consistent results. Instead, we build on the intuition that the face region and eye balls are separate 3D structures that move in a coordinated "
url: "https://research.nvidia.com/publication/2023-06_gazenerf-3d-aware-gaze-redirection-neural-radiance-fields"
status: "new"
---

# GazeNeRF: 3D-Aware Gaze Redirection with Neural Radiance Fields

## 摘要

We propose GazeNeRF, a 3D-aware method for the task of gaze redirection. Existing gaze redirection methods operate on 2D images and struggle to generate 3D consistent results. Instead, we build on the intuition that the face region and eye balls are separate 3D structures that move in a coordinated yet independent fashion. Our method leverages recent advancements in conditional image-based neural radiance fields and proposes a two-branch architecture that predicts volumetric features for the face and eye regions separately. Rigidly transforming the eye features via a 3D rotation matrix provides fine-grained control over the desired gaze angle. The final, redirected image is then attained via differentiable volume compositing. Our experiments show that this architecture outperforms naively conditioned NeRF baselines as well as previous state-of-the-art 2D gaze redirection methods in terms of redirection accuracy and identity preservation. Code and models will be released for research purposes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
