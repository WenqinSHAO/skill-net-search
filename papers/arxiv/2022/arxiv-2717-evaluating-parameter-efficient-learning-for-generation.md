---
id: arxiv-2717
title: "Evaluating Parameter Efficient Learning for Generation"
conference: arXiv 2022
date: 2022-10
authors:
  - name: "Peng Xu"
    affiliation: ""
    is_industry: false
  - name: "Mostofa Patwary"
    affiliation: ""
    is_industry: false
  - name: "Shrimai Prabhumoye"
    affiliation: ""
    is_industry: false
  - name: "Virginia Adams"
    affiliation: ""
    is_industry: false
  - name: "Ryan J. Prenger"
    affiliation: ""
    is_industry: false
  - name: "Wei Ping"
    affiliation: ""
    is_industry: false
  - name: "Nayeon Lee"
    affiliation: ""
    is_industry: false
  - name: "Mohammad Shoeybi"
    affiliation: ""
    is_industry: false
  - name: "Bryan Catanzaro"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Natural Language Processing"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2210.13673"
abstract: "Parameter efficient learning methods (PERMs) have recently gained significant attention as they provide an efficient way for pre-trained language models (PLMs) to adapt to a downstream task. However, these conclusions are mostly drawn from in-domain evaluations over the full training set. In this pa"
url: "https://research.nvidia.com/publication/2022-10_evaluating-parameter-efficient-learning-generation"
status: new
---

# Evaluating Parameter Efficient Learning for Generation

## 摘要

Parameter efficient learning methods (PERMs) have recently gained significant attention as they provide an efficient way for pre-trained language models (PLMs) to adapt to a downstream task. However, these conclusions are mostly drawn from in-domain evaluations over the full training set. In this paper, we present comparisons between PERMs and finetuning from three new perspectives: (1) the effect of sample and model size to in-domain evaluations, (2) generalization to unseen domains and new datasets, and (3) the faithfulness of generations. Our results show that for in-domain settings (a) there is a cross point of sample size for which PERMs will perform better than finetuning when training with fewer samples, and (b) larger PLMs have larger cross points. For cross-domain and cross-dataset cases, we show that (a) Adapter (Houlsby et al., 2019) performs the best amongst all the PERMs studied here, and (b) it outperforms finetuning if the task dataset is below a certain size. We also compare the faithfulness of generations and show that PERMs can achieve better faithfulness score than finetuning, especially for small training set, by as much as 6%. Finally, we apply Adapter to MT-NLG 530b (Smith et al., 2022) and achieve new state-of-the-art results on Xsum (Narayan et al., 2018) for all ROUGE scores (ROUGE-1 49.17, ROUGE-2 27.20, ROUGE-L 40.98).

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
