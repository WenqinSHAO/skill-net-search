---
id: neurips-0012
title: "Molecule Generation with Fragment Retrieval Augmentation"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Seul Lee"
    affiliation: ""
    is_industry: false
  - name: "Srimukh Prasad Veccham"
    affiliation: ""
    is_industry: false
  - name: "Meng Liu"
    affiliation: ""
    is_industry: false
  - name: "Danny Reidenbach"
    affiliation: ""
    is_industry: false
  - name: "Saee Paliwal"
    affiliation: ""
    is_industry: false
  - name: "Weili Nie"
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
    url: "https://arxiv.org/abs/2411.12078"
abstract: "Fragment-based drug discovery, in which molecular fragments are assembled into new molecules with desirable biochemical properties, has achieved great success. However, many fragment-based molecule generation methods show limited exploration beyond the existing fragments in the database as they only"
url: "https://research.nvidia.com/publication/2024-12_molecule-generation-fragment-retrieval-augmentation"
status: new
---

# Molecule Generation with Fragment Retrieval Augmentation

## 摘要

Fragment-based drug discovery, in which molecular fragments are assembled into new molecules with desirable biochemical properties, has achieved great success. However, many fragment-based molecule generation methods show limited exploration beyond the existing fragments in the database as they only reassemble or slightly modify the given ones. To tackle this problem, we propose a new fragment-based molecule generation framework with retrieval augmentation, namely Fragment Retrieval-Augmented Generation (f-RAG). f-RAG is based on a pre-trained molecular generative model that proposes additional fragments from input fragments to complete and generate a new molecule. Given a fragment vocabulary, f-RAG retrieves two types of fragments: (1) hard fragments, which serve as building blocks that will be explicitly included in the newly generated molecule, and (2) soft fragments, which serve as reference to guide the generation of new fragments through a trainable fragment injection module. To extrapolate beyond the existing fragments, f-RAG updates the fragment vocabulary with generated fragments via an iterative refinement process which is further enhanced with post-hoc genetic fragment modification. f-RAG can achieve an improved exploration-exploitation trade-off by maintaining a pool of fragments and expanding it with novel and high-quality fragments through a strong generative prior.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
