---
id: arxiv-2674
title: "Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition"
conference: arXiv 2023
date: 2023-05
authors:
  - name: "Dima Rekesh"
    affiliation: ""
    is_industry: false
  - name: "Nithin Rao Koluguri"
    affiliation: ""
    is_industry: false
  - name: "Samuel Kriman"
    affiliation: ""
    is_industry: false
  - name: "Somshubra Majumdar"
    affiliation: ""
    is_industry: false
  - name: "Vahid Noroozi"
    affiliation: ""
    is_industry: false
  - name: "He Huang"
    affiliation: ""
    is_industry: false
  - name: "Oleskii Hrinchuk"
    affiliation: ""
    is_industry: false
  - name: "Krishna Puvvada"
    affiliation: ""
    is_industry: false
  - name: "Ankur Kumar"
    affiliation: ""
    is_industry: false
  - name: "Jagadeesh Balam"
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
    url: "https://arxiv.org/abs/2305.05084"
abstract: "Conformer-based models have become the dominant end-to-end architecture for speech processing tasks. With the objective of enhancing the conformer architecture for efficient training and inference, we carefully redesigned Conformer with a novel downsampling schema. The proposed model, named Fast Con"
url: "https://research.nvidia.com/publication/2023-05_fast-conformer-linearly-scalable-attention-efficient-speech-recognition"
status: new
---

# Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition

## 摘要

Conformer-based models have become the dominant end-to-end architecture for speech processing tasks. With the objective of enhancing the conformer architecture for efficient training and inference, we carefully redesigned Conformer with a novel downsampling schema. The proposed model, named Fast Conformer(FC), is 2.8x faster than the original Conformer, supports scaling to Billion parameters without any changes to the core architecture and also achieves state-of-the-art accuracy on Automatic Speech Recognition benchmarks. To enable transcription of long-form speech up to 11 hours, we replaced global attention with limited context attention post-training, while also improving accuracy through fine-tuning with the addition of a global token. Fast Conformer, when combined with a Transformer decoder also outperforms the original Conformer in accuracy and in speed for Speech Translation and Spoken Language Understanding.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
