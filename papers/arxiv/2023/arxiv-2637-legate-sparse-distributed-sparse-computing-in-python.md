---
id: arxiv-2637
title: "Legate Sparse: Distributed Sparse Computing in Python"
conference: arXiv 2023
date: 2023-11
authors:
  - name: "Melih Elibol"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Taylor Patti"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Bauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rohan Yadav"
    affiliation: ""
    is_industry: false
  - name: "Wonchan Lee"
    affiliation: ""
    is_industry: false
  - name: "Manolis Papadakis"
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
abstract: "The sparse module of the popular SciPy Python library is widely used across applications in scientific computing, data analysis and machine learning. The standard implementation of SciPy is restricted to a single CPU and cannot take advantage of modern distributed and accelerated computing resources"
url: "https://research.nvidia.com/publication/2023-11_legate-sparse-distributed-sparse-computing-python"
status: new
---

# Legate Sparse: Distributed Sparse Computing in Python

## 摘要

The sparse module of the popular SciPy Python library is widely used across applications in scientific computing, data analysis and machine learning. The standard implementation of SciPy is restricted to a single CPU and cannot take advantage of modern distributed and accelerated computing resources. We introduce Legate Sparse, a system that transparently distributes and accelerates unmodified sparse matrix-based SciPy programs across clusters of CPUs and GPUs, and composes with cuNumeric, a distributed NumPy library. Legate Sparse uses a combination of static and dynamic techniques to efficiently compose independently written sparse and dense array programming libraries, providing a unified Python interface for distributed sparse and dense array computations. We show that Legate Sparse is competitive with single-GPU libraries like CuPy and achieves 65% of the performance of PETSc on up to 1280 CPU cores and 192 GPUs of the Summit supercomputer, while offering the productivity benefits of idiomatic SciPy and NumPy.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
