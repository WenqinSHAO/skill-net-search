---
id: "iclr-0007"
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
conference: "ICLR 2025"
date: "2025-04"
authors:
  - name: "Songlin Yang"
    affiliation: "MIT"
    is_industry: false
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ali Hatamizadeh"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Natural Language Processing"
external_links:
  - name: "https://arxiv.org/abs/2412.06464v1"
    url: "https://github.com/NVlabs/GatedDeltaNet"
abstract: "Linear Transformers have gained attention as efficient alternatives to standard Transformers, but their performance in retrieval and long-context tasks has been limited. To address these limitations, recent work has explored two distinct mechanisms: gating for adaptive memory control and the delta u"
url: "https://research.nvidia.com/publication/2025-04_gated-delta-networks-improving-mamba2-delta-rule"
status: "new"
---

# Gated Delta Networks: Improving Mamba2 with Delta Rule

## 摘要

Linear Transformers have gained attention as efficient alternatives to standard Transformers, but their performance in retrieval and long-context tasks has been limited. To address these limitations, recent work has explored two distinct mechanisms: gating for adaptive memory control and the delta update rule for precise memory modifications. We observe that these mechanisms are complementary: gating enables rapid memory erasure while the delta rule facilitates targeted updates. Building on this insight, we introduce the gated delta rule and develop a parallel training algorithm optimized for modern hardware. Our proposed architecture, Gated DeltaNet, consistently surpasses existing models like Mamba2 and DeltaNet across multiple benchmarks, including language modeling, common-sense reasoning, in-context retrieval, length extrapolation, and long-context understanding. We further enhance performance by developing hybrid architectures that combine Gated DeltaNet layers with sliding window attention or Mamba2 layers, achieving both improved training efficiency and superior task performance.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
