---
id: arxiv-3013
title: "Making Convolutions Resilient via Algorithm-Based Error Detection Techniques"
conference: arXiv 2020
date: 2020-06
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
abstract: "The ability of Convolutional Neural Networks (CNNs) to accurately process real-time telemetry has boosted their use in safety-critical and high-performance computing systems. As such systems require high levels of resilience to errors, CNNs must execute correctly in the presence of hardware faults. "
url: "https://research.nvidia.com/publication/2020-06_making-convolutions-resilient-algorithm-based-error-detection-techniques"
status: new
---

# Making Convolutions Resilient via Algorithm-Based Error Detection Techniques

## 摘要

The ability of Convolutional Neural Networks (CNNs) to accurately process real-time telemetry has boosted their use in safety-critical and high-performance computing systems. As such systems require high levels of resilience to errors, CNNs must execute correctly in the presence of hardware faults. Full duplication provides the needed assurance but incurs a prohibitive 100% overhead. Algorithmic techniques are known to offer low-cost solutions, but the practical feasibility and performance of such techniques have never been studied for CNN deployment platforms (e.g., TensorFlow or TensorRT on GPUs). In this paper, we focus on algorithmically verifying Convolutions, which are the most resource-demanding operations in CNNs. We use checksums to verify convolutions, adding a small amount of redundancy, far less than full-duplication. We first identify the challenges that arise in employing Algorithm-Based Error Detection (ABED) for Convolutions in optimized inference platforms that fuse multiple network layers and use reduced-precision operations, and demonstrate how to overcome them. We propose and evaluate variations of ABED techniques that offer implementation complexity, runtime overhead, and coverage trade-offs. Results show that ABED can detect all transient hardware errors that might otherwise corrupt output and does so while incurring low runtime overheads (6-23%), offering at least 1.6X throughput to workloads compared to full duplication.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
