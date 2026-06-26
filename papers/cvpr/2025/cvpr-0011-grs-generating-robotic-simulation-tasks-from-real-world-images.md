---
id: "cvpr-0011"
title: "GRS: Generating robotic simulation tasks from real-world images"
conference: "CVPR 2025"
date: "2025-06"
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
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Physical AI"
abstract: "Game design hinges on understanding how static rules and content translate into dynamic player behavior---something modern generative systems that inspect only a game's code or assets struggle to capture. We present an automated design iteration framework that closes this gap by pairing a reinforcem"
url: "https://research.nvidia.com/publication/2025-06_grs-generating-robotic-simulation-tasks-real-world-images-0"
status: "new"
---

# GRS: Generating robotic simulation tasks from real-world images

## 摘要

Game design hinges on understanding how static rules and content translate into dynamic player behavior---something modern generative systems that inspect only a game's code or assets struggle to capture. We present an automated design iteration framework that closes this gap by pairing a reinforcement learning (RL) agent, which playtests the game, with a large multimodal model (LMM), which revises the game based on what the agent does. In each loop the RL player completes several episodes, producing (i) numerical play metrics and/or (ii) a compact image strip summarising recent video frames. The LMM designer receives a gameplay goal and the current game configuration, analyses the play traces, and edits the configuration to steer future behaviour toward the goal. We demonstrate results that LMMs can reason over behavioral traces supplied by RL agents to iteratively refine game mechanics, pointing toward practical, scalable tools for AI-assisted game design.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
