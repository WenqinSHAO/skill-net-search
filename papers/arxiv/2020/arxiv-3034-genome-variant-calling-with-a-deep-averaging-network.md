---
id: "arxiv-3034"
title: "Genome Variant Calling with a Deep Averaging Network"
conference: "arXiv 2020"
date: "2020-03"
authors:
  - name: "Nikolai Yakovenko"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Avantika Lal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Johnny Israeli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bryan Catanzaro"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Medical_imaging
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Medical"
abstract: "Variant calling, the problem of estimating whether a position in a DNA sequence differs from a reference sequence, given noisy, redundant, overlapping short sequences that cover that position, is fundamental to genomics. We propose a deep averaging network designed specifically for variant calling. "
url: "https://research.nvidia.com/publication/2020-03_genome-variant-calling-deep-averaging-network"
status: "new"
---

# Genome Variant Calling with a Deep Averaging Network

## 摘要

Variant calling, the problem of estimating whether a position in a DNA sequence differs from a reference sequence, given noisy, redundant, overlapping short sequences that cover that position, is fundamental to genomics. We propose a deep averaging network designed specifically for variant calling. Our model takes into account the independence of each short input read sequence by transforming individual reads through a series of convolutional layers, limiting the communication between individual reads to averaging and concatenating operations. Training and testing on the precisionFDA Truth Challenge (pFDA), we match state of the art overall 99.89 F1 score. Genome datasets exhibit extreme skew between easy examples and those on the decision boundary. We take advantage of this property to converge models at 5x the speed of standard epoch-based training by skipping easy examples during training. To facilitate future work, we release our code, trained models and pre-processed public domain datasets.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
