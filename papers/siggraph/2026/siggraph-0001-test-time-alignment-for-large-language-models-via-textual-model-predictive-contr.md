---
id: "siggraph-0001"
title: "Test-Time Alignment for Large Language Models via Textual Model Predictive Control"
conference: "SIGGRAPH 2026"
date: "2026-04"
authors:
  - name: "Kuang-Da Wang"
    affiliation: "NYCU"
    is_industry: false
  - name: "Teng-Ruei Chen"
    affiliation: "NYCU"
    is_industry: false
  - name: "Yu Heng Hung"
    affiliation: "NYCU"
    is_industry: false
  - name: "Guo-Xun Ko"
    affiliation: "NYCU"
    is_industry: false
  - name: "Shuoyang Ding"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Frank Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wen-Chih Peng"
    affiliation: "NYCU"
    is_industry: false
  - name: "Ping-Chun Hsieh"
    affiliation: "NYCU"
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Machine Translation"
abstract: "Abstract Aligning Large Language Models (LLMs) with human preferences through finetuning is resource-intensive, motivating lightweight alternatives at test time. We address test-time alignment through the lens of sequential decision making, a perspective that reveals two fundamental challenges. When"
url: "https://research.nvidia.com/publication/2026-04%5Ftest-time-alignment-large-language-models-textual-model-predictive-control"
status: "new"
---

# Test-Time Alignment for Large Language Models via Textual Model Predictive Control

## 摘要

Abstract Aligning Large Language Models (LLMs) with human preferences through finetuning is resource-intensive, motivating lightweight alternatives at test time. We address test-time alignment through the lens of sequential decision making, a perspective that reveals two fundamental challenges. When actions are defined at the token level, as in guided decoding, alignment suffers from the curse of horizon. Conversely, when actions are at the response level, as in traditional iterative refinement, the curse of dimensionality emerges. To resolve this trade-off, we draw inspiration from Model Predictive Control (MPC) in control theory to propose Textual Model Predictive Control (TMPC), a novel predictive planning framework adapted for aligning LLMs at inference time. A key limitation of standard MPC is its reliance on predefined, hard segment boundaries, which are often absent in text generation. TMPC overcomes this by introducing two principles inspired by hierarchical reinforcement learning: (1) Hindsight Subgoal Identification, where TMPC analyzes generation subgoals to retrospectively identify high-reward intermediate outputs as subgoals. This allows the framework to discover meaningful, task-specific planning steps (e.g., a sentence in machine translation or a bug fix in code generation.). (2) Subgoal-Conditioned Re-Generation, where these identified subgoals are used to guide subsequent planning iterations. By conditioning on these proven, high-quality subgoals, TMPC ensures stable improvement by building upon previously validated successes. TMPC is evaluated on three tasks with distinct segmentation properties: discourse-level translation, long-form response generation, and program synthesis. The results demonstrate that TMPC consistently improves performance, highlighting the generality.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
