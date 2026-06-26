---
id: "arxiv-2694"
title: "Learning Joint Detection, Equalization and Decoding for Short-Packet Communications"
conference: "arXiv 2022"
date: "2022-12"
authors:
  - name: "Sebastian Dörner"
    affiliation: "University of Stuttgart"
    is_industry: false
  - name: "Jannis Clausius"
    affiliation: "University of Stuttgart"
    is_industry: false
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephan ten Brink"
    affiliation: "University of Stuttgart"
    is_industry: false
topics:
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Telecommunications"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2207.05699"
abstract: "We propose and practically demonstrate a joint detection and decoding scheme for short-packet wireless communications in scenarios that require to first detect the presence of a message before actually decoding it. For this, we extend the recently proposed serial Turbo-autoencoder neural network (NN"
url: "https://research.nvidia.com/publication/2022-12_learning-joint-detection-equalization-and-decoding-short-packet-communications"
status: "new"
---

# Learning Joint Detection, Equalization and Decoding for Short-Packet Communications

## 摘要

We propose and practically demonstrate a joint detection and decoding scheme for short-packet wireless communications in scenarios that require to first detect the presence of a message before actually decoding it. For this, we extend the recently proposed serial Turbo-autoencoder neural network (NN) architecture and train it to find short messages that can be, all “at once”, detected, synchronized, equalized and decoded when sent over an unsynchronized channel with memory. The conceptional advantage of the proposed system stems from a holistic message structure with superimposed pilots for joint detection and decoding without the need of relying on a dedicated preamble. This results not only in a higher spectral efficiency, but also translates into the possibility of shorter messages compared to using a dedicated preamble. We compare the detection error rate (DER), bit error rate (BER) and block error rate (BLER) performance of the proposed system with a hand-crafted state-of-the-art conventional baseline and our simulations show a significant advantage of the proposed autoencoder-based system over the conventional baseline in every scenario up to messages conveying k = 96 information bits. Finally, we practically evaluate and confirm the improved performance of the proposed system over-the-air (OTA) using a software-defined radio (SDR)-based measurement testbed.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
