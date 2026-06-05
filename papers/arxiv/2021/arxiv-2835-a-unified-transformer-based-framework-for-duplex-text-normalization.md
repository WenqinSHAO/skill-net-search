---
id: arxiv-2835
title: "A Unified Transformer-based Framework for Duplex Text Normalization"
conference: arXiv 2021
date: 2021-08
authors:
  - name: "Tuan Manh Lai"
    affiliation: ""
    is_industry: false
  - name: "Yang Zhang"
    affiliation: ""
    is_industry: false
  - name: "Evelina Bakhturina"
    affiliation: ""
    is_industry: false
  - name: "Boris Ginsburg"
    affiliation: ""
    is_industry: false
  - name: "Heng Ji"
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
    url: "https://arxiv.org/abs/2108.09889"
abstract: "Text normalization (TN) and inverse text normalization (ITN) are essential preprocessing and postprocessing steps for text-to-speech synthesis and automatic speech recognition, respectively. Many methods have been proposed for either TN or ITN, ranging from weighted finite-state transducers to neura"
url: "https://research.nvidia.com/publication/2021-08_unified-transformer-based-framework-duplex-text-normalization"
status: new
---

# A Unified Transformer-based Framework for Duplex Text Normalization

## 摘要

Text normalization (TN) and inverse text normalization (ITN) are essential preprocessing and postprocessing steps for text-to-speech synthesis and automatic speech recognition, respectively. Many methods have been proposed for either TN or ITN, ranging from weighted finite-state transducers to neural networks. Despite their impressive performance, these methods aim to tackle only one of the two tasks but not both. As a result, in a complete spoken dialog system, two separate models for TN and ITN need to be built. This heterogeneity increases the technical complexity of the system, which in turn increases the cost of maintenance in a production setting. Motivated by this observation, we propose a unified framework for building a single neural duplex system that can simultaneously handle TN and ITN. Combined with a simple but effective data augmentation method, our systems achieve state-of-the-art results on the Google TN dataset for English and Russian. They can also reach over 95% sentence-level accuracy on an internal English TN dataset without any additional fine-tuning. In addition, we also create a cleaned dataset from the Spoken Wikipedia Corpora for German and report the performance of our systems on the dataset. Overall, experimental results demonstrate the proposed duplex text normalization framework is highly effective and applicable to a range of domains and languages

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
