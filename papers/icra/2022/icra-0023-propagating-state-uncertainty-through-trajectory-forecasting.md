---
id: icra-0023
title: "Propagating State Uncertainty Through Trajectory Forecasting"
conference: ICRA 2022
date: 2022-05
authors:
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yifeng Lin"
    affiliation: ""
    is_industry: false
  - name: "Shubham Shrivastava"
    affiliation: ""
    is_industry: false
  - name: "Punarjay Chakravarty"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Autonomous Vehicles"
  - "Computer Vision"
external_links:
  - name: "Paper"
    url: "https://ieeexplore.ieee.org/document/9811776"
abstract: "Uncertainty pervades through the modern robotic autonomy stack, with nearly every component (e.g., sensors, detection, classification, tracking, behavior prediction) producing continuous or discrete probabilistic distributions. Trajectory forecasting, in particular, is surrounded by uncertainty as i"
url: "https://research.nvidia.com/publication/2022-05_propagating-state-uncertainty-through-trajectory-forecasting"
status: new
---

# Propagating State Uncertainty Through Trajectory Forecasting

## 摘要

Uncertainty pervades through the modern robotic autonomy stack, with nearly every component (e.g., sensors, detection, classification, tracking, behavior prediction) producing continuous or discrete probabilistic distributions. Trajectory forecasting, in particular, is surrounded by uncertainty as its inputs are produced by (noisy) upstream perception and its outputs are predictions that are often probabilistic for use in downstream planning. However, most trajectory forecasting methods do not account for upstream uncertainty, instead taking only the most-likely values. As a result, perceptual uncertainties are not propagated through forecasting and predictions are frequently overconfident. To address this, we present a novel method for incorporating perceptual state uncertainty in trajectory forecasting, a key component of which is a new statistical distance-based loss function which encourages predicting uncertainties that better match upstream perception. We evaluate our approach both in illustrative simulations and on large-scale, real-world data, demonstrating its efficacy in propagating perceptual state uncertainty through prediction and producing more calibrated predictions.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
