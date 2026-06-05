---
id: arxiv-2588
title: "FastAdaSP: Multitask-Adapted Efficient Inference for Large Speech Language Model"
conference: arXiv 2024
date: 2024-11
authors:
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yichen Lu"
    affiliation: ""
    is_industry: false
  - name: "Jiaqi Song"
    affiliation: ""
    is_industry: false
  - name: "Shinji Watanabe"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Machine Translation"
  - "Natural Language Processing"
  - "Speech Processing"
external_links:
  - name: "EMNLP"
    url: "https://aclanthology.org/2024.emnlp-industry.33.pdf"
abstract: "In this study, we aim to explore Multitask Speech Language Model (SpeechLM) efficient inference via token reduction. Unlike other modalities such as vision or text, speech has unique temporal dependencies, making previous efficient inference works on other modalities not directly applicable. Further"
url: "https://research.nvidia.com/publication/2024-11_fastadasp-multitask-adapted-efficient-inference-large-speech-language-model"
status: new
---

# FastAdaSP: Multitask-Adapted Efficient Inference for Large Speech Language Model

## 摘要

In this study, we aim to explore Multitask Speech Language Model (SpeechLM) efficient inference via token reduction. Unlike other modalities such as vision or text, speech has unique temporal dependencies, making previous efficient inference works on other modalities not directly applicable. Furthermore, methods for efficient SpeechLM inference on long sequence and sparse signals remain largely unexplored. Then we propose FastAdaSP, a weighted token merging framework specifically designed for various speech-related tasks to improve the trade-off between efficiency and performance. Experimental results on WavLLM and Qwen-Audio show that our method achieves the state-of-the-art (SOTA) efficiency-performance trade-off compared with other baseline methods. Specifically, FastAdaSP achieved 7x memory efficiency and 1.83x decoding throughput without any degradation on tasks like Emotion Recognition (ER) and Spoken Question Answering (SQA).

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
