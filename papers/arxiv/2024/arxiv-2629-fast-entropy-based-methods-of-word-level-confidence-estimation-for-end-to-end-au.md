---
id: arxiv-2629
title: "Fast Entropy-Based Methods of Word-Level Confidence Estimation for End-to-End Automatic Speech Recognition"
conference: arXiv 2024
date: 2024-01
authors:
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
    url: "https://arxiv.org/abs/2212.08703"
abstract: "This paper presents a class of new fast non-trainable entropy-based confidence estimation methods for automatic speech recognition. We show how per-frame entropy values can be normalized and aggregated to obtain a confidence measure per unit and per word for Connectionist Temporal Classification (CT"
url: "https://research.nvidia.com/publication/2024-01_fast-entropy-based-methods-word-level-confidence-estimation-end-end-automatic"
status: new
---

# Fast Entropy-Based Methods of Word-Level Confidence Estimation for End-to-End Automatic Speech Recognition

## 摘要

This paper presents a class of new fast non-trainable entropy-based confidence estimation methods for automatic speech recognition. We show how per-frame entropy values can be normalized and aggregated to obtain a confidence measure per unit and per word for Connectionist Temporal Classification (CTC) and Recurrent Neural Network Transducer (RNN-T) models. Proposed methods have similar computational complexity to the traditional method based on the maximum per-frame probability, but they are more adjustable, have a wider effective threshold range, and better push apart the confidence distributions of correct and incorrect words. We evaluate the proposed confidence measures on LibriSpeech test sets, and show that they are up to 2 and 4 times better than confidence estimation based on the maximum per-frame probability at detecting incorrect words for Conformer-CTC and Conformer-RNN-T models, respectively.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
