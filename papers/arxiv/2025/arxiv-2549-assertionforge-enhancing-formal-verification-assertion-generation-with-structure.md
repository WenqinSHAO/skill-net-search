---
id: "arxiv-2549"
title: "AssertionForge: Enhancing Formal Verification Assertion Generation with Structured Representation of Specifications and RTL"
conference: "arXiv 2025"
date: "2025-06"
authors:
  - name: "Yunsheng Bai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ghaith Bany Hamad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Syed Suhaib"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2503.19174"
abstract: "Generating SystemVerilog Assertions (SVAs) from natural language specifications remains a major challenge in formal verification (FV) due to the inherent ambiguity and incompleteness of specifications. Existing LLM-based approaches, such as ASSERTLLM, focus on extracting information solely from spec"
url: "https://research.nvidia.com/publication/2025-06_assertionforge-enhancing-formal-verification-assertion-generation-structured"
status: "new"
---

# AssertionForge: Enhancing Formal Verification Assertion Generation with Structured Representation of Specifications and RTL

## 摘要

Generating SystemVerilog Assertions (SVAs) from natural language specifications remains a major challenge in formal verification (FV) due to the inherent ambiguity and incompleteness of specifications. Existing LLM-based approaches, such as ASSERTLLM, focus on extracting information solely from specification documents, often failing to capture essential internal signal interactions and design details present in the RTL code, leading to incomplete or incorrect assertions. We propose a novel approach that constructs a Knowledge Graph (KG) from both specifications and RTL, using a hardware-specific schema with domain-specific entity and relation types. We create an initial KG from the specification and then systematically fuse it with information extracted from the RTL code, resulting in a unified, comprehensive KG. This combined representation enables a more thorough understanding of the design and allows for a multi-resolution context synthesis process which is designed to extract diverse verification contexts from the KG. Experiments on five designs demonstrate that our method significantly enhances SVA quality over prior methods. This structured representation not only improves FV but also paves the way for future research in tasks like code generation and design understanding.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
