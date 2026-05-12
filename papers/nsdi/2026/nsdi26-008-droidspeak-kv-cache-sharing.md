---
id: nsdi26-008
title: "DroidSpeak: KV Cache Sharing for Cross-LLM Communication and Multi-LLM Serving"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yuhan Liu"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Yuyang Huang"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Jiayi Yao"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Shaoting Feng"
    affiliation: ""
    is_industry: false
  - name: "Zhuohan Gu"
    affiliation: ""
    is_industry: false
  - name: "Kuntai Du"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Hanchen Li"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Yihua Cheng"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Junchen Jiang"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Shan Lu"
    affiliation: "University of Chicago"
    is_industry: false
  - name: "Madan Musuvathi"
    affiliation: "Microsoft Research"
    is_industry: true
  - name: "Esha Choukse"
    affiliation: "Microsoft Research"
    is_industry: true
topics:
  - LLM Serving
  - Distributed Systems
tags: [droidspeak, kv-cache-sharing, cross-llm, multi-llm]
arxiv: "2411.02820"
url: "https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan"
status: analyzed
---

# DroidSpeak: KV Cache Sharing for Cross-LLM Communication and Multi-LLM Serving

**NSDI 2026** | arXiv: 2411.02820

## 摘要

Compound AI systems, such as agentic systems, are an emerging trend in large-scale enterprise settings, with multiple LLMs specialized for different users, tasks, and/or roles working together. In these scenarios, different models often process inputs that share the same context prefix. Although much work was done in the past to enable the reuse of prefix KV caches across inputs for a single model, how to enable one model to reuse the prefix KV caches of a different model remains an open question. We introduce DroidSpeak, the first distributed LLM inference system that enables KV cache reuse across distributed nodes running inference of different LLMs, so long as the LLMs have the same architecture. We present the first study that aims at understanding the impact of sharing KV caches across different LLMs, and if/when such sharing affects quality. Inspired by the findings, we present DroidSpeak, which selectively recomputes a few layers of the KV cache produced by another LLM and reuses the remaining layers, with negligible quality loss. Moreover, carefully pipelining the layer-wise re-computation and the loading of reused KV cache further improves the inference performance. Experiments on diverse datasets and model pairs demonstrate that DroidSpeak achieves up to 4× throughput improvement and about 3.1× faster prefill (time to first token), with negligible loss of quality in F1 scores, Rouge-L or code similarity score, compared to the baseline which does not allow any sharing across models.

## 核心贡献

- 首个支持跨不同 LLM 的 KV cache 复用的分布式推理系统
- 只要 LLM 架构相同，即可跨模型复用 KV cache
- 选择性重计算少量层，复用其余层的 KV cache，质量损失可忽略
- 层级重计算与 KV cache 加载精细流水线化，提升推理性能
- 最高 4× 吞吐量提升，3.1× 更快的 prefill (TTFT)
- F1、Rouge-L、代码相似度损失可忽略

---
*导入自 net-research 数据库 | ID: nsdi26-008*
