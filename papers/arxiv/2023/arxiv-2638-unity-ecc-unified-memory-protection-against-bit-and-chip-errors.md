---
id: arxiv-2638
title: "Unity ECC: Unified Memory Protection Against Bit and Chip Errors"
conference: arXiv 2023
date: 2023-11
authors:
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dongwhee Kim"
    affiliation: ""
    is_industry: false
  - name: "Jaeyoon Lee"
    affiliation: ""
    is_industry: false
  - name: "Wonyeong Jung"
    affiliation: ""
    is_industry: false
  - name: "Jungrae Kim"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/abs/10.1145/3581784.3607081"
abstract: "DRAM vendors utilize On-Die Error Correction Codes (OD-ECC) to correct random bit errors internally. Meanwhile, system companies utilize Rank-Level ECC (RL-ECC) to protect data against chip errors. Separate protection increases the redundancy ratio to 32.8% in DDR5 and incurs significant performance"
url: "https://research.nvidia.com/publication/2023-11_unity-ecc-unified-memory-protection-against-bit-and-chip-errors"
status: new
---

# Unity ECC: Unified Memory Protection Against Bit and Chip Errors

## 摘要

DRAM vendors utilize On-Die Error Correction Codes (OD-ECC) to correct random bit errors internally. Meanwhile, system companies utilize Rank-Level ECC (RL-ECC) to protect data against chip errors. Separate protection increases the redundancy ratio to 32.8% in DDR5 and incurs significant performance penalties. This paper proposes a novel RL-ECC, Unity ECC, that can correct both singlechip and double-bit error patterns. Unity ECC corrects doublebit errors using unused syndromes of single-chip correction. Our evaluation shows that Unity ECC without OD-ECC can provide the same reliability level as Chipkill RL-ECC with OD-ECC. Moreover, it can significantly improve system performance and reduce DRAM energy and area by eliminating OD-ECC.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
