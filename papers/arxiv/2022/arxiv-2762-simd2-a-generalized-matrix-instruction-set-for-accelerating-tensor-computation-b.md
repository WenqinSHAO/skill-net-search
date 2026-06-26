---
id: "arxiv-2762"
title: "SIMD^2: A Generalized Matrix Instruction Set for Accelerating Tensor Computation beyond GEMM"
conference: "arXiv 2022"
date: "2022-06"
authors:
  - name: "Yunan Zhang"
    affiliation: "University of California, Riverside"
    is_industry: false
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hung-Wei Tseng"
    affiliation: "University of California, Riverside"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3470496.3527411"
abstract: "Matrix-multiplication units (MXUs) are now prevalent in every computing platform. The key attribute that makes MXUs so successful is the semiring structure, which allows tiling for both parallelism and data reuse. Nonetheless, matrix-multiplication is not the only algorithm with such attributes. We "
url: "https://research.nvidia.com/publication/2022-06_simd2-generalized-matrix-instruction-set-accelerating-tensor-computation-beyond"
status: "new"
---

# SIMD^2: A Generalized Matrix Instruction Set for Accelerating Tensor Computation beyond GEMM

## 摘要

Matrix-multiplication units (MXUs) are now prevalent in every computing platform. The key attribute that makes MXUs so successful is the semiring structure, which allows tiling for both parallelism and data reuse. Nonetheless, matrix-multiplication is not the only algorithm with such attributes. We find that many algorithms share the same structure and differ in only the core operation; for example, using add-minimum instead of multiply-add. Algorithms with a semiring-like structure therefore have potential to be accelerated by a general-purpose matrix operation architecture, instead of common MXUs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
