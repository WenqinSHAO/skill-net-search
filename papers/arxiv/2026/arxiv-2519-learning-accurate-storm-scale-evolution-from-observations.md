---
id: "arxiv-2519"
title: "Learning Accurate Storm-Scale Evolution from Observations"
conference: "arXiv 2026"
date: "2026-01"
authors:
  - name: "Jaideep Pathak"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mohammad Shoaib Abbas"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Peter Harrington"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zeyuan Hu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Noah Brenowitz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Suman Ravuri"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alberto Carpentieri"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jussi Leinonen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Corey Adams"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oliver Hennigh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nicholas Geneva"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dale Durran"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike Pritchard"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
abstract: "Accurate short-term prediction of clouds and precipitation is critical for severe weather warnings,aviation safety, and renewable energy operations. Forecasts at this timescale are provided bynumerical weather models and extrapolation methods, both of which have limitations. Mesoscalenumerical weath"
url: "https://research.nvidia.com/publication/2026-01%5Flearning-accurate-storm-scale-evolution-observations"
status: "new"
---

# Learning Accurate Storm-Scale Evolution from Observations

## 摘要

Accurate short-term prediction of clouds and precipitation is critical for severe weather warnings,aviation safety, and renewable energy operations. Forecasts at this timescale are provided bynumerical weather models and extrapolation methods, both of which have limitations. Mesoscalenumerical weather prediction models provide skillful forecasts at these scales but require significantmodeling expertise and computational infrastructure, which limits their accessibility.Extrapolation-based methods are computationally lightweight but degrade rapidly beyond 1-2hours. This presents an opportunity for data-driven forecasting directly from observations usinggeostationary satellites and ground-based radar, which provide high-frequency, high-resolution observationsthat capture mesoscale atmospheric evolution. We introduce Stormscope, a family oftransformer-based generative diffusion models trained on high-resolution, multi-band geostationarysatellite imagery and ground-based weather radar over the continental United States. Stormscopeproduces forecasts at a temporal resolution of 10 min and 6km spatial resolution, whichare competitive with state-of-the-art mesoscale NWP models for lead times up to 6 hours. Itsgenerative architecture enables large ensemble forecasts of explicit mesoscale dynamics for robustuncertainty quantification. Evaluated against extrapolation methods and operational mesoscaleNWP models, Stormscope achieves leading performance on standard deterministic and probabilisticverification metrics across forecast horizons from 1 to 6 hours. By operating in observationspace, Stormscope establishes a new paradigm for multi-modal AI-driven nowcasting with directapplicability to operational forecasting workflows. The approach is extensible, with demonstratedcomputational scaling to larger domains and higher resolutions. As Stormscope relies on globallyavailable satellite observations (and radar where available), it offers a pathway to extend skillfulmesoscale forecasting to oceanic regions and countries without strong operational mesoscalemodeling programs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
