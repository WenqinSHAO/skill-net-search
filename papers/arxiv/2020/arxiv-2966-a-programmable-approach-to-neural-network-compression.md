---
id: arxiv-2966
title: "A Programmable Approach to Neural Network Compression"
conference: arXiv 2020
date: 2020-10
authors:
  - name: "Saurav Muralidharan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vinu Joseph"
    affiliation: ""
    is_industry: false
  - name: "Ganesh L. Gopalakrishnan"
    affiliation: ""
    is_industry: false
  - name: "Animesh Garg"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/1911.02497"
  - name: "Code"
    url: "https://github.com/NVlabs/condensa"
abstract: "Deep neural networks (DNNs) frequently contain far more weights, represented at a higher precision, than are required for the specific task, which they are trained to perform. Consequently, they can often be compressed using techniques such as weight pruning and quantization that reduce both the mod"
url: "https://research.nvidia.com/publication/2020-10_programmable-approach-neural-network-compression"
status: new
---

# A Programmable Approach to Neural Network Compression

## 摘要

Deep neural networks (DNNs) frequently contain far more weights, represented at a higher precision, than are required for the specific task, which they are trained to perform. Consequently, they can often be compressed using techniques such as weight pruning and quantization that reduce both the model size and inference time without appreciable loss in accuracy. However, finding the best compression strategy and corresponding target sparsity for a given DNN, hardware platform, and optimization objective currently requires expensive, frequently manual, trial-and-error experimentation. In this article, we introduce a programmable system for model compression called Condensa. Users programmatically compose simple operators, in Python, to build more complex and practically interesting compression strategies. Given a strategy and user-provided objective (such as minimization of running time), Condensa uses a novel Bayesian optimization-based algorithm to automatically infer desirable sparsities. Our experiments on four real-world DNNs demonstrate memory footprint and hardware runtime throughput improvements of 188x and 2.59x, respectively, using at most ten samples per search. We have released a reference implementation of Condensa at: https://github.com/NVlabs/condensa

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
