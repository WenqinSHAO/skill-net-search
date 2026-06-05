---
id: arxiv-2538
title: "Huge ensembles–Part 1: Design of ensemble weather forecasts using spherical Fourier neural operators"
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
  - name: "Joshua Elms"
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
  - Robotics_autonomous
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
  - "Physical AI"
abstract: "Simulating low-likelihood high-impact extreme weather events in a warming world is a significant and challenging task for current ensemble forecasting systems. While these systems presently use up to 100 members, larger ensembles could enrich the sampling of internal variability. They may capture th"
url: "https://research.nvidia.com/publication/2025-09_huge-ensembles-part-1-design-ensemble-weather-forecasts-using-spherical-fourier"
status: new
---

# Huge ensembles–Part 1: Design of ensemble weather forecasts using spherical Fourier neural operators

## 摘要

Simulating low-likelihood high-impact extreme weather events in a warming world is a significant and challenging task for current ensemble forecasting systems. While these systems presently use up to 100 members, larger ensembles could enrich the sampling of internal variability. They may capture the long tails associated with climate hazards better than traditional ensemble sizes. Due to computational constraints, it is infeasible to generate huge ensembles (comprised of 1000–10 000 members) with traditional, physics-based numerical models. In this two-part paper, we replace traditional numerical simulations with machine learning (ML) to generate hindcasts of huge ensembles. In Part&nbsp;1, we construct an ensemble weather forecasting system based on spherical Fourier neural operators (SFNOs), and we discuss important design decisions for constructing such an ensemble. The ensemble represents model uncertainty through perturbed-parameter techniques, and it represents initial condition uncertainty through bred vectors, which sample the fastest-growing modes of the forecast. Using the European Centre for Medium-Range Weather Forecasts Integrated Forecasting System (IFS) as a baseline, we develop an evaluation pipeline composed of mean, spectral, and extreme diagnostics. With large-scale, distributed SFNOs with 1.1&nbsp;billion learned parameters, we achieve calibrated probabilistic forecasts. As the trajectories of the individual members diverge, the ML ensemble mean spectra degrade with lead time, consistent with physical expectations. However, the individual ensemble members' spectra stay constant with lead time. Therefore, these members simulate realistic weather states during the rollout, and the ML ensemble passes a crucial spectral test in the literature. The IFS and ML ensembles have similar extreme forecast indices, and we show that the ML extreme weather forecasts are reliable and discriminating. These diagnostics ensure that the ensemble can reliably simulate the time evolution of the atmosphere, including low-likelihood high-impact extremes. In Part&nbsp;2, we generate a huge ensemble initialized each day in summer 2023, and we characterize the simulations of extremes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
