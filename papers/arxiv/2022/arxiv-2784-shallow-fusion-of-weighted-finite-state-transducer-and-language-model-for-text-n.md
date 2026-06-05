---
id: arxiv-2784
title: "Shallow Fusion of Weighted Finite-State Transducer and Language Model for Text Normalization"
conference: arXiv 2022
date: 2022-03
authors:
  - name: "Evelina Bakhturina"
    affiliation: ""
    is_industry: false
  - name: "Yang Zhang"
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
  - "Natural Language Processing"
  - "Speech Processing"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2203.15917"
abstract: "Text normalization (TN) systems in production are largely rule-based using weighted finite-state transducers (WFST). However, WFST-based systems struggle with ambiguous input when the normalized form is context-dependent. On the other hand, neural text normalization systems can take context into acc"
url: "https://research.nvidia.com/publication/2022-03_shallow-fusion-weighted-finite-state-transducer-and-language-model-text"
status: new
---

# Shallow Fusion of Weighted Finite-State Transducer and Language Model for Text Normalization

## 摘要

Text normalization (TN) systems in production are largely rule-based using weighted finite-state transducers (WFST). However, WFST-based systems struggle with ambiguous input when the normalized form is context-dependent. On the other hand, neural text normalization systems can take context into account but they suffer from unrecoverable errors and require labeled normalization datasets, which are hard to collect. We propose a new hybrid approach that combines the benefits of rule-based and neural systems. First, a non-deterministic WFST outputs all normalization candidates, and then a neural language model picks the best one -- similar to shallow fusion for automatic speech recognition. While the WFST prevents unrecoverable errors, the language model resolves contextual ambiguity. The approach is easy to extend and we show it is effective. It achieves comparable or better results than existing state-of-the-art TN models.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
