---
id: "arxiv-2961"
title: "Locality-Centric Data and Threadblock Management for Massive GPUs"
conference: "arXiv 2020"
date: "2020-10"
authors:
  - name: "Mahmoud Khairy"
    affiliation: "Purdue University"
    is_industry: false
  - name: "Vadim Nikiforov"
    affiliation: "Purdue University"
    is_industry: false
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timothy G. Rogers"
    affiliation: "Purdue University"
    is_industry: false
topics:
  - CUDA_ecosystem
  - GPU_architecture
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "High Performance Computing"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9251964"
abstract: "Recent work has shown that building GPUs with hundreds of SMs in a single monolithic chip will not be practical due to slowing growth in transistor density, low chip yields, and photoreticle limitations. To maintain performance scalability, proposals exist to aggregate discrete GPUs into a larger vi"
url: "https://research.nvidia.com/publication/2020-10_locality-centric-data-and-threadblock-management-massive-gpus"
status: "new"
---

# Locality-Centric Data and Threadblock Management for Massive GPUs

## 摘要

Recent work has shown that building GPUs with hundreds of SMs in a single monolithic chip will not be practical due to slowing growth in transistor density, low chip yields, and photoreticle limitations. To maintain performance scalability, proposals exist to aggregate discrete GPUs into a larger virtual GPU and decompose a single GPU into multiple-chip-modules with increased aggregate die area. These approaches introduce non-uniform memory access (NUMA) effects and lead to decreased performance and energy-efficiency if not managed appropriately. To overcome these effects, we propose a holistic Locality-Aware Data Management (LADM) system designed to operate on massive logical GPUs composed of multiple discrete devices, which are themselves composed of chiplets. LADM has three key components: a threadblock-centric index analysis, a runtime system that performs data placement and threadblock scheduling, and an adaptive cache insertion policy. The runtime combines information from the static analysis with topology information to proactively optimize data placement, threadblock scheduling, and remote data caching, minimizing off-chip traffic. Compared to state-of-the-art multi-GPU scheduling, LADM reduces inter-chip memory traffic by 4× and improves system performance by 1.8× on a future multi-GPU system.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
