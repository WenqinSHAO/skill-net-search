---
id: "arxiv-2843"
title: "Known unknowns: Learning novel concepts using exploratory reasoning-by-elimination"
conference: "arXiv 2021"
date: "2021-07"
authors:
  - name: "Harsh Agrawal"
    affiliation: "Georgia Tech"
    is_industry: false
  - name: "Eli Meirom"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Applied_perception
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "paper"
    url: "https://proceedings.mlr.press/v161/agrawal21a.html"
abstract: "People can learn new visual concepts without any samples, from information given by language or by deductive reasoning. For instance, people can use&nbsp;elimination&nbsp;to infer the meaning of novel labels from their context. While recognizing novel concepts was intensively studied in zero-shot le"
url: "https://research.nvidia.com/publication/2021-07_known-unknowns-learning-novel-concepts-using-exploratory-reasoning-elimination"
status: "new"
---

# Known unknowns: Learning novel concepts using exploratory reasoning-by-elimination

## 摘要

People can learn new visual concepts without any samples, from information given by language or by deductive reasoning. For instance, people can use&nbsp;elimination&nbsp;to infer the meaning of novel labels from their context. While recognizing novel concepts was intensively studied in zero-shot learning with semantic descriptions, training models to learn by elimination is much less studied. Here we describe the first approach to train an agent to reason-by-elimination, by providing instructions that contain both familiar concepts and unfamiliar ones (“pick the red box and the green wambim”). In our framework, the agent combines a perception module with a reasoning module that includes internal memory. It uses reinforcement learning to construct a reasoning policy that, by considering all available items in a room, can make a correct inference even for never-seen objects or concepts. Furthermore, it can then perform one-shot learning and use newly learned concepts for inferring additional novel concepts. We evaluate this approach in a new set of environments, showing that agents successfully learn to reason by elimination, and can also learn novel concepts and use them for further reasoning. This approach paves the way to handle open-world environments by extending the abundant supervised learning approaches with reasoning frameworks that can handle novel concepts.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
