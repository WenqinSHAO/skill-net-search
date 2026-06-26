---
id: "arxiv-2634"
title: "A Neural Receiver for 5G NR Multi-user MIMO"
conference: "arXiv 2023"
date: "2023-12"
authors:
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fayçal Aït Aoudia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jakob Hoydis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andreas Oeldemann"
    affiliation: "Rohde & Schwarz"
    is_industry: false
  - name: "Andreas Roessler"
    affiliation: "Rohde & Schwarz"
    is_industry: false
  - name: "Timo Mayer"
    affiliation: "Rohde & Schwarz"
    is_industry: false
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Telecommunications"
abstract: "We introduce a neural network (NN)-based multiuser multiple-input multiple-output (MU-MIMO) receiver with 5G New Radio (5G NR) physical uplink shared channel (PUSCH) compatibility. The NN architecture is based on convolution layers to exploit the time and frequency correlation of the channel and a g"
url: "https://research.nvidia.com/publication/2023-12_neural-receiver-5g-nr-multi-user-mimo"
status: "new"
---

# A Neural Receiver for 5G NR Multi-user MIMO

## 摘要

We introduce a neural network (NN)-based multiuser multiple-input multiple-output (MU-MIMO) receiver with 5G New Radio (5G NR) physical uplink shared channel (PUSCH) compatibility. The NN architecture is based on convolution layers to exploit the time and frequency correlation of the channel and a graph neural network (GNN) to handle multiple users. The proposed architecture adapts to an arbitrary number of sub-carriers and supports a varying number of multiple-input multiple-output (MIMO) layers and users without the need for any retraining. The receiver operates on an entire 5G NR slot, i.e., processes the entire received orthogonal frequency division multiplexing (OFDM) time-frequency resource grid by jointly performing channel estimation, equalization, and demapping. The proposed architecture operates less than 1 dB away from a baseline using linear minimum mean square error (LMMSE) channel estimation with K-best detection but benefits from a significantly lower computational complexity. We show the importance of a carefully designed training process such that the trained receiver is universal for a wide range of different unseen channel conditions. Finally, we demonstrate the results of a hardware-in-the-loop verification based on 3GPP compliant conformance test scenarios.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
