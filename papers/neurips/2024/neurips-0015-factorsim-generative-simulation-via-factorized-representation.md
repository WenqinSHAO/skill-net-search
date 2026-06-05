---
id: neurips-0015
title: "FactorSim: Generative Simulation via Factorized Representation"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Alex Zook"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fan-Yun Sun"
    affiliation: ""
    is_industry: false
  - name: "S. I. Harini"
    affiliation: ""
    is_industry: false
  - name: "Angela Yi"
    affiliation: ""
    is_industry: false
  - name: "Yihan Zhou"
    affiliation: ""
    is_industry: false
  - name: "Logan Cross"
    affiliation: ""
    is_industry: false
  - name: "Jiajun Wu"
    affiliation: ""
    is_industry: false
  - name: "Nick Haber"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "Physical AI"
  - "Robotics"
external_links:
  - name: "NeurIPS publication"
    url: "https://proceedings.neurips.cc/paper_files/paper/2024/hash/9f35ec2f7f403ef2c83d65b581df10bc-Abstract-Conference.html"
abstract: "Generating simulations to train intelligent agents in game-playing and robotics from natural language input, from user input or task documentation, remains an open-ended challenge. Existing approaches focus on parts of this challenge, such as generating reward functions or task hyperparameters. Unli"
url: "https://research.nvidia.com/publication/2024-12_factorsim-generative-simulation-factorized-representation"
status: new
---

# FactorSim: Generative Simulation via Factorized Representation

## 摘要

Generating simulations to train intelligent agents in game-playing and robotics from natural language input, from user input or task documentation, remains an open-ended challenge. Existing approaches focus on parts of this challenge, such as generating reward functions or task hyperparameters. Unlike previous work, we introduce FACTORSIM that generates full simulations in code from language input that can be used to train agents. Exploiting the structural modularity specific to coded simulations, we propose to use a factored partially observable Markov decision process representation that allows us to reduce context dependence during each step of the generation. For evaluation, we introduce a generative simulation benchmark that assesses the generated simulation code’s accuracy and effectiveness in facilitating zero-shot transfers in reinforcement learning settings. We show that FACTORSIM outperforms existing methods in generating simulations regarding prompt alignment (i.e., accuracy), zero-shot transfer abilities, and human evaluation. We also demonstrate its effectiveness in generating robotic tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
