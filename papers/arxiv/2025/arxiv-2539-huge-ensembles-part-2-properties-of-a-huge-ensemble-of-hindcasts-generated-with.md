---
id: arxiv-2539
title: "Huge ensembles – Part 2: Properties of a huge ensemble of hindcasts generated with spherical Fourier neural operators"
conference: arXiv 2025
date: 2025-09
authors:
  - name: "Boris Bonev"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Noah Brenowitz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike Pritchard"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ankur Mahesh"
    affiliation: ""
    is_industry: false
  - name: "William D. Collins"
    affiliation: ""
    is_industry: false
  - name: "Yair Cohen"
    affiliation: ""
    is_industry: false
  - name: "Peter Harrington"
    affiliation: ""
    is_industry: false
  - name: "Karthik Kashinath"
    affiliation: ""
    is_industry: false
  - name: "Thorsten Kurth"
    affiliation: ""
    is_industry: false
  - name: "Joshua North"
    affiliation: ""
    is_industry: false
  - name: "Travis O'Brian"
    affiliation: ""
    is_industry: false
  - name: "David Pruitt"
    affiliation: ""
    is_industry: false
  - name: "Mark Risser"
    affiliation: ""
    is_industry: false
  - name: "Shashank Subramanian"
    affiliation: ""
    is_industry: false
  - name: "Jared Willard"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Climate Simulation"
  - "High Performance Computing"
external_links:
  - name: "GMD Publication"
    url: "https://gmd.copernicus.org/articles/18/5605/2025/"
abstract: "In Part&nbsp;1, we created an ensemble based on spherical Fourier neural operators. As initial condition perturbations, we used bred vectors, and as model perturbations, we used multiple checkpoints trained independently from scratch. Based on diagnostics that assess the ensemble's physical fidelity"
url: "https://research.nvidia.com/publication/2025-09_huge-ensembles-part-2-properties-huge-ensemble-hindcasts-generated-spherical"
status: new
---

# Huge ensembles – Part 2: Properties of a huge ensemble of hindcasts generated with spherical Fourier neural operators

## 摘要

In Part&nbsp;1, we created an ensemble based on spherical Fourier neural operators. As initial condition perturbations, we used bred vectors, and as model perturbations, we used multiple checkpoints trained independently from scratch. Based on diagnostics that assess the ensemble's physical fidelity, our ensemble has comparable performance to operational weather forecasting systems. However, it requires orders-of-magnitude fewer computational resources. Here in Part 2, we generate a huge ensemble (HENS), with 7424 members initialized each day of summer 2023. We enumerate the technical requirements for running huge ensembles at this scale. HENS precisely samples the tails of the forecast distribution and presents a detailed sampling of internal variability. HENS has two primary applications: (1)&nbsp;as a large dataset with which to study the statistics and drivers of extreme weather and (2)&nbsp;as a weather forecasting system. For extreme climate statistics, HENS samples events 4σ away from the ensemble mean. At each grid cell, HENS increases the skill of the most accurate ensemble member and enhances coverage of possible future trajectories. As a weather forecasting model, HENS issues extreme weather forecasts with better uncertainty quantification. It also reduces the probability of outlier events, in which the verification value lies outside the ensemble forecast distribution.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
