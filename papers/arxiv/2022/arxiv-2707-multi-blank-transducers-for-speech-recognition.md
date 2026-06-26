---
id: "arxiv-2707"
title: "Multi-blank Transducers for Speech Recognition"
conference: "arXiv 2022"
date: "2022-11"
authors:
  - name: "Hainan Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fei Jia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Somshubra Majumdar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shinji Watanabe"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Boris Ginsburg"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Speech Processing"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2211.03541"
abstract: "This paper proposes a modification to RNN-Transducer (RNN-T) models for automatic speech recognition (ASR). In standard RNN-T, the emission of a blank symbol consumes exactly one input frame; in our proposed method, we introduce additional blank symbols, which consume two or more input frames when e"
url: "https://research.nvidia.com/publication/2022-11_multi-blank-transducers-speech-recognition"
status: "new"
---

# Multi-blank Transducers for Speech Recognition

## 摘要

This paper proposes a modification to RNN-Transducer (RNN-T) models for automatic speech recognition (ASR). In standard RNN-T, the emission of a blank symbol consumes exactly one input frame; in our proposed method, we introduce additional blank symbols, which consume two or more input frames when emitted. We refer to the added symbols as big blanks, and the method multi-blank RNN-T. For training multi-blank RNN-Ts, we propose a novel logit under-normalization method in order to prioritize emissions of big blanks. With experiments on multiple languages and datasets, we show that multi-blank RNN-T methods could bring relative speedups of over +90%/+139% to model inference for English Librispeech and German Multilingual Librispeech datasets, respectively. The multi-blank RNN-T method also improves ASR accuracy consistently. We will release our implementation of the method in the NeMo (this https URL) toolkit.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
