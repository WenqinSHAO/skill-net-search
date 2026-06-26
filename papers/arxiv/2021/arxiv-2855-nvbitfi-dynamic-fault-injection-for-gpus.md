---
id: "arxiv-2855"
title: "NVBitFI: Dynamic Fault Injection for GPUs"
conference: "arXiv 2021"
date: "2021-06"
authors:
  - name: "Timothy Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oreste Villa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
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
    url: "https://ieeexplore.ieee.org/abstract/document/9505068"
abstract: "GPUs have found wide acceptance in domains such as high-performance computing and autonomous vehicles, which require fast processing of large amounts of data along with provisions for reliability, availability, and safety. A key component of these dependability characteristics is the propagation of "
url: "https://research.nvidia.com/publication/2021-06_nvbitfi-dynamic-fault-injection-gpus"
status: "new"
---

# NVBitFI: Dynamic Fault Injection for GPUs

## 摘要

GPUs have found wide acceptance in domains such as high-performance computing and autonomous vehicles, which require fast processing of large amounts of data along with provisions for reliability, availability, and safety. A key component of these dependability characteristics is the propagation of errors and their eventual effect on system outputs. In addition to analytical and simulation models, fault injection is an important technique that can evaluate the effect of errors on a complete computing system running the full software stack. However, the complexity of modern GPU systems and workloads challenges existing fault injection tools. Some tools require the recompilation of source code that may not be available, struggle to handle dynamic libraries, lack support for modern GPUs, or add unacceptable performance overheads. We introduce the NVBitFI tool for fault injection into GPU programs. In contrast with existing tools, NVBitFI performs instrumentation of code dynamically and selectively to instrument the minimal set of target dynamic kernels; as it requires no access to source code, NVBitFI provides improvements in performance and usability. The NVBitFI tool is publicly available for download and use at https://github.com/NVlabs/nvbitfi.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
