---
id: arxiv26-005
title: "LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents"
conference: "arXiv 2026"
date: "2026-03"
authors:
  - name: "Hyesung Jeon"
    affiliation: ""
    is_industry: false
  - name: "Hyeongju Ha"
    affiliation: ""
    is_industry: false
  - name: "Jae-Joon Kim"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: "2602.01053"
url: "https://arxiv.org/abs/2602.01053"
status: analyzed
---
# LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents

## 摘要

Role-specialized multi-agent systems often use multiple LoRA adapters on top of a shared pretrained backbone, but each agent still builds and stores its own KV cache for the same long trajectories. LRAgent decomposes the cache into a shared base component induced by the pretrained backbone and an adapter-dependent low-rank component induced by the LoRA weights. By sharing the base component and compactly storing the low-rank component, it reduces both memory and compute overhead while preserving accuracy near the non-shared baseline.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
