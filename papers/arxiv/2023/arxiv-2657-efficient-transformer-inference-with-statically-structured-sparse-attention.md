---
id: "arxiv-2657"
title: "Efficient Transformer Inference with Statically Structured Sparse Attention"
conference: "arXiv 2023"
date: "2023-07"
authors:
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hasan Genc"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
  - "Computer Architecture"
  - "Generative AI"
external_links:
  - name: "IEEE Proceeding"
    url: "https://ieeexplore.ieee.org/abstract/document/10247993"
abstract: "Self-attention matrices of Transformers are often highly sparse because the relevant context of each token is typically limited to just a few other tokens in the sequence. To reduce the computational burden of self-attention on Transformer inference, we propose static, structured, sparse attention m"
url: "https://research.nvidia.com/publication/2023-07_efficient-transformer-inference-statically-structured-sparse-attention"
status: "new"
---

# Efficient Transformer Inference with Statically Structured Sparse Attention

## 摘要

Self-attention matrices of Transformers are often highly sparse because the relevant context of each token is typically limited to just a few other tokens in the sequence. To reduce the computational burden of self-attention on Transformer inference, we propose static, structured, sparse attention masks that split attention matrices into dense regions, skipping computations outside these regions while reducing computations inside these regions. To support the proposed mask structure, we design an entropy-aware finetuning algorithm to naturally encourage attention sparsity while maximizing task accuracy. Furthermore, we extend a typical dense deep learning accelerator to efficiently exploit our structured sparsity pattern. Compared to a dense baseline, we achieve 56.6% reduction in energy consumption, 58.9% performance improvement with &lt;1% accuracy loss and 2.6% area overhead.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
