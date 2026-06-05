---
id: arxiv-2505
title: "Editing Physiological Signals in Videos Using Latent Representations"
conference: arXiv 2026
date: 2026-06
authors:
  - name: "Josef Spjut"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tianwen Zhou"
    affiliation: ""
    is_industry: false
  - name: "Akshay Paruchuri"
    affiliation: ""
    is_industry: false
  - name: "Kaan Akşit"
    affiliation: ""
    is_industry: false
topics:
  - Applied_perception
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Generative AI"
  - "Human Computer Interaction"
external_links:
  - name: "GitHub Repository"
    url: "https://github.com/complight/PhysioLatent"
  - name: "arxiv"
    url: "https://arxiv.org/abs/2509.25348"
abstract: "Camera-based physiological signal estimation provides a convenient and non-contact way to monitor heart rate, but it also raises serious privacy concerns because facial videos can leak sensitive information about a person’s health and emotional state. We present a learned framework for editing physi"
url: "https://research.nvidia.com/publication/2026-06%5Fediting-physiological-signals-videos-using-latent-representations"
status: new
---

# Editing Physiological Signals in Videos Using Latent Representations

## 摘要

Camera-based physiological signal estimation provides a convenient and non-contact way to monitor heart rate, but it also raises serious privacy concerns because facial videos can leak sensitive information about a person’s health and emotional state. We present a learned framework for editing physiological signals in videos while preserving visual fidelity. Our method first encodes an input video into a latent representation using a pretrained 3D Variational Autoencoder, and embeds a target heart-rate prompt through a frozen text encoder. The two representations are fused by trainable spatio-temporal layers with Adaptive Layer Normalization to model the strong temporal coherence of remote photoplethysmography signals. To better preserve subtle physiological variations during reconstruction, we apply Feature-wise Linear Modulation in the decoder and fine-tune its output layer. Across multiple benchmark datasets, our approach preserves visual quality with an average PSNR of 38.96 dB and SSIM of 0.98, while achieving an average heart-rate modulation error of 10.00 bpm MAE and 10.09% MAPE under a state-of-the-art rPPG estimator. These results suggest that our framework is useful for privacy-preserving video sharing, biometric anonymization, and the generation of realistic videos with controllable vital signs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
