---
id: arxiv-2913
title: "Verifying High-Level Latency-Insensitive Designs with Formal Model Checking"
conference: arXiv 2021
date: 2021-02
authors:
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nathaniel Pinckney"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alicia Klinefelter"
    affiliation: ""
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Circuits and VLSI Design"
external_links:
  - name: "Verifying High-Level Latency-Insensitive Designs with Formal Model Checking"
    url: "https://arxiv.org/abs/2102.06326"
abstract: "Latency-insensitive design mitigates increasing interconnect delay and enables productive component reuse in complex digital systems. This design style has been adopted in high-level design flows because untimed functional blocks connected through latency-insensitive interfaces provide a natural com"
url: "https://research.nvidia.com/publication/2021-02_verifying-high-level-latency-insensitive-designs-formal-model-checking"
status: new
---

# Verifying High-Level Latency-Insensitive Designs with Formal Model Checking

## 摘要

Latency-insensitive design mitigates increasing interconnect delay and enables productive component reuse in complex digital systems. This design style has been adopted in high-level design flows because untimed functional blocks connected through latency-insensitive interfaces provide a natural communication abstraction. However, latency-insensitive design with high-level languages also introduces a unique set of verification challenges that jeopardize functional correctness. In particular, bugs due to invalid consumption of inputs and deadlocks can be difficult to detect and debug with dynamic simulation methods. To tackle these two classes of bugs, we propose formal model checking methods to guarantee that a high-level latency-insensitive design is unaffected by invalid input data and is free of deadlock. We develop a well-structured verification wrapper for each property to automatically construct the corresponding formal model for checking. Our experiments demonstrate that the formal checks are effective in realistic bug scenarios from high-level designs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
