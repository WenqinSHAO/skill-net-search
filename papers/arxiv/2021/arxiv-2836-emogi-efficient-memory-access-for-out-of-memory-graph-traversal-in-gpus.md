---
id: "arxiv-2836"
title: "EMOGI: Efficient Memory-access for Out-of-memory Graph-traversal in GPUs"
conference: "arXiv 2021"
date: "2021-08"
authors:
  - name: "Seung Won Min"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Vikram Sharma Mailthody"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Zaid Qureshi"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Jinjun Xiong"
    affiliation: "ITM T.J. Watson Research Center"
    is_industry: false
  - name: "Eiman Ebrahimi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wen-mei Hwu"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
topics:
  - GPU_architecture
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "High Performance Computing"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.14778/3425879.3425883"
abstract: "Modern analytics and recommendation systems are increasingly based on graph data that capture the relations between entities being analyzed. Practical graphs come in huge sizes, offer massive parallelism, and are stored in sparse-matrix formats such as compressed sparse row (CSR). To exploit the mas"
url: "https://research.nvidia.com/publication/2021-08_emogi-efficient-memory-access-out-memory-graph-traversal-gpus"
status: "new"
---

# EMOGI: Efficient Memory-access for Out-of-memory Graph-traversal in GPUs

## 摘要

Modern analytics and recommendation systems are increasingly based on graph data that capture the relations between entities being analyzed. Practical graphs come in huge sizes, offer massive parallelism, and are stored in sparse-matrix formats such as compressed sparse row (CSR). To exploit the massive parallelism, developers are increasingly interested in using GPUs for graph traversal. However, due to their sizes, graphs often do not fit into the GPU memory. Prior works have either used input data preprocessing/partitioning or unified virtual memory (UVM) to migrate chunks of data from the host memory to the GPU memory. However, the large, multi-dimensional, and sparse nature of graph data presents a major challenge to these schemes and results in significant amplification of data movement and reduced effective data throughput. In this work, we propose EMOGI, an alternative approach to traverse graphs that do not fit in GPU memory using direct cache-line-sized access to data stored in host memory. This paper addresses the open question of whether a sufficiently large number of overlapping cache-line-sized accesses can be sustained to 1) tolerate the long latency to host memory, 2) fully utilize the available bandwidth, and 3) achieve favorable execution performance. We analyze the data access patterns of several graph traversal applications in GPU over PCIe using an FPGA to understand the cause of poor external bandwidth utilization. By carefully coalescing and aligning external memory requests, we show that we can minimize the number of PCIe transactions and nearly fully utilize the PCIe bandwidth with direct cache-line accesses to the host memory. EMOGI achieves 2.60× speedup on average compared to the optimized UVM implementations in various graph traversal applications. We also show that EMOGI scales better than a UVM-based solution when the

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
