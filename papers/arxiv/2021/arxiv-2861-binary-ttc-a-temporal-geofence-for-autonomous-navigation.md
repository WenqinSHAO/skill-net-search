---
id: arxiv-2861
title: "Binary TTC: A Temporal Geofence for Autonomous Navigation"
conference: arXiv 2021
date: 2021-06
authors:
  - name: "Abhishek Badki"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Orazio Gallo"
    affiliation: ""
    is_industry: false
  - name: "Pradeep Sen"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Computational Photography and Imaging"
  - "Computer Vision"
external_links:
  - name: "Teaser Video"
    url: "https://youtu.be/uUQJcjyerM4"
  - name: "Official project page (with code)"
    url: "https://github.com/NVlabs/BiTTC"
  - name: "Paper"
    url: "https://arxiv.org/abs/2101.04777"
abstract: "Time-to-contact (TTC), the time for an object to collide with the observer's plane, is a powerful tool for path planning: it is potentially more informative than the depth, velocity, and acceleration of objects in the scene---even for humans. TTC presents several advantages, including requiring only"
url: "https://research.nvidia.com/publication/2021-06_binary-ttc-temporal-geofence-autonomous-navigation"
status: new
---

# Binary TTC: A Temporal Geofence for Autonomous Navigation

## 摘要

Time-to-contact (TTC), the time for an object to collide with the observer's plane, is a powerful tool for path planning: it is potentially more informative than the depth, velocity, and acceleration of objects in the scene---even for humans. TTC presents several advantages, including requiring only a monocular, uncalibrated camera. However, regressing TTC for each pixel is not straightforward, and most existing methods make over-simplifying assumptions about the scene. We address this challenge by estimating TTC via a series of simpler, binary classifications. We predict with&nbsp;low latency&nbsp;whether the observer will collide with an obstacle&nbsp;within a certain time,&nbsp;which is often more critical than knowing exact, per-pixel TTC. For such scenarios, our method offers a temporal geofence in 6.4 ms---over 25x faster than existing methods. Our approach can also estimate per-pixel TTC with arbitrarily fine quantization (including continuous values), when the computational budget allows for it. To the best of our knowledge, our method is the first to offer TTC information (binary or coarsely quantized) at sufficiently high frame-rates for practical use.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
