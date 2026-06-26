---
id: "arxiv-2923"
title: "Standard Cell Routing with Reinforcement Learning and Genetic Algorithm in Advanced Technology Nodes"
conference: "arXiv 2021"
date: "2021-01"
authors:
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matt Fojtik"
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
  - name: "Standard Cell Routing with Reinforcement Learning and Genetic Algorithm in Adva…"
    url: "https://dl.acm.org/doi/abs/10.1145/3394885.3431569"
abstract: "Automated standard cell routing in advanced technology nodes with&nbsp;unidirectional metal are challenging because of the constraints of&nbsp;exploding design rules. Previous approaches leveraged mathematical&nbsp;optimization methods such as SAT and MILP to find optimum&nbsp;solution under those c"
url: "https://research.nvidia.com/publication/2021-01_standard-cell-routing-reinforcement-learning-and-genetic-algorithm-advanced"
status: "new"
---

# Standard Cell Routing with Reinforcement Learning and Genetic Algorithm in Advanced Technology Nodes

## 摘要

Automated standard cell routing in advanced technology nodes with&nbsp;unidirectional metal are challenging because of the constraints of&nbsp;exploding design rules. Previous approaches leveraged mathematical&nbsp;optimization methods such as SAT and MILP to find optimum&nbsp;solution under those constraints. The assumption those methods&nbsp;relied on is that all the design rules can be expressed in the optimization&nbsp;framework and the solver is powerful enough to solve&nbsp;them. In this paper we propose a machine learning based approach&nbsp;that does not depend on this assumption. In our approach, we apply&nbsp;genetic algorithm to create initial routing candidates and use&nbsp;Reinforcement Learning (RL) to fix the design rule violations incrementally.&nbsp;Our approach does not need to formulate each design&nbsp;rule constraints in a mathematical framework, instead, a design&nbsp;rule checker feedbacks the violations to the RL agent and the agent&nbsp;learns how to fix them based on the data. This approach is more&nbsp;adaptable to future technologies and potentially more scalable than&nbsp;the mathematical optimization approaches. We also implement a&nbsp;grid based layout environment called Stick, which can generate&nbsp;layout data from the grid-based assignment from our router. We&nbsp;demonstrate the effectiveness of our approach on a number of standard&nbsp;cells. We have shown that it can route a cell which is deemed&nbsp;unroutable manually, reducing the cell size by 11%.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
