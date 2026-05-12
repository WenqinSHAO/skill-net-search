---
id: arxiv25-007
title: "CentroidKV: Efficient Long-Context LLM Inference via KV Cache Clustering"
conference: "arXiv 2025"
date: "2025-03"
authors:
  - name: "Jie Hu"
    affiliation: ""
    is_industry: false
  - name: "Shengnan Wang"
    affiliation: ""
    is_industry: false
  - name: "Yutong He"
    affiliation: ""
    is_industry: false
  - name: "Ping Gong"
    affiliation: ""
    is_industry: false
  - name: "Jiawei Yi"
    affiliation: ""
    is_industry: false
  - name: "Juncheng Zhang"
    affiliation: ""
    is_industry: false
  - name: "Youhui Bai"
    affiliation: ""
    is_industry: false
  - name: "Renhai Chen"
    affiliation: ""
    is_industry: false
  - name: "Gong Zhang"
    affiliation: ""
    is_industry: false
  - name: "Cheng Li"
    affiliation: ""
    is_industry: false
  - name: "Kun Yuan"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: "2506.11418"
url: "https://openreview.net/forum?id=T3EeupQhGj"
status: analyzed
---
# CentroidKV: Efficient Long-Context LLM Inference via KV Cache Clustering

## 摘要

Large language models with extended context windows pose substantial deployment challenges because of their KV cache footprint. CentroidKV introduces an online KV cache clustering framework based on the observation that key states exhibit high similarity along the sequence dimension. It divides the sequence into chunks, applies Chunked Soft Matching within each chunk, and merges each cluster into a centroid. Extensive experiments across multiple models and long-context benchmarks show that CentroidKV can reduce KV cache memory usage by up to 75% while maintaining comparable model performance, accelerate decoding by up to 1.92x, and increase serving throughput by up to 4x with low computational overhead.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
