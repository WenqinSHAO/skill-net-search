---
id: "arxiv-2551"
title: "GEM: GPU-Accelerated Emulator-Inspired RTL Simulation"
conference: "arXiv 2025"
date: "2025-06"
authors:
  - name: "Zizheng Guo"
    affiliation: "Peking Univeristy"
    is_industry: false
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Circuits and VLSI Design"
external_links:
  - name: "Github code release"
    url: "https://github.com/NVlabs/GEM"
abstract: "We present a GPU-accelerated RTL simulator addressing critical challenges in high-speed circuit verification.Traditional CPU-based RTL simulators struggle with scalability and performance, and while FPGA-based emulators offer acceleration, they are costly and less accessible. Previous GPU-based atte"
url: "https://research.nvidia.com/publication/2025-06_gem-gpu-accelerated-emulator-inspired-rtl-simulation"
status: "new"
---

# GEM: GPU-Accelerated Emulator-Inspired RTL Simulation

## 摘要

We present a GPU-accelerated RTL simulator addressing critical challenges in high-speed circuit verification.Traditional CPU-based RTL simulators struggle with scalability and performance, and while FPGA-based emulators offer acceleration, they are costly and less accessible. Previous GPU-based attempts have failed to speed up RTL simulation due to the heterogeneous nature of circuit partitions, which conflicts with the SIMT (Single Instruction, Multiple Thread) paradigm of GPUs. Inspired by the design of emulators, our approach introduces a novel virtual Very Long Instruction Word (VLIW) architecture, designed for efficient CUDA execution. We also design a flow that maps circuit logic to the architecture in a process analogous to the FPGA CAD flow. This architecture mitigates issues of irregular memory access and thread divergence, unlocking GPU potential for RTL simulation. Our solution achieves up to 64°ø speed-up over the best CPU simulators, democratizing high-speed RTL simulation with accessible hardware and establishing a new frontier for GPU-accelerated circuit verification.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
