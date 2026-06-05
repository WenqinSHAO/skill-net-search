---
id: iclr-0004
title: "La-Proteina: Atomistic Protein Generation via Partially Latent Flow Matching"
conference: ICLR 2026
date: 2026-01
authors:
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kieran Didi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhonglin Cao"
    affiliation: ""
    is_industry: false
  - name: "Danny Reidenbach"
    affiliation: ""
    is_industry: false
  - name: "Zuobai Zhang"
    affiliation: ""
    is_industry: false
  - name: "Christian Dallago"
    affiliation: ""
    is_industry: false
  - name: "Emine Kucukbenli"
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
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/genair/la-proteina/"
abstract: "Recently, many generative models for de novo protein structure design have emerged. Yet, only few tackle the difficult task of directly generating fully atomistic structures jointly with the underlying amino acid sequence. This is challenging, for instance, because the model must reason over side ch"
url: "https://research.nvidia.com/publication/2026-01%5Fla-proteina-atomistic-protein-generation-partially-latent-flow-matching"
status: new
---

# La-Proteina: Atomistic Protein Generation via Partially Latent Flow Matching

## 摘要

Recently, many generative models for de novo protein structure design have emerged. Yet, only few tackle the difficult task of directly generating fully atomistic structures jointly with the underlying amino acid sequence. This is challenging, for instance, because the model must reason over side chains that change in length during generation. We introduce La-Proteina for atomistic protein design based on a novel partially latent protein representation: coarse backbone structure is modeled explicitly, while sequence and atomistic details are captured via per-residue latent variables of fixed dimensionality, thereby effectively side-stepping challenges of explicit side-chain representations. Flow matching in this partially latent space then models the joint distribution over sequences and full-atom structures. La-Proteina achieves state-of-the-art performance on multiple generation benchmarks, including all-atom co-designability, diversity, and structural validity, as confirmed through detailed structural analyses and evaluations. Notably, La-Proteina also surpasses previous models in atomistic motif scaffolding performance, unlocking critical atomistic structure-conditioned protein design tasks. Moreover, La-Proteina is able to generate co-designable proteins of up to 800 residues, a regime where most baselines collapse and fail to produce valid samples, demonstrating La-Proteina's scalability and robustness.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
