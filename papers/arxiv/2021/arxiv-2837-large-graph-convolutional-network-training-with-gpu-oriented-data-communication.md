---
id: "arxiv-2837"
title: "Large Graph Convolutional Network Training with GPU-Oriented Data Communication Architecture"
conference: "arXiv 2021"
date: "2021-08"
authors:
  - name: "Seung Won Min"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Kun Wu"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Sitao Huang"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Mert Hidayetoglu"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Jinjun Xiong"
    affiliation: "IBM T.J. Watson Research Center"
    is_industry: true
  - name: "Eiman Ebrahimi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Deming Chen"
    affiliation: "University of Illinois Urbana Champaign"
    is_industry: false
  - name: "Wen-mei Hwu"
    affiliation: "NVIDIA"
    is_industry: true
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
    url: "https://dl.acm.org/doi/10.14778/3476249.3476264"
abstract: "Graph Convolutional Networks (GCNs) are increasingly adopted in large-scale graph-based recommender systems. Training GCN requires the minibatch generator traversing graphs and sampling the sparsely located neighboring nodes to obtain their features. Since real-world graphs often exceed the capacity"
url: "https://research.nvidia.com/publication/2021-08_large-graph-convolutional-network-training-gpu-oriented-data-communication"
status: "new"
---

# Large Graph Convolutional Network Training with GPU-Oriented Data Communication Architecture

## 摘要

Graph Convolutional Networks (GCNs) are increasingly adopted in large-scale graph-based recommender systems. Training GCN requires the minibatch generator traversing graphs and sampling the sparsely located neighboring nodes to obtain their features. Since real-world graphs often exceed the capacity of GPU memory, current GCN training systems keep the feature table in host memory and rely on the CPU to collect sparse features before sending them to the GPUs. This approach, however, puts tremendous pressure on host memory bandwidth and the CPU. This is because the CPU needs to (1) read sparse features from memory, (2) write features into memory as a dense format, and (3) transfer the features from memory to the GPUs. In this work, we propose a novel GPU-oriented data communication approach for GCN training, where GPU threads directly access sparse features in host memory through zero-copy accesses without much CPU help. By removing the CPU gathering stage, our method significantly reduces the consumption of the host resources and data access latency. We further present two important techniques to achieve high host memory access efficiency by the GPU: (1) automatic data access address alignment to maximize PCIe packet efficiency, and (2) asynchronous zero-copy access and kernel execution to fully overlap data transfer with training. We incorporate our method into PyTorch and evaluate its effectiveness using several graphs with sizes up to 111 million nodes and 1.6 billion edges. In a multi-GPU training setup, our method is 65-92% faster than the conventional data transfer method, and can even match the performance of all-in-GPU-memory training for some graphs that fit in GPU memory.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
