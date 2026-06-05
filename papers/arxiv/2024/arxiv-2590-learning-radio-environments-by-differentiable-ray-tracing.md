---
id: arxiv-2590
title: "Learning Radio Environments by Differentiable Ray Tracing"
conference: arXiv 2024
date: 2024-10
authors:
  - name: "Jakob Hoydis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fayçal Aït Aoudia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Merlin Nimier-David"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Florian Euchner"
    affiliation: ""
    is_industry: false
  - name: "Stephan ten Brink"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Interconnect_networking
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Telecommunications"
  - "World Simulation"
abstract: "Ray tracing (RT) is instrumental in 6G research in order to generate spatially-consistent and environment-specific channel impulse responses (CIRs). While acquiring accurate scene geometries is now relatively straightforward, determining material characteristics requires precise calibration using ch"
url: "https://research.nvidia.com/publication/2024-10_learning-radio-environments-differentiable-ray-tracing"
status: new
---

# Learning Radio Environments by Differentiable Ray Tracing

## 摘要

Ray tracing (RT) is instrumental in 6G research in order to generate spatially-consistent and environment-specific channel impulse responses (CIRs). While acquiring accurate scene geometries is now relatively straightforward, determining material characteristics requires precise calibration using channel measurements. We therefore introduce a novel gradient-based calibration method, complemented by differentiable parametrizations of material properties, scattering and antenna patterns. Our method seamlessly integrates with differentiable ray tracers that enable the computation of derivatives of CIRs with respect to these parameters. Essentially, we approach field computation as a large computational graph wherein parameters are trainable akin to weights of a neural network (NN). We have validated our method using both synthetic data and real-world indoor channel measurements, employing a distributed multiple-input multiple-output (MIMO) channel sounder.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
