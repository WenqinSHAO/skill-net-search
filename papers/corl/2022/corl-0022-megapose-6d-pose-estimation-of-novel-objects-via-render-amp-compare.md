---
id: "corl-0022"
title: "MegaPose: 6D Pose Estimation of Novel Objects via Render &amp; Compare"
conference: "CoRL 2022"
date: "2022-12"
authors:
  - name: "Yann Labbe"
    affiliation: "INRIA"
    is_industry: false
  - name: "Lucas Manuelli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tyree"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "et al."
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2212.06870"
  - name: "code"
    url: "https://megapose6d.github.io/"
abstract: "We introduce MegaPose, a method to estimate the 6D pose of novel objects, that is, objects unseen during training. At inference time, the method only assumes knowledge of (i) a region of interest displaying the object in the image and (ii) a CAD model of the observed object. The contributions of thi"
url: "https://research.nvidia.com/publication/2022-12_megapose-6d-pose-estimation-novel-objects-render-compare"
status: "new"
---

# MegaPose: 6D Pose Estimation of Novel Objects via Render &amp; Compare

## 摘要

We introduce MegaPose, a method to estimate the 6D pose of novel objects, that is, objects unseen during training. At inference time, the method only assumes knowledge of (i) a region of interest displaying the object in the image and (ii) a CAD model of the observed object. The contributions of this work are threefold. First, we present a 6D pose refiner based on a render &amp; compare strategy which can be applied to novel objects. The shape and coordinate system of the novel object are provided as inputs to the network by rendering multiple synthetic views of the object's CAD model. Second, we introduce a novel approach for coarse pose estimation which leverages a network trained to classify whether the pose error between a synthetic rendering and an observed image of the same object can be corrected by the refiner. Third, we introduce a large-scale synthetic dataset of photorealistic images of thousands of objects with diverse visual and shape properties and show that this diversity is crucial to obtain good generalization performance on novel objects. We train our approach on this large synthetic dataset and apply it without retraining to hundreds of novel objects in real images from several pose estimation benchmarks. Our approach achieves state-of-the-art performance on the ModelNet and YCB-Video datasets. An extensive evaluation on the 7 core datasets of the BOP challenge demonstrates that our approach achieves performance competitive with existing approaches that require access to the target objects during training.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
