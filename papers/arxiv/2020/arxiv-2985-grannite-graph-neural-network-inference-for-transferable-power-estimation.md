---
id: "arxiv-2985"
title: "GRANNITE: Graph Neural Network Inference for Transferable Power Estimation"
conference: "arXiv 2020"
date: "2020-07"
authors:
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
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
  - "Circuits and VLSI Design"
  - "Artificial Intelligence and Machine Learning"
abstract: "This paper introduces GRANNITE, a GPU-accelerated novel graph neural network (GNN) model for fast, accurate, and transferable vector-based average power estimation. During training, GRANNITE learns how to propagate average toggle rates through combinational logic: a netlist is represented as a graph"
url: "https://research.nvidia.com/publication/2020-07_grannite-graph-neural-network-inference-transferable-power-estimation"
status: "new"
---

# GRANNITE: Graph Neural Network Inference for Transferable Power Estimation

## 摘要

This paper introduces GRANNITE, a GPU-accelerated novel graph neural network (GNN) model for fast, accurate, and transferable vector-based average power estimation. During training, GRANNITE learns how to propagate average toggle rates through combinational logic: a netlist is represented as a graph, register states and unit inputs from RTL simulation are used as features, and combinational gate toggle rates are used as labels. A trained GNN model can then infer average toggle rates on a new workload of interest or new netlists from RTL simulation results in a few seconds. Compared to traditional power analysis using gate-level simulations, GRANNITE achieves &gt;18.7X speedup with an error of only &lt;5.5% across a diverse set of benchmark circuits. Compared to a GPU-accelerated conventional probabilistic switching activity estimation approach, GRANNITE achieves much better accuracy (on average 25.9% lower error) at similar runtimes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
