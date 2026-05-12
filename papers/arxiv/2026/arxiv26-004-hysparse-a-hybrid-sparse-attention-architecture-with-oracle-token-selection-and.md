---
id: arxiv26-004
title: "HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing"
conference: "arXiv 2026"
date: "2026-03"
authors:
  - name: "Yizhao Gao"
    affiliation: ""
    is_industry: false
  - name: "Jianyu Wei"
    affiliation: ""
    is_industry: false
  - name: "Qihao Zhang"
    affiliation: ""
    is_industry: false
  - name: "Yu Cheng"
    affiliation: ""
    is_industry: false
  - name: "Shimao Chen"
    affiliation: ""
    is_industry: false
  - name: "Zhengju Tang"
    affiliation: ""
    is_industry: false
  - name: "Zihan Jiang"
    affiliation: ""
    is_industry: false
  - name: "Yifan Song"
    affiliation: ""
    is_industry: false
  - name: "Hailin Zhang"
    affiliation: ""
    is_industry: false
  - name: "Liang Zhao"
    affiliation: ""
    is_industry: false
  - name: "Bo Yang"
    affiliation: ""
    is_industry: false
  - name: "Gang Wang"
    affiliation: ""
    is_industry: false
  - name: "Shijie Cao"
    affiliation: ""
    is_industry: false
  - name: "Fuli Luo"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: "2602.03560"
url: "https://arxiv.org/abs/2602.03560"
status: analyzed
---
# HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing

## 摘要

HySparse interleaves each full attention layer with several sparse attention layers and derives each sparse layer's token selection and KV caches directly from the preceding full attention layer. This resolves two limitations of prior sparse attention methods: they often require extra proxies to predict token importance, and they reduce computation without saving KV cache. HySparse uses the full attention layer as an oracle for token selection and enables sparse attention layers to reuse the full-attention KV cache, reducing both computation and memory. Evaluations on both 7B dense and 80B MoE models show substantial performance gains while reducing KV cache storage by nearly 10x.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
