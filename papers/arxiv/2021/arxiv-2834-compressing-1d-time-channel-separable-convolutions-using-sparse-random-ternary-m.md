---
id: "arxiv-2834"
title: "Compressing 1D Time-Channel Separable Convolutions using Sparse Random Ternary Matrices"
conference: "arXiv 2021"
date: "2021-08"
authors:
  - name: "Goncalo Mordido"
    affiliation: "Hasso Plattner Institute"
    is_industry: false
  - name: "Matthijs Van keirsbilck"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Arxiv link"
    url: "https://arxiv.org/pdf/2103.17142.pdf"
  - name: "GTC 21 talk"
    url: "https://www.nvidia.com/en-us/on-demand/session/gtcspring21-e31454/"
  - name: "Interspeech 3 minute video"
    url: "https://www.youtube.com/watch?v=s8AL4RIZ2Ig"
abstract: "We demonstrate that 1x1-convolutions in 1D time-channel separable convolutions may be replaced by constant, sparse random ternary matrices with weights in {−1, 0, +1}. Such layers do not perform any multiplications and do not require training. Moreover, the matrices may be generated on the chip duri"
url: "https://research.nvidia.com/publication/2021-08_compressing-1d-time-channel-separable-convolutions-using-sparse-random-ternary"
status: "new"
---

# Compressing 1D Time-Channel Separable Convolutions using Sparse Random Ternary Matrices

## 摘要

We demonstrate that 1x1-convolutions in 1D time-channel separable convolutions may be replaced by constant, sparse random ternary matrices with weights in {−1, 0, +1}. Such layers do not perform any multiplications and do not require training. Moreover, the matrices may be generated on the chip during computation and therefore do not require any memory access. With the same parameter budget, we can afford deeper and more expressive models, improving the Pareto frontiers of existing models on several tasks. For command recognition on Google Speech Commands v1, we improve the state-of-the-art accuracy from 97.21% to 97.41% at the same network size. Alternatively, we can lower the cost of existing models. For speech recognition on Librispeech, we half the number of weights to be trained while only sacrificing about 1% of the floating-point baseline’s word error rate.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
