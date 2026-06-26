---
id: "arxiv-2929"
title: "NVCell: Generate Standard Cell Layout in Advanced Technology Nodes with Reinforcement Learning"
conference: "arXiv 2020"
date: "2020-12"
authors:
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matt Fojtik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
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
abstract: "Standard cell layouts in advanced technology nodes are done manually in the industry today. Automating standard cell layouts is challenging because of the exploding number and complexity of design rule checking (DRC), especially when the design goal is to minimize cell area. In this paper we propose"
url: "https://research.nvidia.com/publication/2020-12_nvcell-generate-standard-cell-layout-advanced-technology-nodes-reinforcement"
status: "new"
---

# NVCell: Generate Standard Cell Layout in Advanced Technology Nodes with Reinforcement Learning

## 摘要

Standard cell layouts in advanced technology nodes are done manually in the industry today. Automating standard cell layouts is challenging because of the exploding number and complexity of design rule checking (DRC), especially when the design goal is to minimize cell area. In this paper we propose a machine learning based approach to handle DRC constrains. In our approach, we apply a genetic algorithm to create routing candidates and use reinforcement learning (RL) to fix the design rule violations incrementally. A design rule checker provides feedback on violations to the RL agent and the agent learns how to fix them based on the data. This approach is also applicable to future technologies with unseen DRCs. Based on this approach, we built a layout generator called NVCell that includes a device placer based on a simulated annealing method and a router based on a genetic algorithm and reinforcement learning. NVCell can generate layouts with equal or smaller area for over 75% of cells in an industry standard cell library.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
