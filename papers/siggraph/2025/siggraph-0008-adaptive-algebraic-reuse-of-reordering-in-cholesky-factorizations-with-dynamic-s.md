---
id: siggraph-0008
title: "Adaptive Algebraic Reuse of Reordering in Cholesky Factorizations with Dynamic Sparsity Patterns"
conference: SIGGRAPH 2025
date: 2025-06
authors:
  - name: "Maryam Mehri Dehnavi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Behrooz Zarebavani"
    affiliation: ""
    is_industry: false
  - name: "Danny Kaufman"
    affiliation: ""
    is_industry: false
  - name: "David Levin"
    affiliation: ""
    is_industry: false
topics:
  - CUDA_ecosystem
  - Graphics_rendering
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Computer Graphics"
  - "High Performance Computing"
  - "Programming Languages, Systems and Tools"
abstract: "We introduce Parth, a fill-reducing ordering method for sparse Cholesky solvers with dynamic sparsity patterns (e.g., in physics simulations with contact or geometry processing with local remeshing). Parth facilitates the selective reuse of fill-reducing orderings when sparsity patterns exhibit temp"
url: "https://research.nvidia.com/publication/2025-06_adaptive-algebraic-reuse-reordering-cholesky-factorizations-dynamic-sparsity"
status: new
---

# Adaptive Algebraic Reuse of Reordering in Cholesky Factorizations with Dynamic Sparsity Patterns

## 摘要

We introduce Parth, a fill-reducing ordering method for sparse Cholesky solvers with dynamic sparsity patterns (e.g., in physics simulations with contact or geometry processing with local remeshing). Parth facilitates the selective reuse of fill-reducing orderings when sparsity patterns exhibit temporal coherence, avoiding full symbolic analysis by localizing the effect of dynamic sparsity changes on the ordering vector. We evaluated Parth on over 175,000 linear systems collected from both physics simulations and geometry processing applications, and show that for some of the most challenging physics simulations, it achieves up to 14x reordering runtime speedup, resulting in a 2x speedup in Cholesky solve time—even on top of well-optimized solvers such as Apple Accelerate and Intel MKL.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
