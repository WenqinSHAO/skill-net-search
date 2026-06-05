---
id: arxiv-2576
title: "Directed Graph Generation with Heat Kernels"
conference: arXiv 2025
date: 2025-01
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marc T. Law"
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
  - name: "OpenReview"
    url: "https://openreview.net/forum?id=60Gi1w6hte"
abstract: "Existing work on graph generation has, so far, mainly focused on undirected graphs. In this paper we propose a denoising autoencoder-based generative model that exploits the global structure of directed graphs (also called digraphs) via their Laplacian dynamics and enables one-shot generation. &nbsp"
url: "https://research.nvidia.com/publication/2025-01_directed-graph-generation-heat-kernels"
status: new
---

# Directed Graph Generation with Heat Kernels

## 摘要

Existing work on graph generation has, so far, mainly focused on undirected graphs. In this paper we propose a denoising autoencoder-based generative model that exploits the global structure of directed graphs (also called digraphs) via their Laplacian dynamics and enables one-shot generation. &nbsp;Our noising encoder uses closed-form expressions based on the heat equation to corrupt its digraph input with uniform noise. Our decoder reconstructs the corrupted representation by exploiting the global topological information of the graph included in its random walk Laplacian matrix. Our approach generalizes a special class of exponential kernels over discrete structures, called diffusion kernels or heat kernels, to the non-symmetric case via Reproducing Kernel Banach Spaces (RKBS). This connection with heat kernels provides us with a geometrically motivated algorithm related to Gaussian processes and dimensionality reduction techniques such as Laplacian eigenmaps. It also allows us to interpret and exploit the eigenproperties of the Laplacian matrix. We provide an experimental analysis of our approach on different types of synthetic datasets and show that our model is able to generate directed graphs that follow the distribution of the training dataset even if it is multimodal.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
