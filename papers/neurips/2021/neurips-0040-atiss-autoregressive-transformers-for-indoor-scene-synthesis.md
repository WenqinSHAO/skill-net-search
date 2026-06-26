---
id: "neurips-0040"
title: "ATISS: Autoregressive Transformers for Indoor Scene Synthesis"
conference: "NeurIPS 2021"
date: "2021-12"
authors:
  - name: "Despoina Paschalidou"
    affiliation: "Autonomous Vision Group MPI for Intelligent Systems Tübingen, Max Planck ETH Center for Learning Systems, NVIDIA"
    is_industry: true
  - name: "Amlan Kar"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Maria Shugrina"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andreas Geiger"
    affiliation: "Autonomous Vision Group MPI for Intelligent Systems Tübingen, University of Tübingen, Max Planck ETH Center for Learning System"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/toronto-ai/ATISS/"
abstract: "The ability to synthesize realistic and diverse indoor furniture layouts automatically or based on partial input, unlocks many applications, from better interactive 3D tools to data synthesis for training and simulation. In this paper, we present ATISS, a novel autoregressive transformer architectur"
url: "https://research.nvidia.com/publication/2021-12_atiss-autoregressive-transformers-indoor-scene-synthesis"
status: "new"
---

# ATISS: Autoregressive Transformers for Indoor Scene Synthesis

## 摘要

The ability to synthesize realistic and diverse indoor furniture layouts automatically or based on partial input, unlocks many applications, from better interactive 3D tools to data synthesis for training and simulation. In this paper, we present ATISS, a novel autoregressive transformer architecture for creating diverse and plausible synthetic indoor environments, given only the room type and its floor plan. In contrast to prior work, which poses scene synthesis as sequence generation, our model generates rooms as unordered sets of objects. We argue that this formulation is more natural, as it makes ATISS generally useful beyond fully automatic room layout synthesis. For example, the same trained model can be used in interactive applications for general scene completion, partial room re-arrangement with any objects specified by the user, as well as object suggestions for any partial room. To enable this, our model leverages the permutation equivariance of the transformer when conditioning on the partial scene, and is trained to be permutation-invariant across object orderings. Our model is trained end-to-end as an autoregressive generative model using only labeled 3D bounding boxes as supervision. Evaluations on four room types in the 3D-FRONT dataset demonstrate that our model consistently generates plausible room layouts that are more realistic than existing methods. In addition, it has fewer parameters, is simpler to implement and train and runs up to 8 times faster than existing methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
