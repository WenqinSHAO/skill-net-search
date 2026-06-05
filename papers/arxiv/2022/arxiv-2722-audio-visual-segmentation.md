---
id: arxiv-2722
title: "Audio-Visual Segmentation"
conference: arXiv 2022
date: 2022-10
authors:
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jinxin Zhou"
    affiliation: ""
    is_industry: false
  - name: "Yiran Zhong"
    affiliation: ""
    is_industry: false
  - name: "et al."
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2207.05042"
  - name: "code"
    url: "https://github.com/OpenNLPLab/AVSBench"
  - name: "website"
    url: "https://opennlplab.github.io/AVSBench/"
abstract: "We propose to explore a new problem called audio-visual segmentation (AVS), in which the goal is to output a pixel-level map of the object(s) that produce sound at the time of the image frame. To facilitate this research, we construct the first audio-visual segmentation benchmark (AVSBench), providi"
url: "https://research.nvidia.com/publication/2022-10_audio-visual-segmentation"
status: new
---

# Audio-Visual Segmentation

## 摘要

We propose to explore a new problem called audio-visual segmentation (AVS), in which the goal is to output a pixel-level map of the object(s) that produce sound at the time of the image frame. To facilitate this research, we construct the first audio-visual segmentation benchmark (AVSBench), providing pixel-wise annotations for the sounding objects in audible videos. Two settings are studied with this benchmark: 1) semi-supervised audio-visual segmentation with a single sound source and 2) fully-supervised audio-visual segmentation with multiple sound sources. To deal with the AVS problem, we propose a novel method that uses a temporal pixel-wise audio-visual interaction module to inject audio semantics as guidance for the visual segmentation process. We also design a regularization loss to encourage the audio-visual mapping during training. Quantitative and qualitative experiments on the AVSBench compare our approach to several existing methods from related tasks, demonstrating that the proposed method is promising for building a bridge between the audio and pixel-wise visual semantics.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
