---
id: "icml-0016"
title: "Equivariant Architectures for Learning in Deep Weight Spaces"
conference: "ICML 2023"
date: "2023-03"
authors:
  - name: "Aviv Navon"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Aviv Shamsian"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Idan Achituve"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Ethan Fetaya"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Project page"
    url: "https://avivnavon.github.io/DWSNets/"
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2301.12780"
abstract: "Designing machine learning architectures for processing neural networks in their raw weight matrix form is a newly introduced research direction. Unfortunately, the unique symmetry structure of deep weight spaces makes this design very challenging. If successful, such architectures would be capable "
url: "https://research.nvidia.com/publication/2023-03_equivariant-architectures-learning-deep-weight-spaces"
status: "new"
---

# Equivariant Architectures for Learning in Deep Weight Spaces

## 摘要

Designing machine learning architectures for processing neural networks in their raw weight matrix form is a newly introduced research direction. Unfortunately, the unique symmetry structure of deep weight spaces makes this design very challenging. If successful, such architectures would be capable of performing a wide range of intriguing tasks, from adapting a pre-trained network to a new domain to editing objects represented as functions (INRs or NeRFs). As a first step towards this goal, we present here a novel network architecture for learning in deep weight spaces. It takes as input a concatenation of weights and biases of a pre-trained MLP and processes it using a composition of layers that are equivariant to the natural permutation symmetry of the MLP’s weights: Changing the order of neurons in intermediate layers of the MLP does not affect the function it represents. We provide a full characterization of all affine equivariant and invariant layers for these symmetries and show how these layers can be implemented using three basic operations: pooling, broadcasting, and fully connected layers applied to the input in an appropriate manner. We demonstrate the effectiveness of our architecture and its advantages over natural baselines in a variety of learning tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
