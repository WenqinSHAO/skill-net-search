---
id: cvpr-0027
title: "Affordance Diffusion: Synthesizing Hand-Object Interactions"
conference: CVPR 2023
date: 2023-06
authors:
  - name: "Xueting Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yufei Ye"
    affiliation: ""
    is_industry: false
  - name: "Abhinav Gupta"
    affiliation: ""
    is_industry: false
  - name: "Jiaming Song"
    affiliation: ""
    is_industry: false
  - name: "Shubham Tulsiani"
    affiliation: ""
    is_industry: false
topics:
  - Applied_perception
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Human Computer Interaction"
  - "Robotics"
external_links:
  - name: "Project Page"
    url: "https://judyye.github.io/affordiffusion-www/"
  - name: "Code"
    url: "https://github.com/NVlabs/affordance_diffusion"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2303.12538"
abstract: "Recent successes in image synthesis are powered by large-scale diffusion models. However, most methods are currently limited to either text- or image-conditioned generation for synthesizing an entire image, texture transfer or inserting objects into a user-specified region. In contrast, in this work"
url: "https://research.nvidia.com/publication/2023-06_affordance-diffusion-synthesizing-hand-object-interactions"
status: new
---

# Affordance Diffusion: Synthesizing Hand-Object Interactions

## 摘要

Recent successes in image synthesis are powered by large-scale diffusion models. However, most methods are currently limited to either text- or image-conditioned generation for synthesizing an entire image, texture transfer or inserting objects into a user-specified region. In contrast, in this work we focus on synthesizing complex interactions (i.e., an articulated hand) with a given object. Given an RGB image of an object, we aim to hallucinate plausible images of a human hand interacting with it. We propose a two-step generative approach: a LayoutNet that samples an articulation-agnostic hand-object-interaction layout, and a ContentNet that synthesizes images of a hand grasping the object given the predicted layout. Both are built on top of a large-scale pretrained diffusion model to make use of its latent representation. Compared to baselines, the proposed method is shown to generalize better to novel objects and perform surprisingly well on out-of-distribution in-the-wild scenes of portable-sized objects. The resulting system allows us to predict descriptive affordance information, such as hand articulation and approaching orientation.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
