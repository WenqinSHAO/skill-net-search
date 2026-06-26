---
id: "rss-0005"
title: "Real-Time Anomaly Detection and Reactive Planning with Large Language Models"
conference: "RSS 2024"
date: "2024-07"
authors:
  - name: "Rohan Sinha"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Amine Elhafsi"
    affiliation: "Stanford Univeristy"
    is_industry: false
  - name: "Christopher Agia"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Matthew Foutter"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Edward Schmerling"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Robotics"
external_links:
  - name: "Arxiv Paper"
    url: "https://arxiv.org/abs/2407.08735"
abstract: "Foundation models, e.g., large language models (LLMs), trained on internet-scale data possess zero-shot generalization capabilities that make them a promising technology towards detecting and mitigating out-of-distribution failure modes of robotic systems. Fully realizing this promise, however, pose"
url: "https://research.nvidia.com/publication/2024-07_real-time-anomaly-detection-and-reactive-planning-large-language-models"
status: "new"
---

# Real-Time Anomaly Detection and Reactive Planning with Large Language Models

## 摘要

Foundation models, e.g., large language models (LLMs), trained on internet-scale data possess zero-shot generalization capabilities that make them a promising technology towards detecting and mitigating out-of-distribution failure modes of robotic systems. Fully realizing this promise, however, poses two challenges: (i) mitigating the considerable computational expense of these models such that they may be applied online, and (ii) incorporating their judgement regarding potential anomalies into a safe control framework. In this work, we present a two-stage reasoning framework: First is a fast binary anomaly classifier that analyzes observations in an LLM embedding space, which may then trigger a slower fallback selection stage that utilizes the reasoning capabilities of generative LLMs. These stages correspond to branch points in a model predictive control strategy that maintains the joint feasibility of continuing along various fallback plans to account for the slow reasoner's latency as soon as an anomaly is detected, thus ensuring safety. We show that our fast anomaly classifier outperforms autoregressive reasoning with state-of-the-art GPT models, even when instantiated with relatively small language models. This enables our runtime monitor to improve the trustworthiness of dynamic robotic systems, such as quadrotors or autonomous vehicles, under resource and time constraints. Videos illustrating our approach in both simulation and real-world experiments are available on this project page: this https URL.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
