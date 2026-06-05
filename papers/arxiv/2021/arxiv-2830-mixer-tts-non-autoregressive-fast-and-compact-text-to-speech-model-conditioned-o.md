---
id: arxiv-2830
title: "Mixer-TTS: non-autoregressive, fast and compact text-to-speech model conditioned on language model embeddings"
conference: arXiv 2021
date: 2021-10
authors:
  - name: "Oktai Tatanov"
    affiliation: ""
    is_industry: false
  - name: "Stanislav Beliaev"
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
    url: "https://arxiv.org/abs/2110.03584"
abstract: "This paper describes Mixer-TTS, a non-autoregressive model for mel-spectrogram generation. The model is based on the MLP-Mixer architecture adapted for speech synthesis. The basic Mixer-TTS contains pitch and duration predictors, with the latter being trained with an unsupervised TTS alignment frame"
url: "https://research.nvidia.com/publication/2021-10_mixer-tts-non-autoregressive-fast-and-compact-text-speech-model-conditioned-0"
status: new
---

# Mixer-TTS: non-autoregressive, fast and compact text-to-speech model conditioned on language model embeddings

## 摘要

This paper describes Mixer-TTS, a non-autoregressive model for mel-spectrogram generation. The model is based on the MLP-Mixer architecture adapted for speech synthesis. The basic Mixer-TTS contains pitch and duration predictors, with the latter being trained with an unsupervised TTS alignment framework. Alongside the basic model, we propose the extended version which additionally uses token embeddings from a pre-trained language model. Basic Mixer-TTS and its extended version achieve a mean opinion score (MOS) of 4.05 and 4.11, respectively, compared to a MOS of 4.27 of original LJSpeech samples. Both versions have a small number of parameters and enable much faster speech synthesis compared to the models with similar quality.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
