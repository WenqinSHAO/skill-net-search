---
id: "arxiv-2677"
title: "Efficient Sequence Transduction by Jointly Predicting Tokens and Durations"
conference: "arXiv 2023"
date: "2023-04"
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
  - name: "He Huang"
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
  - "Machine Translation"
  - "Speech Processing"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2304.06795"
abstract: "This paper introduces a novel Token-and-Duration Transducer (TDT) architecture for sequence-to-sequence tasks. TDT extends conventional RNN-Transducer architectures by jointly predicting both a token and its duration, i.e. the number of input frames covered by the emitted token. This is achieved by "
url: "https://research.nvidia.com/publication/2023-04_efficient-sequence-transduction-jointly-predicting-tokens-and-durations"
status: "new"
---

# Efficient Sequence Transduction by Jointly Predicting Tokens and Durations

## 摘要

This paper introduces a novel Token-and-Duration Transducer (TDT) architecture for sequence-to-sequence tasks. TDT extends conventional RNN-Transducer architectures by jointly predicting both a token and its duration, i.e. the number of input frames covered by the emitted token. This is achieved by using a joint network with two outputs which are independently normalized to generate distributions over tokens and durations. During inference, TDT models can skip input frames guided by the predicted duration output, which makes them significantly faster than conventional Transducers which process the encoder output frame by frame. TDT models achieve both better accuracy and significantly faster inference than conventional Transducers on different sequence transduction tasks. TDT models for Speech Recognition achieve better accuracy and up to 2.82X faster inference than conventional Transducers. TDT models for Speech Translation achieve an absolute gain of over 1 BLEU on the MUST-C test compared with conventional Transducers, and its inference is 2.27X faster. In Speech Intent Classification and Slot Filling tasks, TDT models improve the intent accuracy by up to over 1% (absolute) over conventional Transducers, while running up to 1.28X faster. Our implementation of the TDT model will be open-sourced with the NeMo (this https URL) toolkit.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
