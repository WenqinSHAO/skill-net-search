---
id: "icml-0014"
title: "Spherical Fourier Neural Operators: Learning Stable Dynamics on the Sphere"
conference: "ICML 2023"
date: "2023-06"
authors:
  - name: "Boris Bonev"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thorsten Kurth"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Christian Hundt"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jaideep Pathak"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maximilian Baust"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karthik Kashinath"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Robotics_autonomous
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Climate Simulation"
  - "Physical AI"
external_links:
  - name: "Modeling Earth’s Atmosphere with Spherical Fourier Neural Operators"
    url: "https://resources.nvidia.com/en-us-modulus-pathfactory/modeling-earths-atmosphere"
abstract: "Fourier Neural Operators (FNOs) have proven to be an efficient and effective method for resolution-independent operator learning in a broad variety of application areas across scientific machine learning. A key reason for their success is their ability to accurately model long-range dependencies in "
url: "https://research.nvidia.com/publication/2023-06_spherical-fourier-neural-operators-learning-stable-dynamics-sphere"
status: "new"
---

# Spherical Fourier Neural Operators: Learning Stable Dynamics on the Sphere

## 摘要

Fourier Neural Operators (FNOs) have proven to be an efficient and effective method for resolution-independent operator learning in a broad variety of application areas across scientific machine learning. A key reason for their success is their ability to accurately model long-range dependencies in spatio-temporal data by learning global convolutions in a computationally efficient manner. To this end, FNOs rely on the discrete Fourier transform (DFT), however, DFTs cause visual and spectral artifacts as well as pronounced dissipation when learning operators in spherical coordinates by incorrectly assuming flat geometry. To overcome this limitation, we generalize FNOs on the sphere, introducing Spherical FNOs (SFNOs) for learning operators on spherical geometries. We apply SFNOs to forecasting atmo-spheric dynamics, and demonstrate stable autoregressive rollouts for a year of simulated time (1,460 steps), while retaining physically plausible dynamics. The SFNO has important implications for machine learning-based simulation of climate dynamics that could eventually help accelerate our response to climate change.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
