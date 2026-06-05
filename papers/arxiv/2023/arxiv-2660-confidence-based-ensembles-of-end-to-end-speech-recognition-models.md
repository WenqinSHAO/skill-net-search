---
id: arxiv-2660
title: "Confidence-based Ensembles of End-to-End Speech Recognition Models"
conference: arXiv 2023
date: 2023-06
authors:
  - name: "Igor Gitman"
    affiliation: ""
    is_industry: false
  - name: "Vitaly Lavrukhin"
    affiliation: ""
    is_industry: false
  - name: "Aleksandr Laptev"
    affiliation: ""
    is_industry: false
  - name: "Boris Ginsburg"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Speech Processing"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2306.15824"
abstract: "The number of end-to-end speech recognition models grows every year. These models are often adapted to new domains or languages resulting in a proliferation of expert systems that achieve great results on target data, while generally showing inferior performance outside of their domain of expertise."
url: "https://research.nvidia.com/publication/2023-06_confidence-based-ensembles-end-end-speech-recognition-models"
status: new
---

# Confidence-based Ensembles of End-to-End Speech Recognition Models

## 摘要

The number of end-to-end speech recognition models grows every year. These models are often adapted to new domains or languages resulting in a proliferation of expert systems that achieve great results on target data, while generally showing inferior performance outside of their domain of expertise. We explore combination of such experts via confidence-based ensembles: ensembles of models where only the output of the most-confident model is used. We assume that models' target data is not available except for a small validation set. We demonstrate effectiveness of our approach with two applications. First, we show that a confidence-based ensemble of 5 monolingual models outperforms a system where model selection is performed via a dedicated language identification block. Second, we demonstrate that it is possible to combine base and adapted models to achieve strong results on both original and target data. We validate all our results on multiple datasets and model architectures.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
