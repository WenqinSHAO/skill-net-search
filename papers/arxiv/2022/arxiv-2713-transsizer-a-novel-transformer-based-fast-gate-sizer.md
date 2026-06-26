---
id: "arxiv-2713"
title: "TransSizer: A Novel Transformer-Based Fast Gate Sizer"
conference: "arXiv 2022"
date: "2022-10"
authors:
  - name: "Siddhartha Nath"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Geraldo Pradipta"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Corey Hu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tian Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
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
    url: "https://dl.acm.org/doi/abs/10.1145/3508352.3549442"
abstract: "Gate sizing is a fundamental netlist optimization move and researchers have used supervised learning-based models in gate sizers. Recently, Reinforcement Learning (RL) has been tried for sizing gates (and other EDA optimization problems) but are very runtime-intensive. In this work, we explore a nov"
url: "https://research.nvidia.com/publication/2022-10_transsizer-novel-transformer-based-fast-gate-sizer"
status: "new"
---

# TransSizer: A Novel Transformer-Based Fast Gate Sizer

## 摘要

Gate sizing is a fundamental netlist optimization move and researchers have used supervised learning-based models in gate sizers. Recently, Reinforcement Learning (RL) has been tried for sizing gates (and other EDA optimization problems) but are very runtime-intensive. In this work, we explore a novel Transformer-based gate sizer,&nbsp;TransSizer, to&nbsp;directly generate optimized&nbsp;gate sizes given a placed and unoptimized netlist. TransSizer is trained on datasets obtained from real tapeout-quality industrial designs in a foundry 5nm&nbsp;technology node. Our results indicate that TransSizer achieves 97% accuracy in predicting optimized gate sizes at the postroute optimization stage. Furthermore, TransSizer has a speedup of ~1400× while delivering similar timing, power and area metrics when compared to a leading-edge commercial tool for sizing-only optimization.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
