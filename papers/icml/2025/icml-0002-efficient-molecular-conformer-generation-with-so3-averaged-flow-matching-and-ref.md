---
id: icml-0002
title: "Efficient Molecular Conformer Generation with SO(3)-Averaged Flow Matching and Reflow"
conference: ICML 2025
date: 2025-07
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhonglin Cao"
    affiliation: ""
    is_industry: false
  - name: "Mario Geiger"
    affiliation: ""
    is_industry: false
  - name: "Allan Dos Santos Costa"
    affiliation: ""
    is_industry: false
  - name: "Danny Reidenbach"
    affiliation: ""
    is_industry: false
  - name: "Franco Pellegrini"
    affiliation: ""
    is_industry: false
  - name: "Guoqing Zhou"
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
abstract: "Fast and accurate generation of molecular conformers is desired for downstream computational chemistry and drug discovery tasks. Currently, training and sampling state-of-the-art diffusion or flow-based models for conformer generation require significant computational resources. In this work, we bui"
url: "https://research.nvidia.com/publication/2025-07_efficient-molecular-conformer-generation-so3-averaged-flow-matching-and-reflow"
status: new
---

# Efficient Molecular Conformer Generation with SO(3)-Averaged Flow Matching and Reflow

## 摘要

Fast and accurate generation of molecular conformers is desired for downstream computational chemistry and drug discovery tasks. Currently, training and sampling state-of-the-art diffusion or flow-based models for conformer generation require significant computational resources. In this work, we build upon flow-matching and propose two mechanisms for accelerating training and inference of generative models for 3D molecular conformer generation. For fast training, we introduce the SO(3)-Averaged Flow training objective, which leads to faster convergence to better generation quality compared to conditional optimal transport flow or Kabsch-aligned flow. We demonstrate that models trained using SO(3)-Averaged Flow can reach state-of-the-art conformer generation quality. For fast inference, we show that the reflow and distillation methods of flow-based models enable few-steps or even one-step molecular conformer generation with high quality. The training techniques proposed in this work show a path towards highly efficient molecular conformer generation with flow-based models.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
