---
id: arxiv-2511
title: "Fast AI-Based Pre-Decoders for Surface Codes"
conference: arXiv 2026
date: 2026-04
authors:
  - name: "Christopher Chamberland"
    affiliation: ""
    is_industry: false
  - name: "Jan Olle"
    affiliation: ""
    is_industry: false
  - name: "Muyuan Li"
    affiliation: ""
    is_industry: false
  - name: "Scott Thornton"
    affiliation: ""
    is_industry: false
  - name: "Igor Baratta"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
abstract: "Fast, scalable decoding architectures that operate in a block-wise parallel fashion across space and time are essential for real-time fault-tolerant quantum computing. We introduce a scalable AI-based pre-decoder for the surface code that performs local, parallel error correction at low latency, rem"
url: "https://research.nvidia.com/publication/2026-04%5Ffast-ai-based-pre-decoders-surface-codes"
status: new
---

# Fast AI-Based Pre-Decoders for Surface Codes

## 摘要

Fast, scalable decoding architectures that operate in a block-wise parallel fashion across space and time are essential for real-time fault-tolerant quantum computing. We introduce a scalable AI-based pre-decoder for the surface code that performs local, parallel error correction at low latency, removing the majority of physical errors before passing residual syndromes to a downstream global decoder. This modular architecture is backend-agnostic and composes with arbitrary global decoding algorithms designed for surface codes, and our implementation is completely open source. Integrated with uncorrelated PyMatching, the pipeline achieves end-to-end decoding latencies of order $\mathcal{O}(1 \mu\text{s})$ at large code distances on NVIDIA GB300 GPUs while reducing logical error rates (LERs) relative to global decoding alone. We observe further LER improvements by training a larger model, outperforming correlated PyMatching up to distance-13. We additionally introduce a noise-learning architecture that infers decoding weights directly from experimentally accessible syndrome statistics without requiring an explicit circuit-level noise model. We show that purely data-driven graph weight estimation can nearly match uncorrelated PyMatching and exceed correlated PyMatching in certain regimes, enabling highly-optimized decoding when hardware noise models are unknown or time-varying as well as training pre-decoders with realistic noise models. Together, these results establish a practical, modular, and high-throughput decoding framework suitable for large-distance surface-code implementations.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
