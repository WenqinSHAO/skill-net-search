---
id: "arxiv-2770"
title: "Learning A Continuous and Reconstructible Latent Space for Hardware Accelerator Design"
conference: "arXiv 2022"
date: "2022-05"
authors:
  - name: "Qijing Jenny Huang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Charles Hong"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "John Wawrzynek"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "Mahesh Subedar"
    affiliation: "Intel Labs"
    is_industry: true
  - name: "Yakun Sophia Shao"
    affiliation: "UC Berkeley"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9804604"
abstract: "The hardware design space is high-dimensional and discrete. Systematic and efficient exploration of this space has been a significant challenge. Central to this problem is the intractable search complexity that grows exponentially with the design choices and the discrete nature of the search space. "
url: "https://research.nvidia.com/publication/2022-05_learning-continuous-and-reconstructible-latent-space-hardware-accelerator"
status: "new"
---

# Learning A Continuous and Reconstructible Latent Space for Hardware Accelerator Design

## 摘要

The hardware design space is high-dimensional and discrete. Systematic and efficient exploration of this space has been a significant challenge. Central to this problem is the intractable search complexity that grows exponentially with the design choices and the discrete nature of the search space. This work investigates the feasibility of learning a meaningful low-dimensional continuous representation for hardware designs to reduce such complexity and facilitate the search process. We devise a variational autoencoder (VAE)-based design space exploration framework called VAESA, to encode the hardware design space in a compact and continuous representation. We show that black-box and gradient-based design space exploration algorithms can be applied to the latent space, and design points optimized in the latent space can be reconstructed to high-performance realistic hardware designs. Our experiments show that performing the design space search on the latent space consistently leads to the optimal design point under a fixed number of samples. In addition, the latent space can improve the sample efficiency of the original algorithm by 6.8× and can discover hardware designs that are up to 5% more efficient than the optimal design searched directly in the high-dimensional input space.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
