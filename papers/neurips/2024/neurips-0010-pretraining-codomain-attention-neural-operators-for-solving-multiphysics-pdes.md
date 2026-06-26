---
id: "neurips-0010"
title: "Pretraining codomain attention neural operators for solving multiphysics pdes"
conference: "NeurIPS 2024"
date: "2024-12"
authors:
  - name: "Md Ashiqur Rahman"
    affiliation: "Purdue University"
    is_industry: false
  - name: "Robert Joseph George"
    affiliation: "Caltech"
    is_industry: false
  - name: "Mogab Elleithy"
    affiliation: "Caltech"
    is_industry: false
  - name: "Daniel Leibovici"
    affiliation: "Caltech"
    is_industry: false
  - name: "Zongyi Li"
    affiliation: "Caltech"
    is_industry: false
  - name: "Boris Bonev"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Colin White"
    affiliation: "Caltech"
    is_industry: false
  - name: "Julius Berner"
    affiliation: "Caltech"
    is_industry: false
  - name: "Raymond A. Yeh"
    affiliation: "Purdue University"
    is_industry: false
  - name: "Jean Kossaifi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kamyar Azizzadenesheli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "Caltech"
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Physical AI"
abstract: "Existing neural operator architectures face challenges when solving multiphysics problems with coupled partial differential equations (PDEs) due to complex geometries, interactions between physical variables, and the limited amounts of high-resolution training data. To address these issues, we propo"
url: "https://research.nvidia.com/publication/2024-12_pretraining-codomain-attention-neural-operators-solving-multiphysics-pdes"
status: "new"
---

# Pretraining codomain attention neural operators for solving multiphysics pdes

## 摘要

Existing neural operator architectures face challenges when solving multiphysics problems with coupled partial differential equations (PDEs) due to complex geometries, interactions between physical variables, and the limited amounts of high-resolution training data. To address these issues, we propose Codomain Attention Neural Operator (CoDA-NO), which tokenizes functions along the codomain or channel space, enabling self-supervised learning or pretraining of multiple PDE systems. Specifically, we extend positional encoding, self-attention, and normalization layers to function spaces. CoDA-NO can learn representations of different PDE systems with a single model. We evaluate CoDA-NO's potential as a backbone for learning multiphysics PDEs over multiple systems by considering few-shot learning settings. On complex downstream tasks with limited data, such as fluid flow simulations, fluid-structure interactions, and Rayleigh-Bénard convection, we found CoDA-NO to outperform existing methods by over 36%.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
