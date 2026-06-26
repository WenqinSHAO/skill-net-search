---
id: "arxiv-2558"
title: "Sionna RT: Technical Report"
conference: "arXiv 2025"
date: "2025-04"
authors:
  - name: "Fayçal Aït Aoudia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jakob Hoydis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Merlin Nimier-David"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
  - Interconnect_networking
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Telecommunications"
  - "World Simulation"
external_links:
  - name: "Webpage"
    url: "https://nvlabs.github.io/sionna/rt/tech-report/index.html"
abstract: "Sionna is an open-source, GPU-accelerated library that, as of version 0.14, incorporates a ray tracer for simulating radio wave propagation. A unique feature of Sionna RT is differentiability, enabling the calculation of gradients for the channel impulse responses (CIRs), radio maps, and other relat"
url: "https://research.nvidia.com/publication/2025-04_sionna-rt-technical-report"
status: "new"
---

# Sionna RT: Technical Report

## 摘要

Sionna is an open-source, GPU-accelerated library that, as of version 0.14, incorporates a ray tracer for simulating radio wave propagation. A unique feature of Sionna RT is differentiability, enabling the calculation of gradients for the channel impulse responses (CIRs), radio maps, and other related metrics with respect to system and environmental parameters, such as material properties, antenna patterns, and array geometries. The release of Sionna 1.0 provides a complete overhaul of the ray tracer, significantly improving its speed, memory efficiency, and extensibility. This document details the algorithms employed by Sionna RT to simulate radio wave propagation efficiently, while also addressing their current limitations. Given that the computation of CIRs and radio maps requires distinct algorithms, these are detailed in separate sections. For CIRs, Sionna RT integrates shooting and bouncing of rays (SBR) with the image method and uses a hashing-based mechanism to efficiently eliminate duplicate paths. Radio maps are computed using a purely SBR-based approach.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
