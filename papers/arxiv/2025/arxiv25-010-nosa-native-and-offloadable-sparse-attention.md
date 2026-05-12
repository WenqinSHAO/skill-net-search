---
id: arxiv25-010
title: "NOSA: Native and Offloadable Sparse Attention"
conference: "arXiv 2025"
date: "2025-03"
authors:
  - name: "Yuxiang Huang"
    affiliation: ""
    is_industry: false
  - name: "Chaojun Xiao"
    affiliation: ""
    is_industry: false
  - name: "Xu Han"
    affiliation: ""
    is_industry: false
  - name: "Zhiyuan Liu"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: "2510.13602"
url: "https://arxiv.org/abs/2510.13602"
status: analyzed
---
# NOSA: Native and Offloadable Sparse Attention

## 摘要

Trainable sparse attention can improve decoding efficiency in long-context processing, but existing methods leave the size of the KV cache unchanged, constraining on-GPU batch sizes and throughput. NOSA shows that trainable sparse attention naturally exhibits strong locality in token selection across adjacent decoding steps, enabling KV cache offloading without altering the underlying attention computation. Because inherent locality is insufficient to make offloading efficient on its own, NOSA introduces explicit locality constraints by decomposing token selection into query-aware and query-agnostic components, reducing KV transfers while preserving the same attention computation used during training. Extensive benchmarks show near-lossless performance with up to 2.3x decoding-throughput improvement over a vanilla trainable sparse attention baseline.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
