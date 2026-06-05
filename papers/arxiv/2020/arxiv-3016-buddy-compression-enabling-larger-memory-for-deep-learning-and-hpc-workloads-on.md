---
id: arxiv-3016
title: "Buddy Compression: Enabling Larger Memory for Deep Learning and HPC Workloads on GPUs"
conference: arXiv 2020
date: 2020-06
authors:
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike O&#039;Connor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Esha Chouske"
    affiliation: ""
    is_industry: false
  - name: "Mattan Erez"
    affiliation: ""
    is_industry: false
  - name: "Jeff Pool"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "High Performance Computing"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9138915"
abstract: "GPUs accelerate high-throughput applications, which require orders-of-magnitude higher memory bandwidth than traditional CPU-only systems. However, the capacity of such high-bandwidth memory tends to be relatively small. Buddy Compression is an architecture that makes novel use of compression to uti"
url: "https://research.nvidia.com/publication/2020-06_buddy-compression-enabling-larger-memory-deep-learning-and-hpc-workloads-gpus"
status: new
---

# Buddy Compression: Enabling Larger Memory for Deep Learning and HPC Workloads on GPUs

## 摘要

GPUs accelerate high-throughput applications, which require orders-of-magnitude higher memory bandwidth than traditional CPU-only systems. However, the capacity of such high-bandwidth memory tends to be relatively small. Buddy Compression is an architecture that makes novel use of compression to utilize a larger buddy-memory from the host or disaggregated memory, effectively increasing the memory capacity of the GPU. Buddy Compression splits each compressed 128B memory-entry between the high-bandwidth GPU memory and a slower-but-larger buddy memory such that compressible memory-entries are accessed completely from GPU memory, while incompressible entries source some of their data from off-GPU memory. With Buddy Compression, compressibility changes never result in expensive page movement or re-allocation. Buddy Compression achieves on average 1.9× effective GPU memory expansion for representative HPC applications and 1.5× for deep learning training, performing within 2% of an unrealistic system with no memory limit. This makes Buddy Compression attractive for performance-conscious developers that require additional GPU memory capacity.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
