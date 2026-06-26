---
id: "arxiv-2709"
title: "Adapter-Based Extension of Multi-Speaker Text-to-Speech Model for New Speakers"
conference: "arXiv 2022"
date: "2022-11"
authors:
  - name: "Cheng-Ping Hsieh"
    affiliation: "University of California San Diego"
    is_industry: false
  - name: "Subhankar Ghosh"
    affiliation: "NVIDIA"
    is_industry: true
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
    url: "https://arxiv.org/abs/2211.00585"
abstract: "Fine-tuning is a popular method for adapting text-to-speech (TTS) models to new speakers. However this approach has some challenges. Usually fine-tuning requires several hours of high quality speech per speaker. There is also that fine-tuning will negatively affect the quality of speech synthesis fo"
url: "https://research.nvidia.com/publication/2022-11_adapter-based-extension-multi-speaker-text-speech-model-new-speakers"
status: "new"
---

# Adapter-Based Extension of Multi-Speaker Text-to-Speech Model for New Speakers

## 摘要

Fine-tuning is a popular method for adapting text-to-speech (TTS) models to new speakers. However this approach has some challenges. Usually fine-tuning requires several hours of high quality speech per speaker. There is also that fine-tuning will negatively affect the quality of speech synthesis for previously learnt speakers. In this paper we propose an alternative approach for TTS adaptation based on using parameter-efficient adapter modules. In the proposed approach, a few small adapter modules are added to the original network. The original weights are frozen, and only the adapters are fine-tuned on speech for new speaker. The parameter-efficient fine-tuning approach will produce a new model with high level of parameter sharing with original model. Our experiments on LibriTTS, HiFi-TTS and VCTK datasets validate the effectiveness of adapter-based method through objective and subjective metrics.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
