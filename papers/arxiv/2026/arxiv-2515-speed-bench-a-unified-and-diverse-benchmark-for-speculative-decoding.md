---
id: arxiv-2515
title: "SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding"
conference: arXiv 2026
date: 2026-02
authors:
  - name: "Talor Abramovich"
    affiliation: ""
    is_industry: false
  - name: "Maor Ashkenazi"
    affiliation: ""
    is_industry: false
  - name: "Carl Putterman"
    affiliation: ""
    is_industry: false
  - name: "Benjamin Chislett"
    affiliation: ""
    is_industry: false
  - name: "Tiyasa Mitra"
    affiliation: ""
    is_industry: false
  - name: "Bita Darvish Rouhani"
    affiliation: ""
    is_industry: false
  - name: "Ran Zilberstein"
    affiliation: ""
    is_industry: false
  - name: "Yonatan Geifman"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
abstract: "Speculative Decoding (SD) has emerged as a critical technique for accelerating Large Language Model (LLM) inference. Unlike deterministic system optimizations, SD performance is inherently data-dependent, meaning that diverse and representative workloads are essential for accurately measuring its ef"
url: "https://research.nvidia.com/publication/2026-02%5Fspeed-bench-unified-and-diverse-benchmark-speculative-decoding"
status: new
---

# SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding

## 摘要

Speculative Decoding (SD) has emerged as a critical technique for accelerating Large Language Model (LLM) inference. Unlike deterministic system optimizations, SD performance is inherently data-dependent, meaning that diverse and representative workloads are essential for accurately measuring its effectiveness. Existing benchmarks suffer from limited task diversity, inadequate support for throughput-oriented evaluation, and a reliance on high-level implementations that fail to reflect production environments. To address this, we introduce SPEED-Bench, a comprehensive suite designed to standardize SD evaluation across diverse semantic domains and realistic serving regimes. SPEED-Bench offers a carefully curated qualitative data split, selected by prioritizing semantic diversity across the data samples. Additionally, it includes a Throughput data split, allowing speedup evaluation across a range of concurrencies, from latency-sensitive low-batch settings to throughput-oriented high-load scenarios. By integrating with production engines like vLLM and TensorRT-LLM, SPEED-Bench allows practitioners to analyze system behaviors often masked by other benchmarks. We highlight this by quantifying how synthetic inputs overestimate real-world throughput, identifying batch-size dependent optimal draft lengths and biases in low-diversity data, and analyzing the caveats of vocabulary pruning in state-of-the-art drafters. We release SPEEDBench to establish a unified evaluation standard for practical comparisons of SD algorithms.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
