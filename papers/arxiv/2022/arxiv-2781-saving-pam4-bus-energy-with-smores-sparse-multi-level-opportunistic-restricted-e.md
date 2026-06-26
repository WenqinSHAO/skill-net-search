---
id: "arxiv-2781"
title: "Saving PAM4 Bus Energy with SMOREs: Sparse Multi-level Opportunistic Restricted Encodings"
conference: "arXiv 2022"
date: "2022-04"
authors:
  - name: "Mike O'Connor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Donghyuk Lee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Niladrish Chatterjee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike O&#039;Connor"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Circuits and VLSI Design"
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9773229"
abstract: "Pulse Amplitude Modulation (PAM) uses multiple voltage levels as different data symbols, transferring multiple bits of data simultaneously, thereby enabling higher communication bandwidth without increased operating frequencies. However, dividing the voltage into more symbols leads to a smaller volt"
url: "https://research.nvidia.com/publication/2022-04_saving-pam4-bus-energy-smores-sparse-multi-level-opportunistic-restricted"
status: "new"
---

# Saving PAM4 Bus Energy with SMOREs: Sparse Multi-level Opportunistic Restricted Encodings

## 摘要

Pulse Amplitude Modulation (PAM) uses multiple voltage levels as different data symbols, transferring multiple bits of data simultaneously, thereby enabling higher communication bandwidth without increased operating frequencies. However, dividing the voltage into more symbols leads to a smaller voltage difference between adjacent symbols, making the interface more vulnerable to crosstalk and power noise. GDDR6X adopts four-level symbols (PAM4) with Maximum Transition Avoidance (MTA) coding, which reduces the effects of crosstalk. However, current coding approaches can consume excess energy and produce excess power noise. This paper introduces novel energy reduction techniques for PAM interfaces, specifically demonstrating them for GDDR6X PAM4. Inspired by prior work on conventional single-ended I/O interfaces, we leverage the unused idle periods in DRAM channels between data transmissions to apply longer but more energy-efficient codes. To maximize the energy savings, we build multiple sparse encoding schemes to fit different sized gaps in the DRAM traffic. These sparse encodings can provide energy reductions of up to 52% when transferring 4-bit data using a 3-symbol sequence. We evaluate these coding techniques using an NVIDIA RTX 3090 baseline, a recent GPU which uses GDDR6X with PAM4 signaling. Our evaluation shows the opportunity for large energy savings at the DRAM I/O interface (28.2% on average) over many HPC/DL applications with minimal performance degradation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
