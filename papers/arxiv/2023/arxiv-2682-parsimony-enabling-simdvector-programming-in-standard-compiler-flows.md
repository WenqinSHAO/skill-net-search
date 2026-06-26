---
id: "arxiv-2682"
title: "Parsimony: Enabling SIMD/Vector Programming in Standard Compiler Flows"
conference: "arXiv 2023"
date: "2023-02"
authors:
  - name: "Vijay Kandiah"
    affiliation: "Northwestern University"
    is_industry: false
  - name: "Daniel Lustig"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oreste Villa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nikos Hardavellas"
    affiliation: "Northwestern University"
    is_industry: false
topics:
  - CUDA_ecosystem
  - GPU_architecture
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "High Performance Computing"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3579990.3580019"
abstract: "Achieving peak throughput on modern CPUs requires maximizing the use of single-instruction, multiple-data (SIMD) or vector compute units. Single-program, multiple-data (SPMD) programming models are an effective way to use high-level programming languages to target these ISAs. Unfortunately, many SPM"
url: "https://research.nvidia.com/publication/2023-02_parsimony-enabling-simdvector-programming-standard-compiler-flows"
status: "new"
---

# Parsimony: Enabling SIMD/Vector Programming in Standard Compiler Flows

## 摘要

Achieving peak throughput on modern CPUs requires maximizing the use of single-instruction, multiple-data (SIMD) or vector compute units. Single-program, multiple-data (SPMD) programming models are an effective way to use high-level programming languages to target these ISAs. Unfortunately, many SPMD frameworks have evolved to have either overly restrictive language specifications or under-specified programming models, and this has slowed the widescale adoption of SPMD-style programming. This paper introduces Parsimony (PARallel SIMd), a SPMD programming approach built with semantics designed to be compatible with multiple languages and to cleanly integrate into the standard optimizing&nbsp;compiler toolchains for those languages.&nbsp; We first explain the Parsimony programming model semantics and how they enable a standalone compiler IR-to-IR pass that can perform vectorization independently of other passes, improving the language and toolchain compatibility of SPMD programming.&nbsp; We then demonstrate a LLVM prototype of the Parsimony approach that matches the performance of ispc, a popular but more restrictive SPMD approach, and achieves 97% of the performance of hand-written AVX-512 SIMD intrinsics on over 70 benchmarks ported from the Simd Library. We finally discuss where Parsimony has exposed parts of existing language and compiler flows where slight improvements could further enable improved SPMD program vectorization.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
