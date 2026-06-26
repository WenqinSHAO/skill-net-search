---
id: "iclr-0001"
title: "TimeOmni-1: Incentivizing Complex Reasoning with Time Series in Large Language Models"
conference: "ICLR 2026"
date: "2026-04"
authors:
  - name: "Tong Guan"
    affiliation: "Griffith University"
    is_industry: false
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sabato Marco Siniscalchi"
    affiliation: "University of Palermo"
    is_industry: false
  - name: "Qingsong Wen"
    affiliation: "Griffith University"
    is_industry: false
  - name: "Ming Jin"
    affiliation: "Griffith University"
    is_industry: false
  - name: "Shirui Pan"
    affiliation: "Griffith University"
    is_industry: false
topics:
  - Applied_perception
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Esports"
  - "Natural Language Processing"
  - "Speech Processing"
abstract: "Recent advances in multimodal time series learning underscore a paradigm shift from analytics centered on basic patterns toward advanced time series understanding and reasoning. However, existing multimodal time series datasets mostly remain at the level of surface alignment and question answering, "
url: "https://research.nvidia.com/publication/2026-04%5Ftimeomni-1-incentivizing-complex-reasoning-time-series-large-language-models"
status: "new"
---

# TimeOmni-1: Incentivizing Complex Reasoning with Time Series in Large Language Models

## 摘要

Recent advances in multimodal time series learning underscore a paradigm shift from analytics centered on basic patterns toward advanced time series understanding and reasoning. However, existing multimodal time series datasets mostly remain at the level of surface alignment and question answering, without reaching the depth of genuine reasoning. The absence of well-defined tasks that genuinely require time series reasoning, along with the scarcity of high-quality data, has limited progress in building practical time series reasoning models (TSRMs). To this end, we introduce Time Series Reasoning Suite (TSR-Suite), which formalizes four atomic tasks that span three fundamental capabilities for reasoning with time series: (1) perception, acquired through scenario understanding and causality discovery; (2) extrapolation, realized via event-aware forecasting; and (3) decision-making, developed through deliberation over perception and extrapolation. TSR-Suite is the first comprehensive time series reasoning suite that supports not only thorough evaluation but also the data pipeline and training of TSRMs. It contains more than 23K samples, of which 2.3K are carefully curated through a human-guided hierarchical annotation process. Building on this foundation, we introduce TimeOmni-1, the first unified reasoning model designed to address diverse real-world problems demanding time series reasoning. The model is trained in multiple stages, integrating a mixture of task scenarios, novel reward functions, and tailored optimizations. Experiments show that TimeOmni-1 delivers strong out-of-distribution generalization across all tasks and achieves a high rate of valid responses. It significantly improves causality discovery accuracy (64.0% vs. 35.9% with GPT-4.1) and raises the valid response rate by over 6% compared to GPT-4.1 on the event-aware forecasting task.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
