---
id: arxiv-2562
title: "Composing Distributed Computations Through Task and Kernel Fusion"
conference: arXiv 2025
date: 2025-03
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
  - name: "Shiv Sundrum"
    affiliation: ""
    is_industry: false
  - name: "Wonchan Lee"
    affiliation: ""
    is_industry: false
  - name: "Alex Aiken"
    affiliation: ""
    is_industry: false
  - name: "Fredrik Kjolstad"
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
abstract: "We introduce Diffuse, a system that dynamically performs task and kernel fusion in distributed, task-based runtime systems. The key component of Diffuse is an intermediate representation of distributed computation that enables the necessary analyses for the fusion of distributed tasks to be performe"
url: "https://research.nvidia.com/publication/2025-03_composing-distributed-computations-through-task-and-kernel-fusion"
status: new
---

# Composing Distributed Computations Through Task and Kernel Fusion

## 摘要

We introduce Diffuse, a system that dynamically performs task and kernel fusion in distributed, task-based runtime systems. The key component of Diffuse is an intermediate representation of distributed computation that enables the necessary analyses for the fusion of distributed tasks to be performed in a scalable manner. We pair task fusion with a JIT compiler to fuse together the kernels within fused tasks. We show empirically that Diffuse’s intermediate representation is general enough to be a target for two real-world, task-based libraries (cuPyNumeric and Legate Sparse), letting Diffuse find optimization opportunities across function and library boundaries. Diffuse accelerates unmodified applications developed by composing task-based libraries by 1.86x on average (geo-mean), and by between 0.93x–10.7x on up to 128 GPUs. Diffuse also finds optimization opportunities missed by the original application developers, enabling high-level Python programs to match or exceed the performance of an explicitly parallel MPI library.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
