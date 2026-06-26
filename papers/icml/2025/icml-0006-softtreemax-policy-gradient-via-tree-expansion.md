---
id: "icml-0006"
title: "SoftTreeMax: Policy Gradient via tree expansion"
conference: "ICML 2025"
date: "2025-02"
authors:
  - name: "Gal Dalal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Assaf Hallak"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gugan Thoppe"
    affiliation: "IIS"
    is_industry: false
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "ICML 2025 poster"
    url: "https://icml.cc/virtual/2025/poster/43515"
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2301.13236"
  - name: "Code"
    url: "https://github.com/NVlabs/SoftTreeMax"
abstract: "Policy gradient methods are notorious for having a large variance and high sample complexity. To mitigate this, we introduce SoftTreeMax -- a generalization of softmax that employs planning. In SoftTreeMax, we extend the traditional logits with the multi-step discounted cumulative reward, topped wit"
url: "https://research.nvidia.com/publication/2025-02_softtreemax-policy-gradient-tree-expansion"
status: "new"
---

# SoftTreeMax: Policy Gradient via tree expansion

## 摘要

Policy gradient methods are notorious for having a large variance and high sample complexity. To mitigate this, we introduce SoftTreeMax -- a generalization of softmax that employs planning. In SoftTreeMax, we extend the traditional logits with the multi-step discounted cumulative reward, topped with the logits of future states. We analyze SoftTreeMax and explain how tree expansion helps to reduce its gradient variance. We prove that the variance depends on the chosen tree-expansion policy. Specifically, we show that the closer the induced transitions are to being state-independent, the stronger the variance decay. With approximate forward models, we prove that the resulting gradient bias diminishes with the approximation error while retaining the same variance reduction. Ours is the first result to bound the gradient bias for an approximate model. In a practical implementation of SoftTreeMax, we utilize a parallel GPU-based simulator for fast and efficient tree expansion. Using this implementation in Atari, we show that SoftTreeMax reduces the gradient variance by three orders of magnitude. This leads to better sample complexity and improved performance compared to distributed PPO.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
