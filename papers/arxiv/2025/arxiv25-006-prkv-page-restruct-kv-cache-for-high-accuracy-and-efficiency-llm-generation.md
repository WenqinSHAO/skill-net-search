---
id: arxiv25-006
title: "PRKV: Page Restruct KV Cache for High Accuracy and Efficiency LLM Generation"
conference: "arXiv 2025"
date: "2025-03"
authors:
  - name: "Fang Wu"
    affiliation: ""
    is_industry: false
  - name: "Congming Gao"
    affiliation: ""
    is_industry: false
  - name: "Weixi Zhu"
    affiliation: ""
    is_industry: false
  - name: "Jiwu Shu"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: ""
url: "https://openreview.net/forum?id=7FM0GBFhe5"
status: analyzed
---
# PRKV: Page Restruct KV Cache for High Accuracy and Efficiency LLM Generation

## 摘要

As the key-value (KV) cache size scales with context length, accessing large KV cache each step and substantial GPU memory demand challenge us to deploy LLMs with long contexts. Offloading-based KV retrieval preserves the entire KV cache in CPU memory and dynamically retrieves the most relevant KV pairs for each decoding step, which can preserve quality and reduce GPU memory consumption. However, existing page-level retrieval introduces inaccurate KV selection and significant retrieval overhead. PRKV jointly optimizes algorithm and system for page-level KV retrieval with KV offloading. On the algorithm side, PRKV introduces hybrid KV selection that combines static and dynamic selection strategies. On the system side, PRKV employs contiguous memory indexing and batched transfer optimizations to improve retrieval efficiency. Experiments demonstrate improved accuracy across scenarios and models, with up to 6.75x speedup over prior KV retrieval methods.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
