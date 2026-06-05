---
id: arxiv-2518
title: "iGRPO: Self-Feedback-Driven LLM Reasoning"
conference: arXiv 2026
date: 2026-02
authors:
  - name: "Ali Hatamizadeh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shrimai Prabhumoye"
    affiliation: ""
    is_industry: false
  - name: "Igor Gitman"
    affiliation: ""
    is_industry: false
  - name: "Ximing Lu"
    affiliation: ""
    is_industry: false
  - name: "Seungju Han"
    affiliation: ""
    is_industry: false
  - name: "Wei Ping"
    affiliation: ""
    is_industry: false
  - name: "Yejin Choi"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Natural Language Processing"
external_links:
  - name: "https://arxiv.org/abs/2602.09000"
    url: "https://arxiv.org/abs/2602.09000"
abstract: "Large Language Models (LLMs) have shown promise in solving complex mathematical problems, yet they still fall short of producing accurate and consistent solutions. Reinforcement Learning (RL) is a framework for aligning these models with task-specific rewards, improving overall quality and reliabili"
url: "https://research.nvidia.com/publication/2026-02%5Figrpo-self-feedback-driven-llm-reasoning"
status: new
---

# iGRPO: Self-Feedback-Driven LLM Reasoning

## 摘要

Large Language Models (LLMs) have shown promise in solving complex mathematical problems, yet they still fall short of producing accurate and consistent solutions. Reinforcement Learning (RL) is a framework for aligning these models with task-specific rewards, improving overall quality and reliability. Group Relative Policy Optimization (GRPO) is an efficient, value-function-free alternative to Proximal Policy Optimization (PPO) that leverages group-relative reward normalization. We introduce Iterative Group Relative Policy Optimization (iGRPO), a two-stage extension of GRPO that adds dynamic self-conditioning through model-generated drafts. In Stage 1, iGRPO samples multiple exploratory drafts and selects the highest-reward draft using the same scalar reward signal used for optimization. In Stage 2, it appends this best draft to the original prompt and applies a GRPO-style update on draft-conditioned refinements, training the policy to improve beyond its strongest prior attempt. Under matched rollout budgets, iGRPO consistently outperforms GRPO across base models (e.g., Nemotron-H-8B-Base-8K and DeepSeek-R1 Distilled), validating its effectiveness on diverse reasoning benchmarks. Moreover, applying iGRPO to OpenReasoning-Nemotron-7B trained on AceReason-Math achieves new state-of-the-art results of 85.62\% and 79.64\% on AIME24 and AIME25, respectively. Ablations further show that the refinement wrapper generalizes beyond GRPO variants, benefits from a generative judge, and alters learning dynamics by delaying entropy collapse. These results underscore the potential of iterative, self-feedback-based RL for advancing verifiable mathematical reasoning.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
