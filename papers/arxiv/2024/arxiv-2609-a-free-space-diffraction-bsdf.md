---
id: arxiv-2609
title: "A Free-Space Diffraction BSDF"
conference: arXiv 2024
date: 2024-07
authors:
  - name: "Ravi Ramamoorthi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Benedikt Bitterli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d&#039;Eon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matt Pharr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shlomi Steinberg"
    affiliation: ""
    is_industry: false
  - name: "Arshiya Mollazainali"
    affiliation: ""
    is_industry: false
topics:
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
external_links:
  - name: "Paper"
    url: "https://ssteinberg.xyz/2024/04/05/free_space_diffractions_bsdf/"
abstract: "Free-space diffractions are an optical phenomenon where light appears to “bend” around the geometric edges and corners of scene objects. In this paper we present an efficient method to simulate such effects. We derive an edge-based formulation of Fraunhofer diffraction, which is well suited to the c"
url: "https://research.nvidia.com/publication/2024-07_free-space-diffraction-bsdf"
status: new
---

# A Free-Space Diffraction BSDF

## 摘要

Free-space diffractions are an optical phenomenon where light appears to “bend” around the geometric edges and corners of scene objects. In this paper we present an efficient method to simulate such effects. We derive an edge-based formulation of Fraunhofer diffraction, which is well suited to the common (triangular) geometric meshes used in computer graphics. Our method dynamically constructs a free-space diffraction BSDF by considering the geometry around the intersection point of a ray of light with an object, and we present an importance sampling strategy for these BSDFs. Our method is unique in requiring only ray tracing to produce free-space diffractions, works with general meshes, requires no geometry preprocessing, and is designed to work with path tracers with a linear rendering equation. We show that we are able to reproduce accurate diffraction lobes, and, in contrast to any existing method, are able to handle complex, real-world geometry. This work serves to connect free-space diffractions to the efficient path tracing tools from computer graphics.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
