---
id: "arxiv-2792"
title: "GATSPI: GPU Accelerated Gate-Level Simulation for Power Improvement"
conference: "arXiv 2022"
date: "2022-03"
authors:
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Akshay Sridharan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Circuits and VLSI Design"
  - "High Performance Computing"
external_links:
  - name: "Preprint (ArXiv)"
    url: "https://arxiv.org/abs/2203.06117"
abstract: "In this paper, we present GATSPI, a novel GPU accelerated logic gate simulator that enables ultra-fast power estimation for industry sized ASIC designs with millions of gates. GATSPI is written in PyTorch with custom CUDA kernels for ease of coding and maintainability. It achieves simulation kernel "
url: "https://research.nvidia.com/publication/2022-03_gatspi-gpu-accelerated-gate-level-simulation-power-improvement"
status: "new"
---

# GATSPI: GPU Accelerated Gate-Level Simulation for Power Improvement

## 摘要

In this paper, we present GATSPI, a novel GPU accelerated logic gate simulator that enables ultra-fast power estimation for industry sized ASIC designs with millions of gates. GATSPI is written in PyTorch with custom CUDA kernels for ease of coding and maintainability. It achieves simulation kernel speedup of up to 1668X on a single-GPU system and up to 7412X on a multiple-GPU system when compared to a commercial gate-level simulator running on a single CPU core. GATSPI supports a range of simple to complex cell types from an industry standard cell library and SDF conditional delay statements without requiring prior calibration runs and produces industry-standard SAIF files from delay-aware gate-level simulation. Finally, we deploy GATSPI in a glitch-optimization flow, achieving a 1.4% power saving with a 449X speedup in turnaround time compared to a similar flow using a commercial simulator. &nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
