---
id: "neurips-0002"
title: "Elucidated Rolling Diffusion Models for Probabilistic Weather Forecasting"
conference: "NeurIPS 2025"
date: "2025-12"
authors:
  - name: "Salva Rühling Cachay"
    affiliation: "UC San Diego"
    is_industry: false
  - name: "Miika Aittala"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Noah Brenowitz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Morteza Mardani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rose Yu"
    affiliation: "UC San Diego"
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Climate Simulation"
  - "Generative AI"
abstract: "Diffusion models are a powerful tool for probabilistic forecasting, yet most applications in high-dimensional chaotic systems predict future snapshots one-by-one. This common approach struggles to model complex temporal dependencies and fails to explicitly account for the progressive growth of uncer"
url: "https://research.nvidia.com/publication/2025-12_elucidated-rolling-diffusion-models-probabilistic-weather-forecasting"
status: "new"
---

# Elucidated Rolling Diffusion Models for Probabilistic Weather Forecasting

## 摘要

Diffusion models are a powerful tool for probabilistic forecasting, yet most applications in high-dimensional chaotic systems predict future snapshots one-by-one. This common approach struggles to model complex temporal dependencies and fails to explicitly account for the progressive growth of uncertainty inherent to such systems. While rolling diffusion frameworks, which apply increasing noise to forecasts at longer lead times, have been proposed to address this, their integration with state-of-the-art, high-fidelity diffusion techniques remains a significant challenge. We tackle this problem by introducing Elucidated Rolling Diffusion Models (ERDM), the first framework to successfully unify a rolling forecast structure with the principled, performant design of Elucidated Diffusion Models (EDM). To do this, we adapt the core EDM components-its noise schedule, network preconditioning, and Heun sampler-to the rolling forecast setting. The success of this integration is driven by three key contributions: (i) a novel loss weighting scheme that focuses model capacity on the mid-range forecast horizons where determinism gives way to stochasticity; (ii) an efficient initialization strategy using a pre-trained EDM for the initial window; and (iii) a bespoke hybrid sequence architecture for robust spatiotemporal feature extraction under progressive denoising. On 2D Navier-Stokes simulations and ERA5 global weather forecasting at 1.5^\circ resolution, ERDM consistently outperforms key diffusion-based baselines, including conditional autoregressive EDM. ERDM offers a flexible and powerful general framework for tackling diffusion-based sequence generation problems where modeling escalating uncertainty is paramount. Code is available at https://github.com/salvaRC/erdm.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
