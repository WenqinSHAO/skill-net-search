---
id: iclr-0019
title: "ProtComposer: Compositional Protein Structure Generation with 3D Ellipsoids"
conference: ICLR 2025
date: 2025-01
authors:
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hannes Stark"
    affiliation: ""
    is_industry: false
  - name: "Bowen Jing"
    affiliation: ""
    is_industry: false
  - name: "Jason Yim"
    affiliation: ""
    is_industry: false
  - name: "Tommi Jaakkola"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2503.05025"
abstract: "We develop ProtComposer to generate protein structures conditioned on spatial protein layouts that are specified via a set of 3D ellipsoids capturing substructure shapes and semantics. At inference time, we condition on ellipsoids that are hand-constructed, extracted from existing proteins, or from "
url: "https://research.nvidia.com/publication/2025-01_protcomposer-compositional-protein-structure-generation-3d-ellipsoids"
status: new
---

# ProtComposer: Compositional Protein Structure Generation with 3D Ellipsoids

## 摘要

We develop ProtComposer to generate protein structures conditioned on spatial protein layouts that are specified via a set of 3D ellipsoids capturing substructure shapes and semantics. At inference time, we condition on ellipsoids that are hand-constructed, extracted from existing proteins, or from a statistical model, with each option unlocking new capabilities. Hand-specifying ellipsoids enables users to control the location, size, orientation, secondary structure, and approximate shape of protein substructures. Conditioning on ellipsoids of existing proteins enables redesigning their substructure’s connectivity or editing substructure properties. By conditioning on novel and diverse ellipsoid layouts from a simple statistical model, we improve protein generation with expanded Pareto frontiers between designability, novelty, and diversity. Further, this enables sampling designable proteins with a helix-fraction that matches PDB proteins, unlike existing generative models that commonly oversample conceptually simple helix bundles. Code is available at https://github.com/NVlabs/protcomposer.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
