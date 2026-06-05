---
id: icml-0020
title: "From local structures to size generalization in graph neural networks"
conference: ICML 2021
date: 2021-06
authors:
  - name: "Eli Meirom"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gilad Yehudai"
    affiliation: ""
    is_industry: false
  - name: "Ethan Fetaya"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
abstract: "Graph neural networks (GNNs) can process graphs of different sizes, but their ability to generalize across sizes, specifically from small to large graphs, is still not well understood. In this paper, we identify an important type of data where generalization from small to large graphs is challenging"
url: "https://research.nvidia.com/publication/2021-06_local-structures-size-generalization-graph-neural-networks"
status: new
---

# From local structures to size generalization in graph neural networks

## 摘要

Graph neural networks (GNNs) can process graphs of different sizes, but their ability to generalize across sizes, specifically from small to large graphs, is still not well understood. In this paper, we identify an important type of data where generalization from small to large graphs is challenging: graph distributions for which the local structure depends on the graph size. This effect occurs in multiple important graph learning domains, including social and biological networks. We first prove that when there is a difference between the local structures, GNNs are not guaranteed to generalize across sizes: there are" bad" global minima that do well on small graphs but fail on large graphs. We then study the size-generalization problem empirically and demonstrate that when there is a discrepancy in local structure, GNNs tend to converge to non-generalizing solutions. Finally, we suggest two approaches for improving size generalization, motivated by our findings. Notably, we propose a novel Self-Supervised Learning (SSL) task aimed at learning meaningful representations of local structures that appear in large graphs. Our SSL task improves classification accuracy on several popular datasets.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
