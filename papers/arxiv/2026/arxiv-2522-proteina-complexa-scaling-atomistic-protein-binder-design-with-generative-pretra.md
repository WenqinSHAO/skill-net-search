---
id: "arxiv-2522"
title: "Proteina-Complexa: Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute"
conference: "arXiv 2026"
date: "2026-01"
authors:
  - name: "Kieran Didi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zuobai Zhang"
    affiliation: "NVIDIA, Mila - Quebec AI Institute, Universite de Montreal"
    is_industry: true
  - name: "Guoqing Zhou"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Danny Reidenbach"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhonglin Cao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sooyoung Cha"
    affiliation: "Seoul National University"
    is_industry: false
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Christian Dallago"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jian Tang"
    affiliation: "Mila - Quebec AI Institute, HEC Montreal, CIFAR AI Chair"
    is_industry: false
  - name: "Michael M. Bronstein"
    affiliation: "University of Oxford, AITHYRA"
    is_industry: false
  - name: "Martin Steinegger"
    affiliation: "Seoul National University"
    is_industry: false
  - name: "Emine Kucukbenli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
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
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/genair/proteina-complexa/"
abstract: "Protein interaction modeling is central to protein design, which has been transformed by machine learning with applications in drug discovery and beyond. In this landscape, structure-based de novo binder design is cast as either conditional generative modeling or sequence optimization via structure "
url: "https://research.nvidia.com/publication/2026-01%5Fproteina-complexa-scaling-atomistic-protein-binder-design-generative"
status: "new"
---

# Proteina-Complexa: Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute

## 摘要

Protein interaction modeling is central to protein design, which has been transformed by machine learning with applications in drug discovery and beyond. In this landscape, structure-based de novo binder design is cast as either conditional generative modeling or sequence optimization via structure predictors ("hallucination"). We argue that this is a false dichotomy and propose Proteina-Complexa, a novel fully atomistic binder generation method unifying both paradigms. We extend recent flow-based latent protein generation architectures and leverage the domain-domain interactions of monomeric computationally predicted protein structures to construct Teddymer, a new large-scale dataset of synthetic binder-target pairs for pretraining. Combined with high-quality experimental multimers, this enables training a strong base model. We then perform inference-time optimization with this generative prior, unifying the strengths of previously distinct generative and hallucination methods. Proteina-Complexa sets a new state of the art in computational binder design benchmarks: it delivers markedly higher in-silico success rates than existing generative approaches, and our novel test-time optimization strategies greatly outperform previous hallucination methods under normalized compute budgets. We also demonstrate interface hydrogen bond optimization, fold class-guided binder generation, and extensions to small molecule targets and enzyme design tasks, again surpassing prior methods. Code, models and new data will be publicly released.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
