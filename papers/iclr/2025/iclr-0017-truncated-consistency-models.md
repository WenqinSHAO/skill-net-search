---
id: iclr-0017
title: "Truncated Consistency Models"
conference: ICLR 2025
date: 2025-01
authors:
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sangyun Lee"
    affiliation: ""
    is_industry: false
  - name: "Yilun Xu"
    affiliation: ""
    is_industry: false
  - name: "Giulia Fanti"
    affiliation: ""
    is_industry: false
  - name: "Weili Nie"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://truncated-cm.github.io/"
abstract: "Consistency models have recently been introduced to accelerate sampling from diffusion models by directly predicting the solution (i.e., data) of the probability flow ODE (PF ODE) from initial noise. However, the training of consistency models requires learning to map all intermediate points along P"
url: "https://research.nvidia.com/publication/2025-01_truncated-consistency-models"
status: new
---

# Truncated Consistency Models

## 摘要

Consistency models have recently been introduced to accelerate sampling from diffusion models by directly predicting the solution (i.e., data) of the probability flow ODE (PF ODE) from initial noise. However, the training of consistency models requires learning to map all intermediate points along PF ODE trajectories to their corresponding endpoints. This task is much more challenging than the ultimate objective of one-step generation, which only concerns the PF ODE’s noise-to-data mapping. We empirically find that this training paradigm limits the one-step generation performance of consistency models. To address this issue, we generalize consistency training to the truncated time range, which allows the model to ignore denoising tasks at earlier time steps and focus its capacity on generation. We propose a new parameterization of the consistency function and a two-stage training procedure that prevents the truncated-time training from collapsing to a trivial solution. Experiments on CIFAR-10 and ImageNet 64 x 64 datasets show that our method achieves better one-step and two-step FIDs than the state-of-theart consistency models such as iCT-deep, using more than 2x smaller networks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
