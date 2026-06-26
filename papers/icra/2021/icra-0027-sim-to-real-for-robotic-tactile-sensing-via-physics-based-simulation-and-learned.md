---
id: "icra-0027"
title: "Sim-to-Real for Robotic Tactile Sensing via Physics-Based Simulation and Learned Latent Projections"
conference: "ICRA 2021"
date: "2021-06"
authors:
  - name: "Yashraj Narang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Miles Macklin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Website"
    url: "https://sites.google.com/nvidia.com/tactiledata2"
abstract: "Tactile sensing is critical for robotic grasping and manipulation of objects under visual occlusion. However, in contrast to simulations of robot arms and cameras, current simulations of tactile sensors have limited accuracy, speed, and utility. In this work, we develop an efficient 3D finite elemen"
url: "https://research.nvidia.com/publication/2021-06_sim-real-robotic-tactile-sensing-physics-based-simulation-and-learned-latent"
status: "new"
---

# Sim-to-Real for Robotic Tactile Sensing via Physics-Based Simulation and Learned Latent Projections

## 摘要

Tactile sensing is critical for robotic grasping and manipulation of objects under visual occlusion. However, in contrast to simulations of robot arms and cameras, current simulations of tactile sensors have limited accuracy, speed, and utility. In this work, we develop an efficient 3D finite element method (FEM) model of the SynTouch BioTac sensor using an open-access, GPU-based robotics simulator. Our simulations closely reproduce results from an experimentally-validated model in an industry-standard, CPU-based simulator, but at 75x the speed. We then learn latent representations for simulated BioTac deformations and real-world electrical output through self-supervision, as well as projections between the latent spaces using a small supervised dataset. Using these learned latent projections, we accurately synthesize real-world BioTac electrical output and estimate contact patches, both for unseen contact interactions. This work contributes an efficient, freely-accessible FEM model of the BioTac and comprises one of the first efforts to combine self-supervision, cross-modal transfer, and sim-to-real transfer for tactile sensors.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
