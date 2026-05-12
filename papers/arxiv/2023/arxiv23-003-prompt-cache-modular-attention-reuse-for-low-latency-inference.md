---
id: arxiv23-003
title: "Prompt Cache: Modular Attention Reuse for Low-Latency Inference"
conference: "arXiv 2023"
date: "2023-03"
authors:
  - name: "In Gim"
    affiliation: ""
    is_industry: false
  - name: "Guojun Chen"
    affiliation: ""
    is_industry: false
  - name: "Seung-seob Lee"
    affiliation: ""
    is_industry: false
  - name: "Nikhil Sarda"
    affiliation: ""
    is_industry: false
  - name: "Anurag Khandelwal"
    affiliation: ""
    is_industry: false
  - name: "Lin Zhong"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: "2311.04934"
url: "https://arxiv.org/abs/2311.04934"
status: analyzed
---
# Prompt Cache: Modular Attention Reuse for Low-Latency Inference

## 摘要

Prompt Cache accelerates LLM inference by reusing precomputed attention states across different prompts. Many prompts contain overlapping text segments such as system messages, prompt templates, and documents. Prompt Cache introduces reusable prompt modules defined in a schema and caches their attention states for later reuse. By concatenating cached module states and computing attention only for uncached segments, it significantly reduces time-to-first-token while preserving output accuracy across several LLMs.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
