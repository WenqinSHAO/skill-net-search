---
id: "siggraph-0006"
title: "Generative Detail Enhancement for Physically Based Materials"
conference: "SIGGRAPH 2025"
date: "2025-07"
authors:
  - name: "Saeed Hadadan"
    affiliation: "University of Maryland, College Park and NVIDIA"
    is_industry: true
  - name: "Benedikt Bitterli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tizian Zeltner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jacob Munkberg"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jon Hasselgren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bart Wronski"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matthias Zwicker"
    affiliation: "University of Maryland, College Park"
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "Project page"
    url: "https://generative-detail.github.io/"
abstract: "We present a tool for enhancing the detail of physically based materials using an off-the-shelf diffusion model and inverse rendering. Our goal is to enhance the visual fidelity of materials with detail that is often tedious to author, by adding signs of wear, aging, weathering, etc. As these appear"
url: "https://research.nvidia.com/publication/2025-07_generative-detail-enhancement-physically-based-materials"
status: "new"
---

# Generative Detail Enhancement for Physically Based Materials

## 摘要

We present a tool for enhancing the detail of physically based materials using an off-the-shelf diffusion model and inverse rendering. Our goal is to enhance the visual fidelity of materials with detail that is often tedious to author, by adding signs of wear, aging, weathering, etc. As these appearance details are often rooted in real-world processes, we leverage a generative image model trained on a large dataset of natural images with corresponding visuals in context. Starting with a given geometry, UV mapping, and basic appearance, we render multiple views of the object. We use these views, together with an appearance-defining text prompt, to condition a diffusion model. The details it generates are then backpropagated from the enhanced images to the material parameters via inverse differentiable rendering. For inverse rendering to be successful, the generated appearance has to be consistent across all the images. We propose two priors to address the multi-view consistency of the diffusion model. First, we ensure that the initial noise that seeds the diffusion process is itself consistent across views by integrating it from a view-independent UV space. Second, we enforce geometric consistency by biasing the attention mechanism via a projective constraint so that pixels attend strongly to their corresponding pixel locations in other views. Our approach does not require any training or finetuning of the diffusion model, is agnostic of the material model used, and the enhanced material properties, i.e., 2D PBR textures, can be further edited by artists.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
