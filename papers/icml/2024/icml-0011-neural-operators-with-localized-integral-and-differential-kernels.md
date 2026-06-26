---
id: "icml-0011"
title: "Neural operators with localized integral and differential kernels"
conference: "ICML 2024"
date: "2024-07"
authors:
  - name: "Miguel Liu-Schiaffini"
    affiliation: "Caltech"
    is_industry: false
  - name: "Julius Berner"
    affiliation: "Caltech"
    is_industry: false
  - name: "Boris Bonev"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thorsten Kurth"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kamyar Azizzadenesheli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "Caltech"
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Robotics_autonomous
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Climate Simulation"
  - "Physical AI"
abstract: "Neural operators learn mappings between function spaces, which is practical for learning solution operators of PDEs and other scientific modeling applications. Among them, the Fourier neural operator (FNO) is a popular architecture that performs global convolutions in the Fourier space. However, suc"
url: "https://research.nvidia.com/publication/2024-07_neural-operators-localized-integral-and-differential-kernels"
status: "new"
---

# Neural operators with localized integral and differential kernels

## 摘要

Neural operators learn mappings between function spaces, which is practical for learning solution operators of PDEs and other scientific modeling applications. Among them, the Fourier neural operator (FNO) is a popular architecture that performs global convolutions in the Fourier space. However, such global operations are often prone to over-smoothing and may fail to capture local details. In contrast, convolutional neural networks (CNN) can capture local features but are limited to training and inference at a single resolution. In this work, we present a principled approach to operator learning that can capture local features under two frameworks by learning differential operators and integral operators with locally supported kernels. Specifically, inspired by stencil methods, we prove that we obtain differential operators under an appropriate scaling of the kernel values of CNNs. To obtain local integral operators, we utilize suitable basis representations for the kernels based on discrete-continuous convolutions. Both these approaches preserve the properties of operator learning and, hence, the ability to predict at any resolution. Adding our layers to FNOs significantly improves their performance, reducing the relative L2-error by 34-72% in our experiments, which include a turbulent 2D Navier-Stokes and the spherical shallow water equations.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
