---
id: "neurips-0005"
title: "ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning"
conference: "NeurIPS 2025"
date: "2025-12"
authors:
  - name: "Chi-Pin Huang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yueh-Hua Wu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Frank Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fred Yang"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "Physical AI"
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://jasper0314-huang.github.io/thinkact-vla/"
abstract: "Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit re"
url: "https://research.nvidia.com/publication/2025-12_thinkact-vision-language-action-reasoning-reinforced-visual-latent-planning"
status: "new"
---

# ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

## 摘要

Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
