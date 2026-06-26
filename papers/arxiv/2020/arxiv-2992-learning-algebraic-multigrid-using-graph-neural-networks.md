---
id: "arxiv-2992"
title: "Learning Algebraic Multigrid Using Graph Neural Networks"
conference: "arXiv 2020"
date: "2020-07"
authors:
  - name: "Ilay Luz"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Meirav Galun"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ronen Basri"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Irad Yavneh"
    affiliation: "Technion"
    is_industry: false
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
abstract: "Efficient numerical solvers for sparse linear systems are crucial in science and engineering. One of the fastest methods for solving large-scale sparse linear systems is algebraic multigrid (AMG). The main challenge in the construction of AMG algorithms is the selection of the prolongation operator "
url: "https://research.nvidia.com/publication/2020-07_learning-algebraic-multigrid-using-graph-neural-networks"
status: "new"
---

# Learning Algebraic Multigrid Using Graph Neural Networks

## 摘要

Efficient numerical solvers for sparse linear systems are crucial in science and engineering. One of the fastest methods for solving large-scale sparse linear systems is algebraic multigrid (AMG). The main challenge in the construction of AMG algorithms is the selection of the prolongation operator -- a problem-dependent sparse matrix which governs the multiscale hierarchy of the solver and is critical to its efficiency. Over many years, numerous methods have been developed for this task, and yet there is no known single right answer except in very special cases. Here we propose a framework for learning AMG prolongation operators for linear systems with sparse symmetric positive (semi-) definite matrices. We train a single graph neural network to learn a mapping from an entire class of such matrices to prolongation operators, using an efficient unsupervised loss function. Experiments on a broad class of problems demonstrate improved convergence rates compared to classical AMG, demonstrating the potential utility of neural networks for developing sparse system solvers.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
