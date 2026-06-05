---
id: neurips-0031
title: "HEAT: Hardware-Efficient Automatic Tensor Decomposition for Transformer Compression"
conference: NeurIPS 2022
date: 2022-12
authors:
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jean Kossaifi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiaqi Gu"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
  - name: "David Z. Pan"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2211.16749"
abstract: "Transformers have attained superior performance in natural language processing and computer vision. Their self-attention and feedforward layers are overparameterized, limiting inference speed and energy efficiency. Tensor decomposition is a promising technique to reduce parameter redundancy by lever"
url: "https://research.nvidia.com/publication/2022-12_heat-hardware-efficient-automatic-tensor-decomposition-transformer-compression"
status: new
---

# HEAT: Hardware-Efficient Automatic Tensor Decomposition for Transformer Compression

## 摘要

Transformers have attained superior performance in natural language processing and computer vision. Their self-attention and feedforward layers are overparameterized, limiting inference speed and energy efficiency. Tensor decomposition is a promising technique to reduce parameter redundancy by leveraging tensor algebraic properties to express the parameters in a factorized form. Prior efforts used manual or heuristic factorization settings without hardware-aware customization, resulting in poor hardware efficiencies and large performance degradation.&nbsp; In this work, we propose a hardware-aware tensor decomposition framework, dubbed HEAT, that enables efficient exploration of the exponential space of possible decompositions and automates the choice of tensorization shape and decomposition rank with hardware-aware co-optimization. We jointly investigate tensor contraction path optimizations and a fused Einsum mapping strategy to bridge the gap between theoretical benefits and real hardware efficiency improvement. Our two-stage knowledge distillation flow resolves the trainability bottleneck and thus significantly boosts the final accuracy of factorized Transformers. Overall, we experimentally show that our hardware-aware factorized BERT variants reduce the energy-delay product by 5.7x with less than 1.1% accuracy loss and achieve a better efficiency-accuracy Pareto frontier than hand-tuned and heuristic baselines.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
