---
id: "arxiv-2614"
title: "An Empirical Study of Mamba-based Language Models"
conference: "arXiv 2024"
date: "2024-06"
authors:
  - name: "Roger Waleffe"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Duncan Riach"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brandon Norick"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vijay Korthikanti"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tri Dao"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Albert Gu"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Ali Hatamizadeh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sudhakar Singh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Deepak Narayanan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Garvit Kulshreshtha"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vartika Singh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jared Casper"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mohammad Shoeybi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bryan Catanzaro"
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
  - "Machine Translation"
  - "Natural Language Processing"
abstract: "Selective state-space models (SSMs) like Mamba overcome some of the shortcomings of Transformers, such as quadratic computational complexity with sequence length and large inference-time memory requirements from the key-value cache. Moreover, recent studies have shown that SSMs can match or exceed t"
url: "https://research.nvidia.com/publication/2024-06_empirical-study-mamba-based-language-models"
status: "new"
---

# An Empirical Study of Mamba-based Language Models

## 摘要

Selective state-space models (SSMs) like Mamba overcome some of the shortcomings of Transformers, such as quadratic computational complexity with sequence length and large inference-time memory requirements from the key-value cache. Moreover, recent studies have shown that SSMs can match or exceed the language modeling capabilities of Transformers, making them an attractive alternative. In a controlled setting (e.g., same training data), however, studies so far have only presented small scale experiments (training with &lt;3B parameters and &lt;1T tokens) comparing SSMs to equivalent Transformers. To understand the strengths and weaknesses of these architectures at larger scales, we present a direct comparison between 8B-parameter Mamba, Mamba-2, and Transformer models trained on the same datasets of up to 3.5T tokens. We also compare these models to an 8B-parameter hybrid architecture consisting of 43% Mamba-2, 7% self-attention, and 50% MLP layers (Mamba-2-Hybrid). Using a diverse set of natural language tasks, we answer the important question of whether Mamba models can match their Transformer counterparts at larger training budgets. Our results show that while pure SSM-based models match or exceed Transformers on many tasks, both Mamba and Mamba-2 models lag behind Transformer models on tasks which require strong copying or in-context learning abilities (e.g., five-shot MMLU, Phonebook Lookup) or long-context reasoning. In contrast, we find that the 8B-parameter Mamba2-Hybrid exceeds the 8B-parameter Transformer on all 12 standard tasks we evaluated (+2.65 points on average) and is predicted to be up to 8× faster when generating tokens at inference time. To validate long-context capabilities, we provide additional experiments evaluating variants of the Mamba-2-Hybrid and Transformer extended to support 16K, 32K, and 128K sequence lengths. On an additional 23 long-context tasks, the hybrid model continues to closely match or exceed the Transformer on average

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
