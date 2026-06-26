---
id: "cvpr-0058"
title: "Optimal Quantization Using Scaled Codebook"
conference: "CVPR 2021"
date: "2021-06"
authors:
  - name: "Yerlan Idelbayev"
    affiliation: "UC Merced"
    is_industry: false
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maying Shen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Miguel A. Carreira-Perpinan"
    affiliation: "UC Merced"
    is_industry: false
  - name: "Jose M. Alvarez"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
abstract: "We study the problem of quantizing N sorted, scalar datapoints with a fixed codebook containing K entries that are allowed to be rescaled. The problem is defined as finding the optimal scaling factor alpha and the datapoint assignments into the alpha-scaled codebook to minimize the squared error bet"
url: "https://research.nvidia.com/publication/2021-06_optimal-quantization-using-scaled-codebook"
status: "new"
---

# Optimal Quantization Using Scaled Codebook

## 摘要

We study the problem of quantizing N sorted, scalar datapoints with a fixed codebook containing K entries that are allowed to be rescaled. The problem is defined as finding the optimal scaling factor alpha and the datapoint assignments into the alpha-scaled codebook to minimize the squared error between original and quantized points. Previously, the globally optimal algorithms for this problem were derived only for certain codebooks (binary and ternary) or under the assumption of certain distributions (Gaussian, Laplacian). By studying the properties of the optimal quantizer, we derive an O(NK log K) algorithm that is guaranteed to find the optimal quantization parameters for any fixed codebook regardless of data distribution. We apply our algorithm to synthetic and real-world neural network quantization problems and demonstrate the effectiveness of our approach.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
