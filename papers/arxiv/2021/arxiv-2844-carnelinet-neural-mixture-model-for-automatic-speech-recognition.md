---
id: "arxiv-2844"
title: "CarneliNet: Neural Mixture Model for Automatic Speech Recognition"
conference: "arXiv 2021"
date: "2021-07"
authors:
  - name: "Aleksei Kalinov"
    affiliation: "Skolkovo Institute of Science and Technology"
    is_industry: false
  - name: "Somshubra Majumdar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jagadeesh Balam"
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
    url: "https://arxiv.org/abs/2107.10708"
abstract: "End-to-end automatic speech recognition systems have achieved great accuracy by using deeper and deeper models. However, the increased depth comes with a larger receptive field that can negatively impact model performance in streaming scenarios. We propose an alternative approach that we call Neural"
url: "https://research.nvidia.com/publication/2021-07_carnelinet-neural-mixture-model-automatic-speech-recognition"
status: "new"
---

# CarneliNet: Neural Mixture Model for Automatic Speech Recognition

## 摘要

End-to-end automatic speech recognition systems have achieved great accuracy by using deeper and deeper models. However, the increased depth comes with a larger receptive field that can negatively impact model performance in streaming scenarios. We propose an alternative approach that we call Neural Mixture Model. The basic idea is to introduce a parallel mixture of shallow networks instead of a very deep network. To validate this idea we design CarneliNet -- a CTC-based neural network composed of three mega-blocks. Each mega-block consists of multiple parallel shallow sub-networks based on 1D depthwise-separable convolutions. We evaluate the model on LibriSpeech, MLS and AISHELL-2 datasets and achieved close to state-of-the-art results for CTC-based models. Finally, we demonstrate that one can dynamically reconfigure the number of parallel sub-networks to accommodate the computational requirements without retraining.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
