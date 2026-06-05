---
id: icra-0011
title: "Planning with Occluded Traffic Agents using Bi-Level Variational Occlusion Models"
conference: ICRA 2023
date: 2023-05
authors:
  - name: "Peter Karkus"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Filippos Christianos"
    affiliation: ""
    is_industry: false
  - name: "Stefano V. Albrecht"
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
  - "Computer Vision"
  - "Resilience and Safety"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2210.14584"
abstract: "Reasoning with occluded traffic agents is a significant open challenge for planning for autonomous vehicles. Recent deep learning models have shown impressive results for predicting occluded agents based on the behaviour of nearby visible agents; however, as we show in experiments, these models are "
url: "https://research.nvidia.com/publication/2023-05_planning-occluded-traffic-agents-using-bi-level-variational-occlusion-models"
status: new
---

# Planning with Occluded Traffic Agents using Bi-Level Variational Occlusion Models

## 摘要

Reasoning with occluded traffic agents is a significant open challenge for planning for autonomous vehicles. Recent deep learning models have shown impressive results for predicting occluded agents based on the behaviour of nearby visible agents; however, as we show in experiments, these models are difficult to integrate into downstream planning. To this end, we propose Bi-level Variational Occlusion Models (BiVO), a two-step generative model that first predicts likely locations of occluded agents, and then generates likely trajectories for the occluded agents. In contrast to existing methods, BiVO outputs a trajectory distribution which can then be sampled from and integrated into standard downstream planning. We evaluate the method in closed-loop replay simulation using the real-world nuScenes dataset. Our results suggest that BiVO can successfully learn to predict occluded agent trajectories, and these predictions lead to better subsequent motion plans in critical scenarios.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
