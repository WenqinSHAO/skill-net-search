---
id: neurips-0022
title: "Convolutional State Space Models for Long-Range Spatiotemporal Modeling"
conference: NeurIPS 2023
date: 2023-12
authors:
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jimmy T. H. Smith"
    affiliation: ""
    is_industry: false
  - name: "Scott Linderman"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2310.19694"
  - name: "Project Page"
    url: "https://github.com/NVlabs/ConvSSM"
abstract: "Effectively modeling long spatiotemporal sequences is challenging due to the need to model complex spatial correlations and long-range temporal dependencies simultaneously. ConvLSTMs attempt to address this by updating tensor-valued states with recurrent neural networks, but their sequential computa"
url: "https://research.nvidia.com/publication/2023-12_convolutional-state-space-models-long-range-spatiotemporal-modeling"
status: new
---

# Convolutional State Space Models for Long-Range Spatiotemporal Modeling

## 摘要

Effectively modeling long spatiotemporal sequences is challenging due to the need to model complex spatial correlations and long-range temporal dependencies simultaneously. ConvLSTMs attempt to address this by updating tensor-valued states with recurrent neural networks, but their sequential computation makes them slow to train. In contrast, Transformers can process an entire spatiotemporal sequence, compressed into tokens, in parallel. However, the cost of attention scales quadratically in length, limiting their scalability to longer sequences. Here, we address the challenges of prior methods and introduce convolutional state space models (ConvSSM) that combine the tensor modeling ideas of ConvLSTM with the long sequence modeling approaches of state space methods such as S4 and S5. First, we demonstrate how parallel scans can be applied to convolutional recurrences to achieve subquadratic parallelization and fast autoregressive generation. We then establish an equivalence between the dynamics of ConvSSMs and SSMs, which motivates parameterization and initialization strategies for modeling long-range dependencies. The result is ConvS5, an efficient ConvSSM variant for long-range spatiotemporal modeling. ConvS5 significantly outperforms Transformers and ConvLSTM on a long horizon Moving-MNIST experiment while training 3x faster than ConvLSTM and generating samples 400x faster than Transformers. In addition, ConvS5 matches or exceeds the performance of state-of-the-art methods on challenging DMLab, Minecraft and Habitat prediction benchmarks and enables new directions for modeling long spatiotemporal sequences.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
