---
id: "siggraph-0061"
title: "Instant Neural Graphics Primitives with a Multiresolution Hash Encoding"
conference: "SIGGRAPH 2022"
date: "2022-07"
authors:
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Evans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Christoph Schied"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computational Photography and Imaging"
  - "Computer Graphics"
  - "Computer Vision"
  - "High Performance Computing"
  - "Real-Time Rendering"
external_links:
  - name: "Project page"
    url: "https://nvlabs.github.io/instant-ngp"
abstract: "Neural graphics primitives, parameterized by fully connected neural networks, can be costly to train and evaluate.&nbsp;We reduce this cost with a versatile new input encoding that permits the use of a smaller network without sacrificing quality, thus significantly reducing the number of floating po"
url: "https://research.nvidia.com/publication/2022-07_instant-neural-graphics-primitives-multiresolution-hash-encoding"
status: "new"
---

# Instant Neural Graphics Primitives with a Multiresolution Hash Encoding

## 摘要

Neural graphics primitives, parameterized by fully connected neural networks, can be costly to train and evaluate.&nbsp;We reduce this cost with a versatile new input encoding that permits the use of a smaller network without sacrificing quality, thus significantly reducing the number of floating point and memory access operations:&nbsp;a small neural network is augmented by a multiresolution hash table of trainable feature vectors whose values are optimized through stochastic gradient descent.&nbsp;The multiresolution structure allows the network to disambiguate hash collisions, making for a simple architecture that is trivial to parallelize on modern GPUs.&nbsp;We leverage this parallelism by implementing the whole system using fully-fused CUDA kernels with a focus on minimizing wasted bandwidth and compute operations.&nbsp;We achieve a combined speedup of several orders of magnitude, enabling training of high-quality neural graphics primitives in a matter of seconds, and rendering in tens of milliseconds at a resolution of 1920x1080.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
