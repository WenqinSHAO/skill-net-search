---
id: "arxiv-2895"
title: "Learning Sparse Matrix Row Permutations for Efficient SpMM on GPU Architectures"
conference: "arXiv 2021"
date: "2021-03"
authors:
  - name: "Atefeh Mehrabi"
    affiliation: "Duke University"
    is_industry: false
  - name: "Donghyuk Lee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Niladrish Chatterjee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Danial J. Sorin"
    affiliation: "Duke University"
    is_industry: false
  - name: "Benjamin C. Lee"
    affiliation: "University of Pennsylvania"
    is_industry: false
  - name: "Mike O'Connor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike O&#039;Connor"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "High Performance Computing"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9408181"
abstract: "Achieving peak performance on sparse operations is challenging. The distribution of the non-zero elements and underlying hardware platform affect the execution efficiency. Given the diversity in workloads and architectures, no uniquesolution always wins. In this paper, we improve SpMM efficiency on "
url: "https://research.nvidia.com/publication/2021-03_learning-sparse-matrix-row-permutations-efficient-spmm-gpu-architectures"
status: "new"
---

# Learning Sparse Matrix Row Permutations for Efficient SpMM on GPU Architectures

## 摘要

Achieving peak performance on sparse operations is challenging. The distribution of the non-zero elements and underlying hardware platform affect the execution efficiency. Given the diversity in workloads and architectures, no uniquesolution always wins. In this paper, we improve SpMM efficiency on GPUs. We propose several simple, but effective, sparse data permutations on the CSR data structure. Picking the right permutation over 1,688 datasets improves performance by 1.4x, on average, compared to plain CSR and 2.6x against NVIDIA cuSPARSE. Furthermore, we propose a set of novel features to describe sparsity patterns and their interactions with the kernel and hardware. Using these features, we develop a predictor to select the best permutation for each matrix. Predicted permutations’ average gain achieves 96% of oracle gains.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
