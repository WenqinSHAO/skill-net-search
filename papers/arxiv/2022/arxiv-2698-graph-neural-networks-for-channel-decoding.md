---
id: "arxiv-2698"
title: "Graph Neural Networks for Channel Decoding"
conference: "arXiv 2022"
date: "2022-12"
authors:
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jakob Hoydis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fayçal Aït Aoudia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Telecommunications"
external_links:
  - name: "Sourcecode"
    url: "https://github.com/NVlabs/gnn-decoder"
  - name: "Paper"
    url: "https://arxiv.org/pdf/2207.14742.pdf"
abstract: "In this work, we propose a fully differentiable graph neural network (GNN)-based architecture for channel decoding and showcase a competitive decoding performance for various coding schemes, such as low-density parity-check (LDPC) and BCH codes. The idea is to let a neural network (NN) learn a gener"
url: "https://research.nvidia.com/publication/2022-12_graph-neural-networks-channel-decoding"
status: "new"
---

# Graph Neural Networks for Channel Decoding

## 摘要

In this work, we propose a fully differentiable graph neural network (GNN)-based architecture for channel decoding and showcase a competitive decoding performance for various coding schemes, such as low-density parity-check (LDPC) and BCH codes. The idea is to let a neural network (NN) learn a generalized message passing algorithm over a given graph that represents the forward error correction (FEC) code structure by replacing node and edge message updates with trainable functions. Contrary to many other deep learning-based decoding approaches, the proposed solution enjoys scalability to arbitrary block lengths and the training is not limited by the curse of dimensionality. We benchmark our proposed decoder against state-of-the-art in conventional channel decoding as well as against recent deep learning-based results. For the (63,45) BCH code, our solution outperforms weighted belief propagation (BP) decoding by approximately 0.4 dB with significantly less decoding iterations and even for 5G NR LDPC codes, we observe a competitive performance when compared to conventional BP decoding. For the BCH codes, the resulting GNN decoder can be fully parametrized with only 9640 weights.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
