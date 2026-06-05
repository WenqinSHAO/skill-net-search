---
id: arxiv-3040
title: "Neurreg: Neural registration and its application to image segmentation"
conference: arXiv 2020
date: 2020-03
authors:
  - name: "Andriy Myronenko"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ziyue Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wenqi Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Holger Roth"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daguang Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wentao Zhu"
    affiliation: ""
    is_industry: false
  - name: "Yufang Huang"
    affiliation: ""
    is_industry: false
  - name: "Fausto Milletari"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Medical_imaging
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Medical"
abstract: "Registration is a fundamental task in medical image analysis which can be applied to several tasks including image segmentation, intra-operative tracking, multi-modal image alignment, and motion analysis. Popular registration tools such as ANTs and NiftyReg optimize an objective function for each pa"
url: "https://research.nvidia.com/publication/2020-03_neurreg-neural-registration-and-its-application-image-segmentation"
status: new
---

# Neurreg: Neural registration and its application to image segmentation

## 摘要

Registration is a fundamental task in medical image analysis which can be applied to several tasks including image segmentation, intra-operative tracking, multi-modal image alignment, and motion analysis. Popular registration tools such as ANTs and NiftyReg optimize an objective function for each pair of images from scratch which is time-consuming for large images with complicated deformation. Facilitated by the rapid progress of deep learning, learning-based approaches such as VoxelMorph have been emerging for image registration. These approaches can achieve competitive performance in a fraction of a second on advanced GPUs. In this work, we construct a neural registration framework, called NeurReg, with a hybrid loss of displacement fields and data similarity, which substantially improves the current state-of-the-art of registrations. Within the framework, we simulate various transformations by a registration simulator which generates fixed image and displacement field ground truth for training. Furthermore, we design three segmentation frameworks based on the proposed registration framework: 1) atlas-based segmentation, 2) joint learning of both segmentation and registration tasks, and 3) multi-task learning with atlas based segmentation as an intermediate feature. Extensive experimental results validate the effectiveness of the proposed NeurReg framework based on various metrics: the endpoint error (EPE) of the predicted displacement field, mean square error (MSE), normalized local cross-correlation (NLCC), mutual information (MI), Dice coefficient, uncertainty estimation, and the interpretability of the segmentation. The proposed NeurReg improves registration accuracy with fast inference speed, which can greatly accelerate related medical image analysis tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
