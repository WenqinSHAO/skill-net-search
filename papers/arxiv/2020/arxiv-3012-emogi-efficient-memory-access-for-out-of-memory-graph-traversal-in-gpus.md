---
id: arxiv-3012
title: "EMOGI: Efficient Memory-access for Out-of-memory Graph-traversal In GPUs"
conference: arXiv 2020
date: 2020-06
authors:
  - name: "Seung Won Min"
    affiliation: ""
    is_industry: false
  - name: "Vikram Sharma Mailthody"
    affiliation: ""
    is_industry: false
  - name: "Zaid Qureshi"
    affiliation: ""
    is_industry: false
  - name: "Jinjun Xiong"
    affiliation: ""
    is_industry: false
  - name: "Eiman Ebrahimi"
    affiliation: ""
    is_industry: false
  - name: "Wen-mei Hwu"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "High Performance Computing"
abstract: "Modern analytics and recommendation systems are increasingly based on graph data that capture the relations between entities being analyzed. Practical graphs come in huge sizes, offer massive parallelism, and are stored in sparse-matrix formats such as CSR. To exploit the massive parallelism, develo"
url: "https://research.nvidia.com/publication/2020-06_emogi-efficient-memory-access-out-memory-graph-traversal-gpus"
status: new
---

# EMOGI: Efficient Memory-access for Out-of-memory Graph-traversal In GPUs

## 摘要

Modern analytics and recommendation systems are increasingly based on graph data that capture the relations between entities being analyzed. Practical graphs come in huge sizes, offer massive parallelism, and are stored in sparse-matrix formats such as CSR. To exploit the massive parallelism, developers are increasingly interested in using GPUs for graph traversal. However, due to their sizes, graphs often do not fit into the GPU memory. Prior works have either used input data pre-processing/partitioning or UVM to migrate chunks of data from the host memory to the GPU memory. However, the large, multi-dimensional, and sparse nature of graph data presents a major challenge to these schemes and results in significant amplification of data movement and reduced effective data throughput. In this work, we propose EMOGI, an alternative approach to traverse graphs that do not fit in GPU memory using direct cacheline-sized access to data stored in host memory. This paper addresses the open question of whether a sufficiently large number of overlapping cacheline-sized accesses can be sustained to 1) tolerate the long latency to host memory, 2) fully utilize the available bandwidth, and 3) achieve favorable execution performance. We analyze the data access patterns of several graph traversal applications in GPU over PCIe using an FPGA to understand the cause of poor external bandwidth utilization. By carefully coalescing and aligning external memory requests, we show that we can minimize the number of PCIe transactions and nearly fully utilize the PCIe bandwidth even with direct cache-line accesses to the host memory. EMOGI achieves 2.92×&nbsp;speedup on average compared to the optimized UVM implementations in various graph traversal applications. We also show that EMOGI scales better than a UVM-based solution when the system uses higher bandwidth interconnects such as PCIe 4.0.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
