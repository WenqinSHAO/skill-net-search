---
id: arxiv26-003
title: "Joint Encoding of KV-Cache Blocks for Scalable LLM Serving"
conference: arXiv 2026
date: 2026-01
authors:
  - name: "Joseph Kampeas"
    affiliation: ""
    is_industry: false
  - name: "Emir Haleva"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [joint-encoding, kv-cache-compression, scalable-serving]
arxiv: "2601.03067"
url: "https://arxiv.org/abs/2601.03067"
status: analyzed
---

# Joint Encoding of KV-Cache Blocks for Scalable LLM Serving

**arXiv 2026** | arXiv: 2601.03067

## 摘要

Modern large language models (LLMs) drive interactive AI systems but are bottlenecked by the memory-heavy growth of key-value (KV) caches, which limits real-time throughput under concurrent loads. Existing KV-cache compression methods rely on rigid heuristics, disrupt tensor layouts, or require specialized compute, hindering scalability and deployment. We propose joint encoding of KV-cache blocks, which fuses similar blocks across requests and input chunks into shared representations while preserving standard cache structure. This alleviates the KV-cache memory bottleneck, supporting high-concurrency serving without specialized hardware. Theoretically, we analyze the rate-distortion tradeoff of fused cache blocks under a Poisson process model. Empirically, our method achieves up to 4.38 × KV-cache compression with negligible accuracy loss across diverse LLMs and benchmarks, outperforming recent structured and adaptive compression baselines. In real LLM serving, joint encoding improves the token throughput by ∼40% on a single-machine vLLM benchmark, demonstrating substantial gains in inference throughput.

## 核心贡献

- 提出 KV-cache blocks 的联合编码（joint encoding）
- 跨请求和输入块融合相似 blocks 为共享表示
- 保持标准 cache 结构，不破坏张量布局
- 理论上分析 Poisson 过程模型下的速率-失真权衡
- 最高 4.38× KV-cache 压缩，准确率损失可忽略
- 单机上 vLLM benchmark：token 吞吐量提升 ∼40%
- 代码已开源：https://github.com/sef1/kv_fast_fusion kv_joint_encoding

---
*导入自 net-research 数据库 | ID: arxiv26-003*