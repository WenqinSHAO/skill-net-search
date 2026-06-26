---
id: "arxiv-2782"
title: "Improving Locality of Irregular Updates with Hardware Assisted Propagation Blocking"
conference: "arXiv 2022"
date: "2022-04"
authors:
  - name: "Vignesh Balaji"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brandon Lucia"
    affiliation: "Carnegie Mellon University"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9773262"
abstract: "Many application domains perform irregular memory updates. Irregular accesses lead to inefficient use of conventional cache hierarchies. To make better use of the cache, we focus on Propagation Blocking (PB), a software-based cache locality optimization initially designed for graph processing applic"
url: "https://research.nvidia.com/publication/2022-04_improving-locality-irregular-updates-hardware-assisted-propagation-blocking"
status: "new"
---

# Improving Locality of Irregular Updates with Hardware Assisted Propagation Blocking

## 摘要

Many application domains perform irregular memory updates. Irregular accesses lead to inefficient use of conventional cache hierarchies. To make better use of the cache, we focus on Propagation Blocking (PB), a software-based cache locality optimization initially designed for graph processing applications. We make two contributions in this work. First, we show that PB generalizes beyond graph processing applications to any application with unordered parallelism and irregular memory updates. Second, we identify the inefficiencies of a PB execution on conventional multicore processors and propose architecture support to further improve the performance gains from PB. Our proposed architecture, COBRA, optimizes the PB execution of a range of applications with irregular memory updates, offering speedups of up to 3.78x compared to PB (1.74x on average).

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
