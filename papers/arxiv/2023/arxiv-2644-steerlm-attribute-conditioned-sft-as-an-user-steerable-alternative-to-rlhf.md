---
id: arxiv-2644
title: "SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF"
conference: arXiv 2023
date: 2023-10
authors:
  - name: "Yi Dong"
    affiliation: ""
    is_industry: false
  - name: "Zhilin Wang"
    affiliation: ""
    is_industry: false
  - name: "Makesh Narsimhan Sreedhar"
    affiliation: ""
    is_industry: false
  - name: "Xianchao Wu"
    affiliation: ""
    is_industry: false
  - name: "Oleksii Kuchaiev"
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
    url: "https://arxiv.org/abs/2310.05344"
abstract: "Model alignment with human preferences is an essential step in making Large Language Models (LLMs) helpful and consistent with human values. It typically consists of supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF) stages. However, RLHF faces inherent limitations st"
url: "https://research.nvidia.com/publication/2023-10_steerlm-attribute-conditioned-sft-user-steerable-alternative-rlhf"
status: new
---

# SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF

## 摘要

Model alignment with human preferences is an essential step in making Large Language Models (LLMs) helpful and consistent with human values. It typically consists of supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF) stages. However, RLHF faces inherent limitations stemming from a complex training setup and its tendency to align the model with implicit values that end users cannot control at run-time. Moreover, reward models in RLHF stage commonly rely on single-dimensional feedback as opposed to explicit, multifaceted signals that indicate attributes such as helpfulness, humor, and toxicity. To address these limitations, we propose SteerLM, a supervised fine-tuning method that empowers end-users to control responses during inference. SteerLM conditions responses to conform to an explicitly defined multi-dimensional set of attributes, thereby empowering a steerable AI capable of generating helpful and high-quality responses while maintaining customizability. Experiments show that SteerLM trained on open source datasets generates responses that are preferred by human and automatic evaluators to many state-of-the-art baselines trained with RLHF while being much easier to train. Try SteerLM at https://huggingface.co/nvidia/SteerLM-llama2-13B

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
