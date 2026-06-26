---
id: "arxiv-3056"
title: "Fearless Concurrency on the GPU"
conference: "arXiv 2026"
date: "2026-06"
authors:
  - name: "Melih Elibol"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jared Roesch"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Isaac Gelado"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eric Buehler"
    affiliation: "Hugging Face"
    is_industry: false
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "High Performance Computing"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "Source code (GitHub)"
    url: "https://github.com/nvlabs/cutile-rs"
abstract: "Rust has made safe systems programming practical on the CPU, but writing custom GPU kernels in Rust still forces programmers outside the language's ownership guarantees. We present cuTile Rust, a tile-based system for safe, idiomatic GPU kernel authoring in Rust. cuTile Rust extends Rust's ownership"
url: "https://research.nvidia.com/publication/2026-06_fearless-concurrency-gpu"
status: "new"
---

# Fearless Concurrency on the GPU

## 摘要

Rust has made safe systems programming practical on the CPU, but writing custom GPU kernels in Rust still forces programmers outside the language's ownership guarantees. We present cuTile Rust, a tile-based system for safe, idiomatic GPU kernel authoring in Rust. cuTile Rust extends Rust's ownership discipline to tile-based GPU kernels: mutable outputs are split into disjoint pieces, kernel launches preserve the host-side ownership contract, and programmers can opt out locally when they need lower-level control. The system also provides a composable host execution model spanning synchronous launches, asynchronous pipelines, and CUDA graph replay.Our evaluation shows that these abstractions can preserve performance on high-end GPUs. On the NVIDIA B200 GPU, cuTile Rust achieves 7 TB/s for element-wise operations and 2 PFlop/s for GEMM (96% of cuBLAS), matching cuTile Python within measurement noise. Grout, a cuTile-Rust-based inference engine, exercises cuTile Rust across an end-to-end Qwen3 inference path. In batch-1 decode, Grout reaches 171 generated tokens/s for Qwen3-4B on the NVIDIA GeForce RTX 5090 and 82 generated tokens/s for Qwen3-32B on the B200, competitive with vLLM and SGLang and consistent with an HBM roofline sanity check.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
