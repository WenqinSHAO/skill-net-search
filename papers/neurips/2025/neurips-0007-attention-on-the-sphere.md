---
id: "neurips-0007"
title: "Attention on the Sphere"
conference: "NeurIPS 2025"
date: "2025-11"
authors:
  - name: "Boris Bonev"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Max Rietmann"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andrea Paris"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alberto Carpentieri"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thorsten Kurth"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Physical AI"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2505.11157"
abstract: "We introduce a generalized attention mechanism for spherical domains, enabling Transformer architectures to natively process data defined on the two-dimensional sphere - a critical need in fields such as atmospheric physics, cosmology, and robotics, where preserving spherical symmetries and topology"
url: "https://research.nvidia.com/publication/2025-11_attention-sphere"
status: "new"
---

# Attention on the Sphere

## 摘要

We introduce a generalized attention mechanism for spherical domains, enabling Transformer architectures to natively process data defined on the two-dimensional sphere - a critical need in fields such as atmospheric physics, cosmology, and robotics, where preserving spherical symmetries and topology is essential for physical accuracy. By integrating numerical quadrature weights into the attention mechanism, we obtain a geometrically faithful spherical attention that is approximately rotationally equivariant, providing strong inductive biases and leading to better performance than Cartesian approaches. To further enhance both scalability and model performance, we propose neighborhood attention on the sphere, which confines interactions to geodesic neighborhoods. This approach reduces computational complexity and introduces the additional inductive bias for locality, while retaining the symmetry properties of our method. We provide optimized CUDA kernels and memory-efficient implementations to ensure practical applicability. The method is validated on three diverse tasks: simulating shallow water equations on the rotating sphere, spherical image segmentation, and spherical depth estimation. Across all tasks, our spherical Transformers consistently outperform their planar counterparts, highlighting the advantage of geometric priors for learning on spherical domains.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
