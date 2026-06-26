---
id: "arxiv-3048"
title: "ABCDPlace: Accelerated Batch-based Concurrent Detailed Placement on Multi-threaded CPUs and GPUs"
conference: "arXiv 2020"
date: "2020-02"
authors:
  - name: "Yibo Lin"
    affiliation: "Peking University"
    is_industry: false
  - name: "Wuxi Li"
    affiliation: "Xilinx"
    is_industry: false
  - name: "Jiaqi Gu"
    affiliation: "UT-Austin"
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Z. Pan"
    affiliation: "UT-Austin"
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
abstract: "Placement is an important step in modern very-large-scale integrated (VLSI) designs. Detailed placement is a placement refining procedure intensively called throughout the design flow, thus its efficiency has a vital impact on design closure. However, since most detailed placement techniques are inh"
url: "https://research.nvidia.com/publication/2020-02_abcdplace-accelerated-batch-based-concurrent-detailed-placement-multi-threaded"
status: "new"
---

# ABCDPlace: Accelerated Batch-based Concurrent Detailed Placement on Multi-threaded CPUs and GPUs

## 摘要

Placement is an important step in modern very-large-scale integrated (VLSI) designs. Detailed placement is a placement refining procedure intensively called throughout the design flow, thus its efficiency has a vital impact on design closure. However, since most detailed placement techniques are inherently greedy and sequential, they are generally difficult to parallelize. In this work, we present a concurrent detailed placement framework, ABCDPlace, exploiting multithreading and GPU acceleration. We propose batch-based concurrent algorithms for widely-adopted sequential detailed placement techniques, such as independent set matching, global swap, and local reordering. Experimental results demonstrate that ABCDPlace can achieve 2×-5× faster runtime than sequential implementations with multi-threaded CPU and over 10× with GPU on ISPD 2005 contest benchmarks without quality degradation. On larger industrial benchmarks, we show more than 16× speedup with GPU over the state-of-the-art sequential detailed placer. ABCDPlace finishes the detailed placement of a 10-million-cell industrial design in one minute.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
