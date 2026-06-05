---
id: arxiv-3009
title: "Two-shot Spatially-varying BRDF and Shape Estimation"
conference: arXiv 2020
date: 2020-06
authors:
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Boss"
    affiliation: ""
    is_industry: false
  - name: "Varun Jampani"
    affiliation: ""
    is_industry: false
  - name: "Kihwan Kim"
    affiliation: ""
    is_industry: false
  - name: "Hendrik P.A. Lensch"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/pdf/2004.00403"
  - name: "Video (youtube)"
    url: "https://www.youtube.com/watch?v=Bvjoolt2-iY"
abstract: "Capturing the shape and spatially-varying appearance (SVBRDF) of an object from images is a challenging task that has applications in both computer vision and graphics. Traditional optimization-based approaches often need a large number of images taken from multiple views in a controlled environment"
url: "https://research.nvidia.com/publication/2020-06_two-shot-spatially-varying-brdf-and-shape-estimation"
status: new
---

# Two-shot Spatially-varying BRDF and Shape Estimation

## 摘要

Capturing the shape and spatially-varying appearance (SVBRDF) of an object from images is a challenging task that has applications in both computer vision and graphics. Traditional optimization-based approaches often need a large number of images taken from multiple views in a controlled environment. Newer deep learning-based approaches require only a few input images, but the reconstruction quality is not on par with optimization techniques. We propose a novel deep learning architecture with a stage-wise estimation of shape and SVBRDF. The previous predictions guide each estimation, and a joint refinement network later refines both SVBRDF and shape. We follow a practical mobile image capture setting and use unaligned two-shot flash and no-flash images as input. Both our two-shot image capture and network inference can run on mobile hardware. We also create a large-scale synthetic training dataset with domain-randomized geometry and realistic materials. Extensive experiments on both synthetic and real-world datasets show that our network trained on a synthetic dataset can generalize well to real-world images. Comparisons with recent approaches demonstrate the superior performance of the proposed approach.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
