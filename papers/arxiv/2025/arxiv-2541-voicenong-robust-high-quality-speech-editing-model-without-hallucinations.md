---
id: "arxiv-2541"
title: "VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations"
conference: "arXiv 2025"
date: "2025-08"
authors:
  - name: "Sung-Feng Huang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Heng-Cheng Kuo"
    affiliation: "National Taiwan University"
    is_industry: false
  - name: "Zhehuai Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xuesong Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pin-Jui Ku"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ante Jukić"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu Tsao"
    affiliation: "Academia Sinica"
    is_industry: false
  - name: "Frank Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hung-yi Lee"
    affiliation: "National Taiwan University"
    is_industry: false
  - name: "Szu-Wei Fu"
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
  - "Generative AI"
  - "Speech Processing"
external_links:
  - name: "Demo page"
    url: "https://jasonswfu.github.io/NoNG-IS-/"
abstract: "Voicebox and VoiceCraft are the current most representative models for non-autoregressive and autoregressive speech editing, respectively. Although both of them can generate high-quality speech edits, we identify their limitations: Voicebox is not good at editing speech with background audio, while "
url: "https://research.nvidia.com/publication/2025-08_voicenong-robust-high-quality-speech-editing-model-without-hallucinations"
status: "new"
---

# VoiceNoNG: Robust High-Quality Speech Editing Model without Hallucinations

## 摘要

Voicebox and VoiceCraft are the current most representative models for non-autoregressive and autoregressive speech editing, respectively. Although both of them can generate high-quality speech edits, we identify their limitations: Voicebox is not good at editing speech with background audio, while VoiceCraft suffers from the hallucination-like problem. To maintain speech quality for varying audio scenarios and address the hallucination issue, we introduce VoiceNoNG, which combines the strengths of both model frameworks. VoiceNoNG utilizes a latent flow-matching framework to model the pre-quantization features of a neural codec. The vector quantizer in the neural codec provides additional robustness against minor prediction errors from the editing model, which enables VoiceNoNG to achieve state-of-the-art performance in both objective and subjective evaluations under diverse audio conditions.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
