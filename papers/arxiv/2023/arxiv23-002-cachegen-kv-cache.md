---
id: arxiv23-002
title: "CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving"
conference: arXiv 2023
date: 2023-10
authors:
  - name: "Yuhan Liu"
    affiliation: ""
    is_industry: false
  - name: "Hanchen Li"
    affiliation: ""
    is_industry: false
  - name: "Yihua Cheng"
    affiliation: ""
    is_industry: false
  - name: "Siddhant Ray"
    affiliation: ""
    is_industry: false
  - name: "Yuyang Huang"
    affiliation: ""
    is_industry: false
  - name: "Qizheng Zhang"
    affiliation: ""
    is_industry: false
  - name: "Kuntai Du"
    affiliation: ""
    is_industry: false
  - name: "Jiayi Yao"
    affiliation: ""
    is_industry: false
  - name: "Shan Lu"
    affiliation: ""
    is_industry: false
  - name: "Ganesh Ananthanarayanan"
    affiliation: ""
    is_industry: true
  - name: "Michael Maire"
    affiliation: ""
    is_industry: false
  - name: "Henry Hoffmann"
    affiliation: ""
    is_industry: false
  - name: "Ari Holtzman"
    affiliation: ""
    is_industry: false
  - name: "Junchen Jiang"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [cachegen, kv-cache-compression, streaming, network-transfer]
arxiv: "2310.07240"
url: "https://arxiv.org/abs/2310.07240"
status: analyzed
---

# CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving

**arXiv 2023** | SIGCOMM 2024 | arXiv: 2310.07240

## 摘要

As large language models (LLMs) take on complex tasks, their inputs are supplemented with longer contexts that incorporate domain knowledge. Yet using long contexts is challenging, as nothing can be generated until the whole context is processed by the LLM. While the context-processing delay can be reduced by reusing the KV cache of a context across different inputs, fetching the KV cache, which contains large tensors, over the network can cause high extra network delays. CacheGen is a fast context-loading module for LLM systems. First, CacheGen uses a custom tensor encoder, leveraging KV cache's distributional properties to encode a KV cache into more compact bitstream representations with negligible decoding overhead, to save bandwidth usage. Second, CacheGen adapts the compression level of different parts of a KV cache to cope with changes in available bandwidth, in order to maintain low context-loading delay and high generation quality. When available bandwidth drops, CacheGen may raise the compression level for a part of the context or recompute its KV cache on the fly. We test CacheGen on popular LLMs and datasets. Compared to the recent systems that reuse the KV cache, CacheGen reduces the KV cache size by 3.5-4.3x and the total delay in fetching and processing contexts by 3.2-3.7x with negligible impact on the LLM response quality.

## 核心贡献

- 提出 CacheGen，KV cache 压缩 + 流式传输模块
- 自定义张量编码器，利用 KV cache 分布特性压缩为紧凑比特流
- 自适应压缩级别，根据可用带宽动态调整
- KV cache 大小减少 3.5-4.3×，总延迟降低 3.2-3.7×
- 对 LLM 生成质量影响可忽略
- 代码已开源

---
*导入自 net-research 数据库 | ID: arxiv23-002*
