---
id: arxiv-2887
title: "VS-QUANT: Per-Vector Scaled Quantization for Accurate Low-Precision Neural Network Inference"
conference: arXiv 2021
date: 2021-04
authors:
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brian Zimmer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "William Dally"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
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
  - "Circuits and VLSI Design"
  - "Computer Architecture"
external_links:
  - name: "VS-QUANT: Per-Vector Scaled Quantization for Accurate Low-Precision Neural Netw…"
    url: "https://arxiv.org/abs/2102.04503"
abstract: "Quantization enables efficient acceleration of deep neural networks by reducing model memory footprint and exploiting low-cost integer math hardware units. Quantization maps floating-point weights and activations in a trained model to low-bitwidth integer values using scale factors. Excessive quanti"
url: "https://research.nvidia.com/publication/2021-04_vs-quant-vector-scaled-quantization-accurate-low-precision-neural-network"
status: new
---

# VS-QUANT: Per-Vector Scaled Quantization for Accurate Low-Precision Neural Network Inference

## 摘要

Quantization enables efficient acceleration of deep neural networks by reducing model memory footprint and exploiting low-cost integer math hardware units. Quantization maps floating-point weights and activations in a trained model to low-bitwidth integer values using scale factors. Excessive quantization, reducing precision too aggressively, results in accuracy degradation. When scale factors are shared at a coarse granularity across many dimensions of each tensor, effective precision of individual elements within the tensor are limited. To reduce quantization-related accuracy loss, we propose using a separate scale factor for each small vector of (≈16-64) elements within a single dimension of a tensor. To achieve an efficient hardware implementation, the per-vector scale factors can be implemented with low-bitwidth integers when calibrated using a two-level quantization scheme. We find that per-vector scaling consistently achieves better inference accuracy at low precision compared to conventional scaling techniques for popular neural networks without requiring retraining. We also modify a deep learning accelerator hardware design to study the area and energy overheads of per-vector scaling support. Our evaluation demonstrates that per-vector scaled quantization with 4-bit weights and activations achieves 37% area saving and 24% energy saving while maintaining over 75% accuracy for ResNet50 on ImageNet. 4-bit weights and 8-bit activations achieve near-full-precision accuracy for both BERT-base and BERT-large on SQuAD while reducing area by 26% compared to an 8-bit baseline.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
