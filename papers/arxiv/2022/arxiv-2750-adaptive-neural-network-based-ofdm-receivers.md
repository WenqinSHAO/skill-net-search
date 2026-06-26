---
id: "arxiv-2750"
title: "Adaptive Neural Network-based OFDM Receivers"
conference: "arXiv 2022"
date: "2022-07"
authors:
  - name: "Moritz Benedikt Fischer"
    affiliation: "University of Stuttgart"
    is_industry: false
  - name: "Sebastian Dörner"
    affiliation: "University of Stuttgart"
    is_industry: false
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Takayuki Shimizu"
    affiliation: "Toyota Motor North America"
    is_industry: false
  - name: "Hongsheng Lu"
    affiliation: "Toyota Motor North America"
    is_industry: false
  - name: "Stephan ten Brink"
    affiliation: "University of Stuttgart"
    is_industry: false
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
  - name: "Paper"
    url: "https://arxiv.org/abs/2203.13571"
abstract: "We propose and examine the idea of continuously adapting state-of-the-art neural network (NN)-based orthogonal frequency division multiplex (OFDM) receivers to current channel conditions. This online adaptation via retraining is mainly motivated by two reasons: First, receiver design typically focus"
url: "https://research.nvidia.com/publication/2022-07_adaptive-neural-network-based-ofdm-receivers"
status: "new"
---

# Adaptive Neural Network-based OFDM Receivers

## 摘要

We propose and examine the idea of continuously adapting state-of-the-art neural network (NN)-based orthogonal frequency division multiplex (OFDM) receivers to current channel conditions. This online adaptation via retraining is mainly motivated by two reasons: First, receiver design typically focuses on the universal optimal performance for a wide range of possible channel realizations. However, in actual applications and within short time intervals, only a subset of these channel parameters is likely to occur, as macro parameters, e.g., the maximum channel delay, can assumed to be static. Second, in-the-field alterations like temporal interferences or other conditions out of the originally intended specifications can occur on a practical (real-world) transmission. While conventional (filter-based) systems would require reconfiguration or additional signal processing to cope with these unforeseen conditions, NN-based receivers can learn to mitigate previously unseen effects even after their deployment. For this, we showcase on-the-fly adaption to current channel conditions and temporal alterations solely based on recovered labels from an outer forward error correction (FEC) code without any additional piloting overhead. To underline the flexibility of the proposed adaptive training, we showcase substantial gains for scenarios with static channel macro parameters, for out-of-specification usage and for interference compensation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
