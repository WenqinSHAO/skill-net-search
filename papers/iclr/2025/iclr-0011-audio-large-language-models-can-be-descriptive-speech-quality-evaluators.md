---
id: "iclr-0011"
title: "Audio Large Language Models Can Be Descriptive Speech Quality Evaluators"
conference: "ICLR 2025"
date: "2025-04"
authors:
  - name: "Chen Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuchen Hu"
    affiliation: "Nanyang Technological University"
    is_industry: false
  - name: "Siyin Wang"
    affiliation: "Tsinghua University"
    is_industry: false
  - name: "Helin Wang"
    affiliation: "JHU"
    is_industry: false
  - name: "Zhehuai Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chao Zhang"
    affiliation: "Tsinghua University"
    is_industry: false
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "EngSiong Chng"
    affiliation: "Nanyang Technological University"
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Natural Language Processing"
  - "Speech Processing"
abstract: "An ideal multimodal agent should be aware of the quality of its input modalities.Recent advances have enabled large language models (LLMs) to incorporate auditory systems for handling various speech-related tasks. However, most audioLLMs remain unaware of the quality of the speech they process. This"
url: "https://research.nvidia.com/publication/2025-04_audio-large-language-models-can-be-descriptive-speech-quality-evaluators"
status: "new"
---

# Audio Large Language Models Can Be Descriptive Speech Quality Evaluators

## 摘要

An ideal multimodal agent should be aware of the quality of its input modalities.Recent advances have enabled large language models (LLMs) to incorporate auditory systems for handling various speech-related tasks. However, most audioLLMs remain unaware of the quality of the speech they process. This limitation arises because speech quality evaluation is typically excluded from multi-tasktraining due to the lack of suitable datasets. To address this, we introduce the firstnatural language-based speech evaluation corpus, generated from authentic human ratings. In addition to the overall Mean Opinion Score (MOS), this corpusoffers detailed analysis across multiple dimensions and identifies causes of qualitydegradation. It also enables descriptive comparisons between two speech samples(A/B tests) with human-like judgment. Leveraging this corpus, we propose analignment approach with LLM distillation (ALLD) to guide the audio LLM inextracting relevant information from raw speech and generating meaningful responses. Experimental results demonstrate that ALLD outperforms the previousstate-of-the-art regression model in MOS prediction, with a mean square error of0.17 and an A/B test accuracy of 98.6%. Additionally, the generated responsesachieve BLEU scores of 25.8 and 30.2 on two tasks, surpassing the capabilities oftask-specific models. This work advances the comprehensive perception of speechsignals by audio LLMs, contributing to the development of real-world auditoryand sensory intelligent agents.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
