---
id: "arxiv-2537"
title: "FVDebug: An LLM-Driven Debugging Assistant for Automated Root Cause Analysis of Formal Verification Failures"
conference: "arXiv 2025"
date: "2025-09"
authors:
  - name: "Yunsheng Bai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ghaith Bany Hamad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chia-Tung (Mark) Ho"
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
    url: "https://arxiv.org/abs/2510.15906"
abstract: "Debugging formal verification (FV) failures represents one of the most time-consuming bottlenecks in modern hardware design workflows. When properties fail, engineers must manually trace through complex counter-examples spanning multiple cycles, analyze waveforms, and cross-reference design specific"
url: "https://research.nvidia.com/publication/2025-09_fvdebug-llm-driven-debugging-assistant-automated-root-cause-analysis-formal"
status: "new"
---

# FVDebug: An LLM-Driven Debugging Assistant for Automated Root Cause Analysis of Formal Verification Failures

## 摘要

Debugging formal verification (FV) failures represents one of the most time-consuming bottlenecks in modern hardware design workflows. When properties fail, engineers must manually trace through complex counter-examples spanning multiple cycles, analyze waveforms, and cross-reference design specifications to identify root causes - a process that can consume hours or days per bug. Existing solutions are largely limited to manual waveform viewers or simple automated tools that cannot reason about the complex interplay between design intent and implementation logic. We present FVDebug, an intelligent system that automates root-cause analysis by combining multiple data sources - waveforms, RTL code, design specifications - to transform failure traces into actionable insights. Our approach features a novel pipeline: (1) Causal Graph Synthesis that structures failure traces into directed acyclic graphs, (2) Graph Scanner using batched Large Language Model (LLM) analysis with for-and-against prompting to identify suspicious nodes, and (3) Insight Rover leveraging agentic narrative exploration to generate high-level causal explanations. FVDebug further provides concrete RTL fixes through its Fix Generator. Evaluated on open benchmarks, FVDebug attains high hypothesis quality and strong Pass@k fix rates. We further report results on two proprietary, production-scale FV counterexamples. These results demonstrate FVDebug's applicability from academic benchmarks to industrial designs.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
