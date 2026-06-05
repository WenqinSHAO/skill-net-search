---
id: iclr-0026
title: "Graph Metanetworks for Processing Diverse Neural Architectures"
conference: ICLR 2023
date: 2023-12
authors:
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Derek Lim"
    affiliation: ""
    is_industry: false
  - name: "Marc T. Law"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Lorraine"
    affiliation: ""
    is_industry: false
  - name: "James Lucas"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2312.04501"
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/GMN/"
abstract: "Neural networks efficiently encode learned information within their parameters. Consequently, many tasks can be unified by treating neural networks themselves as input data. When doing so, recent studies demonstrated the importance of accounting for the symmetries and geometry of parameter spaces. H"
url: "https://research.nvidia.com/publication/2023-12_graph-metanetworks-processing-diverse-neural-architectures"
status: new
---

# Graph Metanetworks for Processing Diverse Neural Architectures

## 摘要

Neural networks efficiently encode learned information within their parameters. Consequently, many tasks can be unified by treating neural networks themselves as input data. When doing so, recent studies demonstrated the importance of accounting for the symmetries and geometry of parameter spaces. However, those works developed architectures tailored to specific networks such as MLPs and CNNs without normalization layers, and generalizing such architectures to other types of networks can be challenging. In this work, we overcome these challenges by building new metanetworks - neural networks that take weights from other neural networks as input. Put simply, we carefully build graphs representing the input neural networks and process the graphs using graph neural networks. Our approach, Graph Metanetworks (GMNs), generalizes to neural architectures where competing methods struggle, such as multi-head attention layers, normalization layers, convolutional layers, ResNet blocks, and group-equivariant linear layers. We prove that GMNs are expressive and equivariant to parameter permutation symmetries that leave the input neural network functions unchanged. We validate the effectiveness of our method on several metanetwork tasks over diverse neural network architectures.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
