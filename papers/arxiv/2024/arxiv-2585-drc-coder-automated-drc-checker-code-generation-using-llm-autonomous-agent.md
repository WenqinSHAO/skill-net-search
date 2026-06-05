---
id: arxiv-2585
title: "DRC-Coder: Automated DRC Checker Code Generation Using LLM Autonomous Agent"
conference: arXiv 2024
date: 2024-11
authors:
  - name: "Chia-Tung (Mark) Ho"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chen-Chia Chang"
    affiliation: ""
    is_industry: false
  - name: "Yaguang Li"
    affiliation: ""
    is_industry: false
  - name: "Yiran Chen"
    affiliation: ""
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
  - "Generative AI"
abstract: "In the advanced technology nodes, the integrated design rule checker (DRC) is often utilized in place and route tools for fast optimization loops for power-performance-area. Implementing integrated DRC checkers to meet the standard of commercial DRC tools demands extensive human expertise to interpr"
url: "https://research.nvidia.com/publication/2024-11_drc-coder-automated-drc-checker-code-generation-using-llm-autonomous-agent"
status: new
---

# DRC-Coder: Automated DRC Checker Code Generation Using LLM Autonomous Agent

## 摘要

In the advanced technology nodes, the integrated design rule checker (DRC) is often utilized in place and route tools for fast optimization loops for power-performance-area. Implementing integrated DRC checkers to meet the standard of commercial DRC tools demands extensive human expertise to interpret foundry specifications, analyze layouts, and debug code iteratively. However, this labor-intensive process, requiring to be repeated by every update of technology nodes, prolongs the turnaround time of designing circuits. In this paper, we present DRC-Coder, a multi-agent framework with vision capabilities for automated DRC code generation. By incorporating vision language models and large language models (LLM), DRC-Coder can effectively process textual, visual, and layout information to perform rule interpretation and coding by two specialized LLMs. We also design an auto-evaluation function for LLMs to enable DRC code debugging. Experimental results show that targeting on a sub-3nm technology node for a state-of-the-art standard cell layout tool, DRC-Coder achieves perfect F1 score 1.000 in generating DRC codes for meeting the standard of a commercial DRC tool, highly outperforming standard prompting techniques (F1=0.631). DRC-Coder can generate code for each design rule within four minutes on average, which significantly accelerates technology advancement and reduces engineering costs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
