---
id: icra-0024
title: "PredictionNet: Real-Time Joint Probabilistic Traffic Prediction for Planning, Control, and Simulation"
conference: ICRA 2022
date: 2022-03
authors:
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexey Kamenev"
    affiliation: ""
    is_industry: false
  - name: "Lirui Wang"
    affiliation: ""
    is_industry: false
  - name: "Ollin Boer Bohan"
    affiliation: ""
    is_industry: false
  - name: "Ishwar Kulkarni"
    affiliation: ""
    is_industry: false
  - name: "Bilal Kartal"
    affiliation: ""
    is_industry: false
  - name: "Artem Molchanov"
    affiliation: ""
    is_industry: false
  - name: "David Nister"
    affiliation: ""
    is_industry: false
  - name: "Nikolai Smolyanskiy"
    affiliation: ""
    is_industry: false
topics:
  - Applied_perception
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Autonomous Vehicles"
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2109.11094"
abstract: "Predicting the future motion of traffic agents is crucial for safe and efficient autonomous driving. To this end, we present PredictionNet, a deep neural network (DNN) that predicts the motion of all surrounding traffic agents together with the ego-vehicle's motion. All predictions are probabilistic"
url: "https://research.nvidia.com/publication/2022-03_predictionnet-real-time-joint-probabilistic-traffic-prediction-planning-control"
status: new
---

# PredictionNet: Real-Time Joint Probabilistic Traffic Prediction for Planning, Control, and Simulation

## 摘要

Predicting the future motion of traffic agents is crucial for safe and efficient autonomous driving. To this end, we present PredictionNet, a deep neural network (DNN) that predicts the motion of all surrounding traffic agents together with the ego-vehicle's motion. All predictions are probabilistic and are represented in a simple top-down rasterization that allows an arbitrary number of agents. Conditioned on a multi-layer map with lane information, the network outputs future positions, velocities, and backtrace vectors jointly for all agents including the ego-vehicle in a single pass. Trajectories are then extracted from the output. &nbsp;The network can be used to simulate realistic traffic, and it produces competitive results on popular benchmarks. &nbsp;More importantly, it has been used to successfully control a real-world vehicle for hundreds of kilometers, by combining it with a motion planning/control subsystem. The network runs faster than real-time on an embedded GPU, and the system shows good generalization (across sensory modalities and locations) due to the choice of input representation. Furthermore, we demonstrate that by extending the DNN with reinforcement learning (RL), it can better handle rare or unsafe events like aggressive maneuvers and crashes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
