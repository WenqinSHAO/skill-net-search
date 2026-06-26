---
id: "iclr-0009"
title: "Hymba: A Hybrid-head Architecture for Small Language Models"
conference: "ICLR 2025"
date: "2025-04"
authors:
  - name: "Xin Dong*"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yonggan Fu*"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shizhe Diao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zijia Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ameya Sunil Mahabaleshwarkar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shih-Yang Liu"
    affiliation: "NVIDIA, HKUST"
    is_industry: true
  - name: "Matthijs Van keirsbilck"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yoshi Nishi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yingyan Celine Lin"
    affiliation: "NVIDIA, Georgia Tech"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
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
  - "Natural Language Processing"
external_links:
  - name: "openreview"
    url: "https://openreview.net/forum?id=A1ztozypga"
abstract: "We propose Hymba, a family of small language models featuring a hybrid-head parallel architecture that integrates attention mechanisms and state space models (SSMs) within the same layer, offering parallel and complementary processing of the same inputs. In this hybrid-head module, attention heads p"
url: "https://research.nvidia.com/publication/2025-04_hymba-hybrid-head-architecture-small-language-models"
status: "new"
---

# Hymba: A Hybrid-head Architecture for Small Language Models

## 摘要

We propose Hymba, a family of small language models featuring a hybrid-head parallel architecture that integrates attention mechanisms and state space models (SSMs) within the same layer, offering parallel and complementary processing of the same inputs. In this hybrid-head module, attention heads provide high-resolution recall, while SSM heads facilitate efficient context summarization. Additionally, we introduce learnable meta tokens, which are prepended to prompts to store critical meta information, guiding subsequent tokens and alleviating the “forced-to-attend” burden associated with attention mechanisms. Thanks to the global context summarized by SSMs, the attention heads in our model can be further optimized through cross-layer key-value (KV) sharing and a mix of global and local attention, resulting in a compact cache size without compromising accuracy. Notably, Hymba achieves state-of-the-art performance among small LMs: Our Hymba-1.5B-Base model surpasses all sub-2B public models and even outperforms Llama-3.2-3B, achieving 1.32% higher average accuracy, an 11.67 reduction in cache size, and 3.49 higher throughput.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
