---
id: arxiv-2909
title: "P-OPT: Practical Optimal Cache Replacement for Graph Analytics"
conference: arXiv 2021
date: 2021-02
authors:
  - name: "Neal Crago"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aamer Jaleel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vignesh Balaji"
    affiliation: ""
    is_industry: false
  - name: "Brandon Lucia"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9407090"
abstract: "Graph analytics is an important workload that achieves suboptimal performance due to poor cache locality. State-of-the-art cache replacement policies fail to capture the highly dynamic and input-specific reuse patterns of graph application data. The main insight of this work is that for graph applic"
url: "https://research.nvidia.com/publication/2021-02_p-opt-practical-optimal-cache-replacement-graph-analytics"
status: new
---

# P-OPT: Practical Optimal Cache Replacement for Graph Analytics

## 摘要

Graph analytics is an important workload that achieves suboptimal performance due to poor cache locality. State-of-the-art cache replacement policies fail to capture the highly dynamic and input-specific reuse patterns of graph application data. The main insight of this work is that for graph applications, the transpose of a graph succinctly represents the next references of all vertices in a graph execution; enabling an efficient emulation of Belady's MIN replacement policy. In this work, we propose P-OPT, an architecture solution that uses a specialized compressed representation of a transpose's next reference information to enable a practical implementation of Belady's MIN replacement policy. Our evaluations across multiple applications and inputs reveal that P-OPT improves cache locality for graph applications providing an average performance improvement of 33% (56% maximum) over LRU replacement.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
