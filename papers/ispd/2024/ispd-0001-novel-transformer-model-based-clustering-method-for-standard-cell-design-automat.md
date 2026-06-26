---
id: "ispd-0001"
title: "Novel Transformer Model Based Clustering Method for Standard Cell Design Automation"
conference: "ISPD 2024"
date: "2024-03"
authors:
  - name: "Chia-Tung (Mark) Ho"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ajay Chandna"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Guan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alvin Ho"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Minsoo Kim"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yaguang Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
external_links:
  - name: "Novel Transformer Model Based Clustering Method for Standard Cell Design Automa…"
    url: "https://ispd.cc/ispd2024/index.php"
abstract: "Standard cells are essential components of modern digital circuit designs. With process technologies advancing beyond 5nm, more routability issues have arisen due to the decreasing number of rout\u0002ing tracks (RTs), increasing number and complexity of design rules, and strict patterning rules. The sta"
url: "https://research.nvidia.com/publication/2024-03_novel-transformer-model-based-clustering-method-standard-cell-design-automation"
status: "new"
---

# Novel Transformer Model Based Clustering Method for Standard Cell Design Automation

## 摘要

Standard cells are essential components of modern digital circuit designs. With process technologies advancing beyond 5nm, more routability issues have arisen due to the decreasing number of routing tracks (RTs), increasing number and complexity of design rules, and strict patterning rules. The standard cell design automation framework is able to automatically design standard cell layouts, but it is struggling to resolve the severe routability issues in advanced nodes. As a result, a better and more efficient standard cell design automation method that can not only resolve the routability issue but also scale to hundreds of transistors to shorten the development time of standard cell libraries is highly needed and essential. High quality device clustering with the considerations of routability in the layouts of different technology nodes can reduce the complexity and assist finding the routable layouts faster. In this paper, we develop a novel transformer model-based clustering methodology - training the model using LVS/DRC clean cell layouts and leveraging the personalized page rank vectors to cluster the devices with the attentions to netlist graph and learned embeddings from the actual LVS/DRC clean layouts. On a benchmark of 94 complex and hard-to-route standard cells, the proposed method not only generates 15% more LVS/DRC clean layouts, but also achieves average 12.7X faster than previous work. The proposed method can generate 100% LVS/DRC clean cell layouts over 1000 standard cells and achieve 14.5% smaller cell width than an industrial standard cell library.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
