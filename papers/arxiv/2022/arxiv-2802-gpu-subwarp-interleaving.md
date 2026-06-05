---
id: arxiv-2802
title: "GPU Subwarp Interleaving"
conference: arXiv 2022
date: 2022-01
authors:
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sana Damani"
    affiliation: ""
    is_industry: false
  - name: "Ram Rangan"
    affiliation: ""
    is_industry: false
  - name: "Daniel Johnson"
    affiliation: ""
    is_industry: false
  - name: "Rishkul Kulkarni"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9773183"
abstract: "Raytracing applications have naturally high thread divergence, low warp occupancy and are limited by memory latency. In this paper, we present an architectural enhancement called Subwarp Interleaving that exploits thread divergence to hide pipeline stalls in divergent sections of low warp occupancy "
url: "https://research.nvidia.com/publication/2022-01_gpu-subwarp-interleaving"
status: new
---

# GPU Subwarp Interleaving

## 摘要

Raytracing applications have naturally high thread divergence, low warp occupancy and are limited by memory latency. In this paper, we present an architectural enhancement called Subwarp Interleaving that exploits thread divergence to hide pipeline stalls in divergent sections of low warp occupancy workloads. Subwarp Interleaving allows for fine-grained interleaved execution of diverged paths within a warp with the goal of increasing hardware utilization and reducing warp latency. However, notwithstanding the promise shown by early microbenchmark studies and an average performance upside of 6.3% (up to 20%) on a simulator across a suite of raytracing application traces, the Subwarp Interleaving design feature has shortcomings that preclude its near-term implementation. This paper introduces the reader to the challenges of raytracing and discusses a novel microarchitectural approach that, on paper, addresses many of the challenges. A thorough analysis of the idea on a production simulator reveals that the high-level motivating statistics are optimistic, and second-order effects, along with other architectural sharp edges, limit the idea’s potential. We identify Subwarp Interleaving’s primary limiters for an NVIDIA Turing-like architecture, and we outline the conditions under which the approach could be more effective.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
