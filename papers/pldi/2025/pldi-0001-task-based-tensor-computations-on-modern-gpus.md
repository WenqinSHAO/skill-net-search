---
id: pldi-0001
title: "Task-Based Tensor Computations on Modern GPUs"
conference: PLDI 2025
date: 2025-06
authors:
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Bauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rohan Yadav"
    affiliation: ""
    is_industry: false
  - name: "Alex Aiken"
    affiliation: ""
    is_industry: false
topics:
  - CUDA_ecosystem
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "High Performance Computing"
  - "Programming Languages, Systems and Tools"
abstract: "Domain-specific, fixed-function units are becoming increasingly common in modern processors. As the computational demands of applications evolve, the capabilities and programming interfaces of these fixed-function units continue to change. NVIDIA’s Hopper GPU architecture contains multiple fixed-fun"
url: "https://research.nvidia.com/publication/2025-06_task-based-tensor-computations-modern-gpus"
status: new
---

# Task-Based Tensor Computations on Modern GPUs

## 摘要

Domain-specific, fixed-function units are becoming increasingly common in modern processors. As the computational demands of applications evolve, the capabilities and programming interfaces of these fixed-function units continue to change. NVIDIA’s Hopper GPU architecture contains multiple fixed-function units per compute unit, including an asynchronous data movement unit (TMA) and an asynchronous matrix multiplication unit (Tensor Core). Efficiently utilizing these units requires a fundamentally different programming style than previous architectures; programmers must now develop warp-specialized kernels that orchestrate producer-consumer pipelines between the asynchronous units. To manage the complexity of programming these new architectures, we introduce Cypress, a task-based programming model with sequential semantics. Cypress programs are a set of designated functions called tasks that operate on tensors and are free of communication and synchronization. Cypress programs are bound to the target machine through a mapping specification that describes where tasks should run and in which memories tensors should be materialized. We present a compiler architecture that lowers Cypress programs into CUDA programs that perform competitively with expert-written codes. Cypress achieves 0.88x-1.06x the performance of cuBLAS on GEMM, and between 0.80x-0.98x the performance of the currently best-known Flash Attention implementation while eliminating all aspects of explicit data movement and asynchronous computation from application code.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
