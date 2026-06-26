---
id: "arxiv-2592"
title: "Conformer without Convolutions"
conference: "arXiv 2024"
date: "2024-09"
authors:
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
abstract: "We analyze the weights of a trained speech-to-text neural network and discover a surprising amount of structure in the temporal convolutions. Based on our observations we propose to completely remove learnable temporal convolutions, and replace them with fixed averaging and shift operations which ha"
url: "https://research.nvidia.com/publication/2024-09_conformer-without-convolutions"
status: "new"
---

# Conformer without Convolutions

## 摘要

We analyze the weights of a trained speech-to-text neural network and discover a surprising amount of structure in the temporal convolutions. Based on our observations we propose to completely remove learnable temporal convolutions, and replace them with fixed averaging and shift operations which have no learnable parameters and open the way for significantly faster implementations. In the state-of-the-art models Conformer, Squeezeformer and FastConformer, this improves WER by 0.12%, 0.62%, and 0.20% respectively, while reducing the computational cost.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
