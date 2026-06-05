---
id: arxiv-2906
title: "Making Convolutions Resilient via Algorithm-Based Error Detection Techniques"
conference: arXiv 2021
date: 2021-03
authors:
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timothy Tsai"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "Resilience and Safety"
external_links:
  - name: "Published manuscript (IEEE Digital Library)"
    url: "https://ieeexplore.ieee.org/document/9366780"
abstract: "Convolutional Neural Networks (CNNs) are being increasingly used in safety-critical and high-performance computing systems. As such systems require high levels of resilience to errors, CNNs must execute correctly in the presence of hardware faults. Full duplication provides the needed assurance but "
url: "https://research.nvidia.com/publication/2021-03_making-convolutions-resilient-algorithm-based-error-detection-techniques"
status: new
---

# Making Convolutions Resilient via Algorithm-Based Error Detection Techniques

## 摘要

Convolutional Neural Networks (CNNs) are being increasingly used in safety-critical and high-performance computing systems. As such systems require high levels of resilience to errors, CNNs must execute correctly in the presence of hardware faults. Full duplication provides the needed assurance but incurs a prohibitive 100% overhead. In this paper, we focus on algorithmically verifying convolutions, the most resource-demanding operations in CNNs. We use checksums to verify convolutions. We identify the feasibility and performance-related challenges that arise in algorithmically detecting errors in convolutions in optimized CNN inference deployment platforms (e.g., TensorFlow or TensorRT on GPUs) that fuse multiple network layers and use reduced-precision operations, and demonstrate how to overcome them. We propose and evaluate variations of the algorithm-based error detection (ABED) techniques that offer implementation complexity, runtime overhead, and coverage trade-offs. Results show that ABED can detect all transient hardware errors that might otherwise corrupt output with low runtime overheads (6-23%). Only about 1.4% of the total computations in a CNN are not protected by ABED, which can be duplicated for full CNN protection. ABED for the compute-intensive convolutions and duplicating the rest can offer at least 1.6x throughput compared to full duplication.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
