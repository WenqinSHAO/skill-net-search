---
id: "arxiv-2945"
title: "GPU-Trident: Efficient Modeling of Error Propagation in GPU Programs"
conference: "arXiv 2020"
date: "2020-11"
authors:
  - name: "Abdul Rehman Anwer"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Guanpeng Li"
    affiliation: "University of Iowa"
    is_industry: false
  - name: "Karthik Pattabiraman"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timothy Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Resilience and Safety"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/abstract/document/9355257"
abstract: "Fault injection (FI) techniques are typically used to determine the reliability profiles of programs under soft errors. However, these techniques are highly resource- and time-intensive. Prior research developed a model, TRIDENT to analytically predict Silent Data Corruption (SDC, i.e., incorrect ou"
url: "https://research.nvidia.com/publication/2020-11_gpu-trident-efficient-modeling-error-propagation-gpu-programs"
status: "new"
---

# GPU-Trident: Efficient Modeling of Error Propagation in GPU Programs

## 摘要

Fault injection (FI) techniques are typically used to determine the reliability profiles of programs under soft errors. However, these techniques are highly resource- and time-intensive. Prior research developed a model, TRIDENT to analytically predict Silent Data Corruption (SDC, i.e., incorrect output without any indication) probabilities of single-threaded CPU applications without requiring FIs. Unfortunately, TRIDENT is incompatible with GPU programs, due to their high degree of parallelism and different memory architectures than CPU programs. The main challenge is that modeling error propagation across thousands of threads in a GPU kernel requires enormous amounts of data to be profiled and analyzed, posing a major scalability bottleneck for HPC applications. In this paper, we propose GPU-TRIDENT, an accurate and scalable technique for modeling error propagation in GPU programs. We find that GPU-TRIDENT is 2 orders of magnitude faster than FI-based approaches, and nearly as accurate in determining the SDC rate of GPU programs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
