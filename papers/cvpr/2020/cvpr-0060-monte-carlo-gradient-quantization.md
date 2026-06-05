---
id: cvpr-0060
title: "Monte Carlo Gradient Quantization"
conference: CVPR 2020
date: 2020-06
authors:
  - name: "Matthijs Van keirsbilck"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Goncalo Mordido"
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
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "IEEE link"
    url: "https://ieeexplore.ieee.org/document/9150640"
abstract: "We propose Monte Carlo methods to leverage both sparsity and quantization to compress gradients of neural networks throughout training. On top of reducing the communication exchanged between multiple workers in a distributed setting, we also improve the computational efficiency of each worker. Our m"
url: "https://research.nvidia.com/publication/2020-06_monte-carlo-gradient-quantization"
status: new
---

# Monte Carlo Gradient Quantization

## 摘要

We propose Monte Carlo methods to leverage both sparsity and quantization to compress gradients of neural networks throughout training. On top of reducing the communication exchanged between multiple workers in a distributed setting, we also improve the computational efficiency of each worker. Our method, called Monte Carlo Gradient Quantization (MCGQ), shows faster convergence and higher performance than existing quantization methods on image classification and language modeling. Using both low-bit-width-quantization and high sparsity levels, our method more than doubles the rates of existing compression methods from 200x to 520x and 462x to more than 1200x on different language modeling tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
