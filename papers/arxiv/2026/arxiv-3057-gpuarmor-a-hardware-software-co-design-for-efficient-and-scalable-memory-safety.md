---
id: "arxiv-3057"
title: "GPUArmor: A Hardware-Software Co-design for Efficient and Scalable Memory Safety on GPUs"
conference: "arXiv 2026"
date: "2026-05"
authors:
  - name: "Mohamed Tarek Ibn Ziad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sana Damani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aamer Jaleel"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Miscellaneous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Security"
abstract: "Memory safety errors continue to pose a significant threat to current computing systems, and graphics processing units (GPUs) are no exception. A prominent class of memory safety algorithms is allocation-based solutions. The key idea is to maintain each allocation’s metadata (base address and size) "
url: "https://research.nvidia.com/publication/2026-05_gpuarmor-hardware-software-co-design-efficient-and-scalable-memory-safety-gpus"
status: "new"
---

# GPUArmor: A Hardware-Software Co-design for Efficient and Scalable Memory Safety on GPUs

## 摘要

Memory safety errors continue to pose a significant threat to current computing systems, and graphics processing units (GPUs) are no exception. A prominent class of memory safety algorithms is allocation-based solutions. The key idea is to maintain each allocation’s metadata (base address and size) in a disjoint table and retrieve it at runtime to verify memory accesses. While several previous solutions have adopted allocation-based algorithms (e.g., cuCatch [39 ] and GPUShield [ 18 ]), they typically suffer from high memory overheads or scalability problems. In this work, we examine the key characteristics of real-world GPU workloads and observe several differences between GPU and CPU applications regarding memory access patterns, memory footprint, number of live allocations, and active allocation working set. Our observations motivate GPUArmor, a hardware-software co-design framework for memory safety on GPUs. We show that a simple compiler analysis combined with lightweight hardware support can help prevent spatial and temporal memory violations on modern GPU workloads with 8% average run time overheads while cuCatch incurs nearly 36% overhead. In fact, GPUArmor achieves speed-of-light performance with negligible storage requirements. This result benefits both base and bounds solutions and memory tagging techniques, which we showcase with GPUArmor-Binary, a variation of GPUArmor that does not require recompilation, and achieves 2.2% slowdowns while significantly reducing storage overheads beyond traditional memory tagging approaches

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
