---
id: arxiv-2661
title: "Implicit Memory Tagging: No-Overhead Memory Safety Using Alias-Free Tagged ECC"
conference: arXiv 2023
date: 2023-06
authors:
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mohamed Tarek Ibn Ziad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aamer Jaleel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen W. Keckler"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Miscellaneous
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Resilience and Safety"
  - "Security"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/abs/10.1145/3579371.3589102"
abstract: "Memory safety is a major security concern for unsafe programming languages, including C/C++ and CUDA/OpenACC. Hardware-accelerated memory tagging is an effective mechanism for detecting memory safety violations; however, its adoption is challenged by significant meta-data storage and memory traffic "
url: "https://research.nvidia.com/publication/2023-06_implicit-memory-tagging-no-overhead-memory-safety-using-alias-free-tagged-ecc"
status: new
---

# Implicit Memory Tagging: No-Overhead Memory Safety Using Alias-Free Tagged ECC

## 摘要

Memory safety is a major security concern for unsafe programming languages, including C/C++ and CUDA/OpenACC. Hardware-accelerated memory tagging is an effective mechanism for detecting memory safety violations; however, its adoption is challenged by significant meta-data storage and memory traffic overheads. This paper proposes Implicit Memory Tagging (IMT), a novel approach that provides no-overhead hardware-accelerated memory tagging by leveraging the system error correcting code (ECC) to check for the equivalence of a memory tag in addition to its regular duties of detecting and correcting data errors. Implicit Memory Tagging relies on a new class of ECC codes called Alias-Free Tagged ECC (AFT-ECC) that can unambiguously identify tag mismatches in the absence of data errors, while maintaining the efficacy of ECC when data errors are present. When applied to GPUs, IMT addresses the increasing importance of GPU memory safety and the costs of adding meta-data to GPU memory. Ultimately, IMT detects memory safety violations without meta-data storage or memory access overheads. In practice, IMT can provide larger tag sizes than existing industry memory tagging implementations, enhancing security.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
