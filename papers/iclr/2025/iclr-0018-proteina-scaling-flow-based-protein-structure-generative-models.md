---
id: iclr-0018
title: "Proteina: Scaling Flow-based Protein Structure Generative Models"
conference: ICLR 2025
date: 2025-01
authors:
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kieran Didi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zuobai Zhang"
    affiliation: ""
    is_industry: false
  - name: "Danny Reidenbach"
    affiliation: ""
    is_industry: false
  - name: "Zhonglin Cao"
    affiliation: ""
    is_industry: false
  - name: "Jason Yim"
    affiliation: ""
    is_industry: false
  - name: "Mario Geiger"
    affiliation: ""
    is_industry: false
  - name: "Christian Dallago"
    affiliation: ""
    is_industry: false
  - name: "Emine Kucukbenli"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/genair/proteina/"
abstract: "Recently, diffusion- and flow-based generative models of protein structures have emerged as a powerful tool for de novo protein design. Here, we develop Proteina, a new large-scale flow-based protein backbone generator that utilizes hierarchical fold class labels for conditioning and relies on a tai"
url: "https://research.nvidia.com/publication/2025-01_proteina-scaling-flow-based-protein-structure-generative-models"
status: new
---

# Proteina: Scaling Flow-based Protein Structure Generative Models

## 摘要

Recently, diffusion- and flow-based generative models of protein structures have emerged as a powerful tool for de novo protein design. Here, we develop Proteina, a new large-scale flow-based protein backbone generator that utilizes hierarchical fold class labels for conditioning and relies on a tailored scalable transformer architecture with up to 5x as many parameters as previous models. To meaningfully quantify performance, we introduce a new set of metrics that directly measure the distributional similarity of generated proteins with reference sets, complementing existing metrics. We further explore scaling training data to millions of synthetic protein structures and explore improved training and sampling recipes adapted to protein backbone generation. This includes fine-tuning strategies like LoRA for protein backbones, new guidance methods like classifier-free guidance and autoguidance for protein backbones, and new adjusted training objectives. Proteina achieves state-of-the-art performance on de novo protein backbone design and produces diverse and designable proteins at unprecedented length, up to 800 residues. The hierarchical conditioning offers novel control, enabling high-level secondary-structure guidance as well as low-level fold-specific generation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
