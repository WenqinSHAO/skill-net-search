---
id: "arxiv-2751"
title: "GPU-Accelerated Partially Linear Multiuser Detection for 5G and Beyond URLLC Systems"
conference: "arXiv 2022"
date: "2022-06"
authors:
  - name: "Matthias Mehlhose"
    affiliation: "Fraunhofer Institute for Telecommunications, HHI"
    is_industry: false
  - name: "Guillermo Marcus"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Schäufele"
    affiliation: "Fraunhofer Institute for Telecommunications, HHI"
    is_industry: false
  - name: "Daniyal Amir Awan"
    affiliation: "Fraunhofer Institute for Telecommunications, HHI"
    is_industry: false
  - name: "Nikolaus Binder"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Martin Kasparick"
    affiliation: "Fraunhofer Institute for Telecommunications, HHI"
    is_industry: false
  - name: "Renato L. G. Cavalcante"
    affiliation: "Fraunhofer Institute for Telecommunications, HHI"
    is_industry: false
  - name: "Sławomir Stanćzak"
    affiliation: "Fraunhofer Institute for Telecommunications, HHI"
    is_industry: false
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Telecommunications"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/pdf/2201.05024.pdf"
abstract: "We have implemented a recently proposed partially linear multiuser detection algorithm in reproducing kernel Hilbert spaces (RKHSs) on a GPU-accelerated platform. Our proof of concept combines the robustness of linear detection and non-linear detection for the non-orthogonal multiple access (NOMA) b"
url: "https://research.nvidia.com/publication/2022-06_gpu-accelerated-partially-linear-multiuser-detection-5g-and-beyond-urllc"
status: "new"
---

# GPU-Accelerated Partially Linear Multiuser Detection for 5G and Beyond URLLC Systems

## 摘要

We have implemented a recently proposed partially linear multiuser detection algorithm in reproducing kernel Hilbert spaces (RKHSs) on a GPU-accelerated platform. Our proof of concept combines the robustness of linear detection and non-linear detection for the non-orthogonal multiple access (NOMA) based massive connectivity scenario. Mastering the computation of the vast number of inner products (which involve kernel evaluations) is a challenge in ultra-low latency (ULL) applications due to the sub-millisecond latency requirement. To address the issue, we propose a massively parallel implementation of the detection of user data in a received orthogonal frequency-division multiplexing (OFDM) radio frame. The result is a GPU-accelerated real-time OFDM receiver that enables detection latency of less than one millisecond that complies with the requirements of 5th generation (5G) and beyond ultra-reliable and low latency communications (URLLC) systems. Moreover, the parallelization and acceleration techniques explored and demonstrated in this study can be extended to many signal processing algorithms in Hilbert spaces, such as projection onto convex sets (POCS) and adaptive projected subgradient method (APSM) based algorithms. Results and comparisons with the state-of-the-art confirm the effectiveness of our approach.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
