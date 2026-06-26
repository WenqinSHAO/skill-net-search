---
id: "arxiv-2759"
title: "Mixed-Proxy Extensions for the NVIDIA PTX Memory Consistency Model"
conference: "arXiv 2022"
date: "2022-06"
authors:
  - name: "Daniel Lustig"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Simon Cooksey"
    affiliation: "University of Kent"
    is_industry: false
  - name: "Olivier Giroux"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3470496.3533045"
abstract: "In recent years, there has been a trend towards the use of accelerators and architectural specialization to continue scaling performance in spite of a slowing of Moore’s Law. GPUs have always relied on dedicated hardware for graphics workloads, but modern GPUs now also incorporate compute-domain acc"
url: "https://research.nvidia.com/publication/2022-06_mixed-proxy-extensions-nvidia-ptx-memory-consistency-model"
status: "new"
---

# Mixed-Proxy Extensions for the NVIDIA PTX Memory Consistency Model

## 摘要

In recent years, there has been a trend towards the use of accelerators and architectural specialization to continue scaling performance in spite of a slowing of Moore’s Law. GPUs have always relied on dedicated hardware for graphics workloads, but modern GPUs now also incorporate compute-domain accelerators such as NVIDIA’s Tensor Cores for machine learning. For these accelerators to be successfully integrated into a general-purpose programming language such as C++ or CUDA, there must be a forward- and backward-compatible API for the functionality they provide. To the extent that all of these accelerators interact with program threads through memory, they should be incorporated into the GPU’s memory consistency model. Unfortunately, the use of accelerators and/or special non-coherent paths into memory produces non-standard memory behavior that existing GPU memory models cannot capture.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
