---
id: "arxiv-2543"
title: "Fly, Fail, Fix: Iterative Game Repair with Reinforcement Learning and Large Multimodal Models"
conference: "arXiv 2025"
date: "2025-08"
authors:
  - name: "Alex Zook"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Josef Spjut"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
external_links:
  - name: "openreview"
    url: "https://openreview.net/forum?id=Sn26ZtJoyT"
  - name: "arxiv"
    url: "https://arxiv.org/abs/2507.12666"
abstract: "Game design hinges on understanding how static rules and content translate into dynamic player behavior---something modern generative systems that inspect only a game's code or assets struggle to capture. We present an automated design iteration framework that closes this gap by pairing a reinforcem"
url: "https://research.nvidia.com/publication/2025-08_fly-fail-fix-iterative-game-repair-reinforcement-learning-and-large-multimodal"
status: "new"
---

# Fly, Fail, Fix: Iterative Game Repair with Reinforcement Learning and Large Multimodal Models

## 摘要

Game design hinges on understanding how static rules and content translate into dynamic player behavior---something modern generative systems that inspect only a game's code or assets struggle to capture. We present an automated design iteration framework that closes this gap by pairing a reinforcement learning (RL) agent, which playtests the game, with a large multimodal model (LMM), which revises the game based on what the agent does. In each loop the RL player completes several episodes, producing(i)~numerical play metrics and/or&nbsp;(ii)~a compact image strip summarising recent video frames.The LMM designer receives a gameplay goal and the current game configuration, analyses the play traces, and edits the configuration to steer future behaviour toward the goal. We demonstrate results that LMMs can reason over behavioral traces supplied by RL agents to iteratively refine game mechanics, pointing toward practical, scalable tools for AI-assisted game design.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
