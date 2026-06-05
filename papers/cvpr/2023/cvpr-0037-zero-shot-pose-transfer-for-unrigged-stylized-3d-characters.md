---
id: cvpr-0037
title: "Zero-shot Pose Transfer for Unrigged Stylized 3D Characters"
conference: CVPR 2023
date: 2023-06
authors:
  - name: "Xueting Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiashun Wang"
    affiliation: ""
    is_industry: false
  - name: "Orazio Gallo"
    affiliation: ""
    is_industry: false
  - name: "Xiaolong Wang"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
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
  - "Human Computer Interaction"
external_links:
  - name: "Project Page"
    url: "https://jiashunwang.github.io/ZPT/"
  - name: "ArXIv"
    url: "https://arxiv.org/abs/2306.00200"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=ynT65hp92SE"
abstract: "Transferring the pose of a reference avatar to stylized 3D characters of various shapes is a fundamental task in computer graphics. Existing methods either require the stylized characters to be rigged, or they use the stylized character in the desired pose as ground truth at training. We present a z"
url: "https://research.nvidia.com/publication/2023-06_zero-shot-pose-transfer-unrigged-stylized-3d-characters"
status: new
---

# Zero-shot Pose Transfer for Unrigged Stylized 3D Characters

## 摘要

Transferring the pose of a reference avatar to stylized 3D characters of various shapes is a fundamental task in computer graphics. Existing methods either require the stylized characters to be rigged, or they use the stylized character in the desired pose as ground truth at training. We present a zero-shot approach that requires only the widely available deformed non-stylized avatars in training, and deforms stylized characters of significantly different shapes at inference. Classical methods achieve strong generalization by deforming the mesh at the triangle level, but this requires labelled correspondences. We leverage the power of local deformation, but without requiring explicit correspondence labels. We introduce a semi-supervised shape-understanding module to bypass the need for explicit correspondences at test time, and an implicit pose deformation module that deforms individual surface points to match the target pose. Furthermore, to encourage realistic and accurate deformation of stylized characters, we introduce an efficient volume-based test-time training procedure. Because it does not need rigging, nor the deformed stylized character at training time, our model generalizes to categories with scarce annotation, such as stylized quadrupeds. Extensive experiments demonstrate the effectiveness of the proposed method compared to the state-of-the-art approaches trained with comparable or more supervision. Our project page is available at https://jiashunwang.github.io/ZPT.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
