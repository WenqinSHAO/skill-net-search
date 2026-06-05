---
id: neurips-0041
title: "Alias-Free Generative Adversarial Networks"
conference: NeurIPS 2021
date: 2021-12
authors:
  - name: "Tero Karras"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Miika Aittala"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Samuli Laine"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Janne Hellsten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timo Aila"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Erik Härkönen"
    affiliation: ""
    is_industry: false
  - name: "Jaakko Lehtinen"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "Project page"
    url: "https://nvlabs.github.io/stylegan3"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2106.12423"
  - name: "PyTorch implementation"
    url: "https://github.com/NVlabs/stylegan3"
abstract: "We observe that despite their hierarchical convolutional nature, the synthesis process of typical generative adversarial networks depends on absolute pixel coordinates in an unhealthy manner. This manifests itself as, e.g., detail appearing to be glued to image coordinates instead of the surfaces of"
url: "https://research.nvidia.com/publication/2021-12_alias-free-generative-adversarial-networks"
status: new
---

# Alias-Free Generative Adversarial Networks

## 摘要

We observe that despite their hierarchical convolutional nature, the synthesis process of typical generative adversarial networks depends on absolute pixel coordinates in an unhealthy manner. This manifests itself as, e.g., detail appearing to be glued to image coordinates instead of the surfaces of depicted objects. We trace the root cause to careless signal processing that causes aliasing in the generator network. Interpreting all signals in the network as continuous, we derive generally applicable, small architectural changes that guarantee that unwanted information cannot leak into the hierarchical synthesis process. The resulting networks match the FID of StyleGAN2 but differ dramatically in their internal representations, and they are fully equivariant to translation and rotation even at subpixel scales. Our results pave the way for generative models better suited for video and animation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
