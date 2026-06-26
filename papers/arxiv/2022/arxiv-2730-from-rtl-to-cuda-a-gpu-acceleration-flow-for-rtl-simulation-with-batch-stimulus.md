---
id: "arxiv-2730"
title: "From RTL to CUDA: A GPU Acceleration Flow for RTL Simulation with Batch Stimulus"
conference: "arXiv 2022"
date: "2022-08"
authors:
  - name: "Dian-Lun Lin"
    affiliation: "University of Utah"
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tsung-Wei Huang"
    affiliation: "University of Utah"
    is_industry: false
topics:
  - CUDA_ecosystem
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Circuits and VLSI Design"
external_links:
  - name: "Open source code"
    url: "https://github.com/dian-lun-lin/RTLflow"
abstract: "High-throughput RTL simulation is critical for verifying today’s&nbsp;highly complex SoCs. Recent research has explored accelerating&nbsp;RTL simulation by leveraging event-driven approaches or partitioning&nbsp;heuristics to speed up simulation on a single stimulus. To further&nbsp;accelerate throu"
url: "https://research.nvidia.com/publication/2022-08_rtl-cuda-gpu-acceleration-flow-rtl-simulation-batch-stimulus"
status: "new"
---

# From RTL to CUDA: A GPU Acceleration Flow for RTL Simulation with Batch Stimulus

## 摘要

High-throughput RTL simulation is critical for verifying today’s&nbsp;highly complex SoCs. Recent research has explored accelerating&nbsp;RTL simulation by leveraging event-driven approaches or partitioning&nbsp;heuristics to speed up simulation on a single stimulus. To further&nbsp;accelerate throughput performance, industry-quality functional verification&nbsp;signoff must explore running multiple stimulus (i.e., batch&nbsp;stimulus) simultaneously, either with directed tests or random inputs.&nbsp;In this paper, we propose RTLFlow, a GPU-accelerated RTL&nbsp;simulation flow with batch stimulus. RTLflow first transpiles RTL&nbsp;into CUDA kernels that each simulates a partition of the RTL simultaneously&nbsp;across multiple stimulus. It also leverages CUDA Graph and pipeline scheduling for efficient runtime execution. Measuring&nbsp;experimental results on a large industrial design (NVDLA) with&nbsp;65536 stimulus, we show that RTLflow running on a single A6000&nbsp;GPU can achieve a 40× runtime speed-up when compared to an&nbsp;80-thread multi-core CPU baseline.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
