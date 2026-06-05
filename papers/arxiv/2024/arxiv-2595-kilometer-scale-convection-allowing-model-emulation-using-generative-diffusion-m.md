---
id: arxiv-2595
title: "Kilometer-Scale Convection Allowing Model Emulation using Generative Diffusion Modeling"
conference: arXiv 2024
date: 2024-08
authors:
  - name: "Jaideep Pathak"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Noah Brenowitz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dale Durran"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Morteza Mardani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike Pritchard"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yair Cohen"
    affiliation: ""
    is_industry: false
  - name: "Piyush Garg"
    affiliation: ""
    is_industry: false
  - name: "Peter Harrington"
    affiliation: ""
    is_industry: false
  - name: "Shaoming Xu"
    affiliation: ""
    is_industry: false
  - name: "Karthik Kashinath"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Climate Simulation"
  - "Generative AI"
abstract: "Storm-scale convection-allowing models (CAMs) are an important tool for predicting the evolution of thunderstorms and mesoscale convective systems that result in damaging extreme weather. By explicitly resolving convective dynamics within the atmosphere they afford meteorologists the nuance needed t"
url: "https://research.nvidia.com/publication/2024-08_kilometer-scale-convection-allowing-model-emulation-using-generative-diffusion"
status: new
---

# Kilometer-Scale Convection Allowing Model Emulation using Generative Diffusion Modeling

## 摘要

Storm-scale convection-allowing models (CAMs) are an important tool for predicting the evolution of thunderstorms and mesoscale convective systems that result in damaging extreme weather. By explicitly resolving convective dynamics within the atmosphere they afford meteorologists the nuance needed to provide outlook on hazard. Deep learning models have thus far not proven skilful at km-scale atmospheric simulation, despite being competitive at coarser resolution with state-of-the-art global, medium-range weather forecasting. We present a generative diffusion model called StormCast, which emulates the high-resolution rapid refresh (HRRR) model—NOAA’s state-of-the-art 3km operational CAM. StormCast autoregressively predicts 99 state variables at km scale using a 1-hour time step, with dense vertical resolution in the atmospheric boundary layer, conditioned on 26 synoptic variables. We present evidence of successfully learnt km-scale dynamics including competitive 1-6 hour forecast skill for composite radar reflectivity alongside physically realistic convective cluster evolution, moist updrafts, and cold pool morphology. StormCast predictions maintain realistic power spectra for multiple predicted variables across multi-hour forecasts. Together, these results establish the potential for autoregressive ML to emulate CAMs – opening up new km-scale frontiers for regional ML weather prediction and future climate hazard dynamical downscaling.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
