---
id: arxiv-2935
title: "Neural Networks with Recurrent Generative Feedback"
conference: arXiv 2020
date: 2020-12
authors:
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yujia Huang"
    affiliation: ""
    is_industry: false
  - name: "James Gornet"
    affiliation: ""
    is_industry: false
  - name: "Sihui Dai"
    affiliation: ""
    is_industry: false
  - name: "Tan Nguyen"
    affiliation: ""
    is_industry: false
  - name: "Doris Y. Tsao"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/2007.09200"
  - name: "Code"
    url: "https://github.com/yjhuangcd/CNNF"
  - name: "Talk"
    url: "https://www.youtube.com/watch?v=8N9AF8V52-E&amp;feature=youtu.be"
  - name: "Slides"
    url: "https://chrisding.github.io/publications/NeurIPS20a_Slides.pdf"
  - name: "Blog Post"
    url: "https://yjhuangcd.github.io/blog/2020/neurips_cnnf/"
abstract: "Neural networks are vulnerable to input perturbations such as additive noise and adversarial attacks. In contrast, human perception is much more robust to such perturbations. The Bayesian brain hypothesis states that human brains use an internal generative model to update the posterior beliefs of th"
url: "https://research.nvidia.com/publication/2020-12_neural-networks-recurrent-generative-feedback"
status: new
---

# Neural Networks with Recurrent Generative Feedback

## 摘要

Neural networks are vulnerable to input perturbations such as additive noise and adversarial attacks. In contrast, human perception is much more robust to such perturbations. The Bayesian brain hypothesis states that human brains use an internal generative model to update the posterior beliefs of the sensory input. This mechanism can be interpreted as a form of self-consistency between the maximum a posteriori (MAP) estimation of an internal generative model and the external environment. Inspired by such hypothesis, we enforce self-consistency in neural networks by incorporating generative recurrent feedback. We instantiate this design on convolutional neural networks (CNNs). The proposed framework, termed Convolutional Neural Networks with Feedback (CNN-F), introduces a generative feedback with latent variables to existing CNN architectures, where consistent predictions are made through alternating MAP inference under a Bayesian framework. In the experiments, CNN-F shows considerably improved adversarial robustness over conventional feedforward CNNs on standard benchmarks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
