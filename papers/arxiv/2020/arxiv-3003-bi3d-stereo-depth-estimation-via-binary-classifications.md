---
id: "arxiv-3003"
title: "Bi3D: Stereo Depth Estimation via Binary Classifications"
conference: "arXiv 2020"
date: "2020-06"
authors:
  - name: "Abhishek Badki"
    affiliation: "UC Santa Barbara"
    is_industry: false
  - name: "Alejandro Troccoli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kihwan Kim"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pradeep Sen"
    affiliation: "UC Santa Barbara"
    is_industry: false
  - name: "Orazio Gallo"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computational Photography and Imaging"
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Video teaser"
    url: "https://youtu.be/HuEwjpw5O64"
  - name: "Paper on arXiv"
    url: "https://arxiv.org/abs/2005.07274"
  - name: "Code (coming soon)"
    url: "https://github.com/NVlabs/bi3d"
abstract: "Stereo-based depth estimation is a cornerstone of computer vision, with state-of-the-art methods delivering accurate results in real time. For several applications such as autonomous navigation, however, it may be useful to trade accuracy for lower latency. We present Bi3D, a method that estimates d"
url: "https://research.nvidia.com/publication/2020-06_bi3d-stereo-depth-estimation-binary-classifications"
status: "new"
---

# Bi3D: Stereo Depth Estimation via Binary Classifications

## 摘要

Stereo-based depth estimation is a cornerstone of computer vision, with state-of-the-art methods delivering accurate results in real time. For several applications such as autonomous navigation, however, it may be useful to trade accuracy for lower latency. We present Bi3D, a method that estimates depth via a series of binary classifications. Rather than testing if objects are at a particular depth D, as existing stereo methods do, it classifies them as being closer or farther than D. This property offers a powerful mechanism to balance accuracy and latency. Given a strict time budget, Bi3D can detect objects closer than a given distance in as little as a few milliseconds, or estimate depth with arbitrarily coarse quantization, with complexity linear with the number of quantization levels. Bi3D can also use the allotted quantization levels to get continuous depth, but in a specific depth range. For standard stereo (i.e., continuous depth on the whole range), our method is close to or on par with state-of-the-art, finely tuned stereo methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
