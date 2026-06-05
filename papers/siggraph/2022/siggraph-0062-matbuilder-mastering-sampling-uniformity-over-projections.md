---
id: siggraph-0062
title: "MatBuilder: Mastering Sampling Uniformity Over Projections"
conference: SIGGRAPH 2022
date: 2022-05
authors:
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Loïs Paulin"
    affiliation: ""
    is_industry: false
  - name: "Nicolas Bonneel"
    affiliation: ""
    is_industry: false
  - name: "David Coeurjolly"
    affiliation: ""
    is_industry: false
  - name: "Jean-Claude Iehl"
    affiliation: ""
    is_industry: false
  - name: "Victor Ostromoukhov"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Project Page"
    url: "https://projet.liris.cnrs.fr/matbuilder/"
abstract: "Many applications ranging from quasi-Monte Carlo integration over optimal control to neural networks benefit from high-dimensional, highly uniform samples.&nbsp;In the case of computer graphics,&nbsp; and more particularly in rendering, despite the need for uniformity, several sub-problems expose a "
url: "https://research.nvidia.com/publication/2022-05_matbuilder-mastering-sampling-uniformity-over-projections"
status: new
---

# MatBuilder: Mastering Sampling Uniformity Over Projections

## 摘要

Many applications ranging from quasi-Monte Carlo integration over optimal control to neural networks benefit from high-dimensional, highly uniform samples.&nbsp;In the case of computer graphics,&nbsp; and more particularly in rendering, despite the need for uniformity, several sub-problems expose a low-dimensional structure.&nbsp;In this context, mastering sampling uniformity over projections while preserving high-dimensional uniformity has been intrinsically challenging.&nbsp;This difficulty may explain the relatively small number of mathematical constructions for such samplers.&nbsp;We propose a novel approach by showing that uniformity constraints can be expressed as an integer linear program that results in a sampler with the desired properties.&nbsp;As it turns out, complex constraints are easy to describe by means of stratification and sequence properties of digital nets.&nbsp;Formalized using generator matrix determinants, our new MatBuilder software solves the set of constraints by iterating the linear integer program solver in a greedy fashion to compute a problem-specific set of generator matrices that can be used as a drop-in replacement in the popular digital net samplers.&nbsp;The samplers created by MatBuilder achieve the uniformity of classic low discrepancy sequences.&nbsp;More importantly, we demonstrate the benefit of the unprecedented versatility of our constraint approach with respect to low-dimensional problem structure for several applications.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
