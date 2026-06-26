---
id: "arxiv-2854"
title: "Real-time Neural Radiance Caching for Path Tracing"
conference: "arXiv 2021"
date: "2021-06"
authors:
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "GTC Presentation"
    url: "https://www.nvidia.com/en-us/on-demand/session/gtcspring21-e31307/"
  - name: "Neural Network Code (tiny-cuda-nn library)"
    url: "https://github.com/nvlabs/tiny-cuda-nn"
  - name: "Interactive Results Explorer"
    url: "https://tom94.net/data/publications/mueller21realtime/interactive-viewer/"
abstract: "We introduce a real-time neural radiance caching technique for path-traced global illumination. Our system is designed to handle fully dynamic scenes, and makes no assumptions about the lighting, geometry, and materials. The data-driven nature of our approach sidesteps many difficulties of caching a"
url: "https://research.nvidia.com/publication/2021-06_real-time-neural-radiance-caching-path-tracing"
status: "new"
---

# Real-time Neural Radiance Caching for Path Tracing

## 摘要

We introduce a real-time neural radiance caching technique for path-traced global illumination. Our system is designed to handle fully dynamic scenes, and makes no assumptions about the lighting, geometry, and materials. The data-driven nature of our approach sidesteps many difficulties of caching algorithms, such as locating, interpolating, and updating cache points. Since pretraining neural networks to handle novel, dynamic scenes is a formidable generalization challenge, we do away with pretraining and instead achieve generalization via adaptation, i.e. we opt for training the radiance cache while rendering. We employ self-training—reminiscent of radiosity algorithms—to provide low-noise training targets and simulate infinite-bounce transport by merely iterating few-bounce training updates. The updates and cache queries incur a mild overhead—about 2.6ms on full HD resolution—thanks to a streaming implementation of the neural network that fully exploits modern hardware. We demonstrate significant noise reduction at the cost of little induced bias, and report state-of-the-art, real-time performance on a number of challenging scenarios.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
