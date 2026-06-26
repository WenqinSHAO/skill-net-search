---
id: "arxiv-3006"
title: "Regularizing Neural Networks via Minimizing Hyperspherical Energy"
conference: "arXiv 2020"
date: "2020-06"
authors:
  - name: "Weiyang Liu"
    affiliation: "Gatech"
    is_industry: false
  - name: "Rongmei Lin"
    affiliation: "Emory"
    is_industry: false
  - name: "Zhen Liu"
    affiliation: "Mila"
    is_industry: false
  - name: "Chen Feng"
    affiliation: "NYU"
    is_industry: false
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "James M. Rehg"
    affiliation: "Gatech"
    is_industry: false
  - name: "Li Xiong"
    affiliation: "Emory"
    is_industry: false
  - name: "Le Song"
    affiliation: "Gatech"
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/1906.04892"
  - name: "Code"
    url: "https://github.com/rmlin/CoMHE"
  - name: "Talk"
    url: "https://www.youtube.com/watch?v=vXxt_ggWW8s"
  - name: "Slides"
    url: "https://wyliu.com/papers/CoMHE_slides.pdf"
abstract: "Inspired by the Thomson problem in physics where the distribution of multiple propelling electrons on a unit sphere can be modeled via minimizing some potential energy, hyperspherical energy minimization has demonstrated its potential in regularizing neural networks and improving their generalizatio"
url: "https://research.nvidia.com/publication/2020-06_regularizing-neural-networks-minimizing-hyperspherical-energy"
status: "new"
---

# Regularizing Neural Networks via Minimizing Hyperspherical Energy

## 摘要

Inspired by the Thomson problem in physics where the distribution of multiple propelling electrons on a unit sphere can be modeled via minimizing some potential energy, hyperspherical energy minimization has demonstrated its potential in regularizing neural networks and improving their generalization power. In this paper, we first study the important role that hyperspherical energy plays in neural network training by analyzing its training dynamics. Then we show that naively minimizing hyperspherical energy suffers from some difficulties due to highly non-linear and non-convex optimization as the space dimensionality becomes higher, therefore limiting the potential to further improve the generalization. To address these problems, we propose the compressive minimum hyperspherical energy (CoMHE) as a more effective regularization for neural networks. Specifically, CoMHE utilizes projection mappings to reduce the dimensionality of neurons and minimizes their hyperspherical energy. According to different designs for the projection mapping, we propose several distinct yet well-performing variants and provide some theoretical guarantees to justify their effectiveness. Our experiments show that CoMHE consistently outperforms existing regularization methods, and can be easily applied to different neural networks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
