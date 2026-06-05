---
id: arxiv-2510
title: "QCalEval: Benchmarking Vision-Language Models for Quantum Calibration Plot Understanding"
conference: arXiv 2026
date: 2026-04
authors:
  - name: "Ligeng Zhu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alan Aspuru-Guzik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shuxiang Cao"
    affiliation: ""
    is_industry: false
  - name: "Zijian Zhang"
    affiliation: ""
    is_industry: false
  - name: "Abhishek Agarwal"
    affiliation: ""
    is_industry: false
  - name: "Grace Bratrud"
    affiliation: ""
    is_industry: false
  - name: "Niyaz R. Beysengulov"
    affiliation: ""
    is_industry: false
  - name: "Daniel C. Cole"
    affiliation: ""
    is_industry: false
  - name: "Alejandro Gomez Frieiro"
    affiliation: ""
    is_industry: false
  - name: "Elena O. Glen"
    affiliation: ""
    is_industry: false
  - name: "Hao Hsu"
    affiliation: ""
    is_industry: false
  - name: "Gang Huang"
    affiliation: ""
    is_industry: false
  - name: "Raymond Jow"
    affiliation: ""
    is_industry: false
  - name: "Greshma Shaji"
    affiliation: ""
    is_industry: false
  - name: "Tom Lubowe"
    affiliation: ""
    is_industry: false
  - name: "Luis Mantilla Calderon"
    affiliation: ""
    is_industry: false
  - name: "Nicola Pancotti"
    affiliation: ""
    is_industry: false
  - name: "Joel Pendleton"
    affiliation: ""
    is_industry: false
  - name: "Brandon Severin"
    affiliation: ""
    is_industry: false
  - name: "Charles Etienne Staub"
    affiliation: ""
    is_industry: false
  - name: "Sara Sussman"
    affiliation: ""
    is_industry: false
  - name: "Antti Vepsalainen"
    affiliation: ""
    is_industry: false
  - name: "Neel Rajeshbhai Vora"
    affiliation: ""
    is_industry: false
  - name: "Yilun Xu"
    affiliation: ""
    is_industry: false
  - name: "Varinia Bernales"
    affiliation: ""
    is_industry: false
  - name: "Daniel Bowring"
    affiliation: ""
    is_industry: false
  - name: "Elica Kyoseva"
    affiliation: ""
    is_industry: false
  - name: "Ivan Rungger"
    affiliation: ""
    is_industry: false
  - name: "Giulia Semeghini"
    affiliation: ""
    is_industry: false
  - name: "Sam Stanwyck"
    affiliation: ""
    is_industry: false
  - name: "Timothy Costa"
    affiliation: ""
    is_industry: false
  - name: "Krysta Svore"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "QCalEval benchmark dataset"
    url: "https://huggingface.co/datasets/nvidia/QCalEval"
  - name: "Evaluation Scripts"
    url: "https://github.com/nvidia/QCalEval"
  - name: "NVIDIA Ising Calibration 1 model weights"
    url: "https://huggingface.co/nvidia/Ising-Calibration-1-35B-A3B"
abstract: "Quantum computing calibration depends on interpreting experimental data, and calibration plots provide the most universal human-readable representation for this task, yet no systematic evaluation exists of how well vision-language models (VLMs) interpret them. We introduce&nbsp;QCalEval, the first V"
url: "https://research.nvidia.com/publication/2026-04%5Fqcaleval-benchmarking-vision-language-models-quantum-calibration-plot"
status: new
---

# QCalEval: Benchmarking Vision-Language Models for Quantum Calibration Plot Understanding

## 摘要

Quantum computing calibration depends on interpreting experimental data, and calibration plots provide the most universal human-readable representation for this task, yet no systematic evaluation exists of how well vision-language models (VLMs) interpret them. We introduce&nbsp;QCalEval, the first VLM benchmark for quantum calibration plots: 243 samples across 87 scenario types from 22 experiment families, spanning superconducting qubits and neutral atoms, evaluated on six question types in both zero-shot and in-context learning settings. The best general-purpose zero-shot model reaches a mean score of 72.3, and many open-weight models degrade under multi-image in-context learning, whereas frontier closed models improve substantially. A supervised fine-tuning ablation at the 9-billion-parameter scale shows that supervision format is critical, zero-shot-formatted and in-context-learning-formatted fine-tuning improve different capabilities, and no single recipe improves open-ended analysis. As a reference case study, we release&nbsp;NVIDIA Ising Calibration 1, an open-weight model based on Qwen3.5-35B-A3B that reaches 74.7 zero-shot average score.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
