---
id: iclr-0015
title: "Towards Neural Scaling Laws for Time Series Foundation Models"
conference: ICLR 2025
date: 2025-04
authors:
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Qingren Yao"
    affiliation: ""
    is_industry: false
  - name: "Renhe Jiang"
    affiliation: ""
    is_industry: false
  - name: "Ming Jin"
    affiliation: ""
    is_industry: false
  - name: "Shirui Pan"
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
  - "Natural Language Processing"
abstract: "Scaling laws offer valuable insights into the design of time series foundation models (TSFMs). However, previous research has largely focused on the scaling lawsof TSFMs for in-distribution (ID) data, leaving their out-of-distribution (OOD)scaling behavior and the influence of model architectures le"
url: "https://research.nvidia.com/publication/2025-04_towards-neural-scaling-laws-time-series-foundation-models"
status: new
---

# Towards Neural Scaling Laws for Time Series Foundation Models

## 摘要

Scaling laws offer valuable insights into the design of time series foundation models (TSFMs). However, previous research has largely focused on the scaling lawsof TSFMs for in-distribution (ID) data, leaving their out-of-distribution (OOD)scaling behavior and the influence of model architectures less explored. In thiswork, we examine two common TSFM architectures—encoder-only and decoderonly Transformers—and investigate their scaling behavior on both ID and OODdata. These models are trained and evaluated across varying parameter counts,compute budgets, and dataset sizes. Our experiments reveal that the negative loglikelihood of TSFMs exhibits similar scaling behavior in both OOD and ID settings. We further compare the scaling properties across different architectures, incorporating two state-of-the-art TSFMs as case studies, showing that model architecture plays a significant role in scaling. The encoder-only Transformers demonstrate better scalability than the decoder-only Transformers in ID data, while thearchitectural enhancements in the two advanced TSFMs primarily improve IDperformance but reduce OOD scalability. While scaling up TSFMs is expected todrive performance breakthroughs, the lack of a comprehensive understanding ofTSFM scaling laws has hindered the development of a robust framework to guidemodel scaling. We fill this gap in this work by synthesizing our findings and providing practical guidelines for designing and scaling larger TSFMs with enhancedmodel capabilities.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
