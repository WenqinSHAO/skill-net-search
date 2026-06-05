---
id: arxiv-3022
title: "An In-Network Architecture for Accelerating Shared-Memory Multiprocessor Collectives"
conference: arXiv 2020
date: 2020-05
authors:
  - name: "Benjamin Klenk"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ted Jiang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Larry Dennison"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Greg Thorson"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - Interconnect_networking
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "High Performance Computing"
  - "Networking"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1109/ISCA45697.2020.00085"
abstract: "The slowdown of single-chip performance scaling combined with the growing demands of computing ever larger problems efficiently has led to a renewed interest in distributed architectures and specialized hardware. Dedicated accelerators for common or critical operations are becoming cost-effective ad"
url: "https://research.nvidia.com/publication/2020-05_network-architecture-accelerating-shared-memory-multiprocessor-collectives"
status: new
---

# An In-Network Architecture for Accelerating Shared-Memory Multiprocessor Collectives

## 摘要

The slowdown of single-chip performance scaling combined with the growing demands of computing ever larger problems efficiently has led to a renewed interest in distributed architectures and specialized hardware. Dedicated accelerators for common or critical operations are becoming cost-effective additions to processors, peripherals, and networks. In this paper we focus on one such operation, the All-Reduce, which is both a common and critical feature of neural network training. All-Reduce is impossible to fully parallelize and difficult to amortize, so it benefits greatly from hardware acceleration. We are proposing an accelerator-centric, shared-memory network that improves All-Reduce performance through in-network reductions, as well as accelerating other collectives like Multicast. We propose switch designs to support in-network computation, including two reduction methods that offer trade-offs in implementation complexity and performance. Additionally, we propose network endpoint modifications to further improve collectives. We present simulation results for a 16 GPU system showing that our collective acceleration design improves the All-Reduce operation by up to 2x for large messages and up to 18x for small messages when compared with a state-of-the-art software algorithm, leading up to 1.4x faster DL training times for networks like Transformer. We demonstrate that this design is scalable to large systems and present results for up to 128 GPUs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
