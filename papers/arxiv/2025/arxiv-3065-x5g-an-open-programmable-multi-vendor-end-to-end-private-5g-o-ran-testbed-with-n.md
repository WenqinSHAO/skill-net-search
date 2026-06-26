---
id: "arxiv-3065"
title: "X5G: An Open, Programmable, Multi-vendor, End-to-end, Private 5G O-RAN Testbed with NVIDIA ARC and OpenAirInterface"
conference: "arXiv 2025"
date: "2025-09"
authors:
  - name: "Davide Villa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Imran Khan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Florian Kaltenberger"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nicholas Hedberg"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rúben Soares da Silva"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stefano Maxenti"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Leonardo Bonati"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anupa Kelkar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chris Dick"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eduardo Baena"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Josep M. Jornet"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tommaso Melodia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michele Polese"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dimitrios Koutsonikolas"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Telecommunications"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/pdf/2406.15935"
abstract: "As Fifth generation (5G) cellular systems transition to softwarized, programmable, and intelligent networks, it becomes fundamental to enable public and private 5G deployments that are (i) primarily based on software components while (ii) maintaining or exceeding the performance of traditional monol"
url: "https://research.nvidia.com/publication/2025-09_x5g-open-programmable-multi-vendor-end-end-private-5g-o-ran-testbed-nvidia-arc"
status: "new"
---

# X5G: An Open, Programmable, Multi-vendor, End-to-end, Private 5G O-RAN Testbed with NVIDIA ARC and OpenAirInterface

## 摘要

As Fifth generation (5G) cellular systems transition to softwarized, programmable, and intelligent networks, it becomes fundamental to enable public and private 5G deployments that are (i) primarily based on software components while (ii) maintaining or exceeding the performance of traditional monolithic systems and (iii) enabling programmability through bespoke configurations and optimized deployments. This requires hardware acceleration to scale the Physical (PHY) layer performance, programmable elements in the Radio Access Network (RAN) and intelligent controllers at the edge, careful planning of the Radio Frequency (RF) environment, as well as end-to-end integration and testing. In this paper, we describe how we developed the programmable X5G testbed, addressing these challenges through the deployment of the first 8-node network based on the integration of NVIDIA Aerial RAN CoLab Over-the-Air (ARC-OTA), OpenAirInterface (OAI), and a near-real-time RAN Intelligent Controller (RIC). The Aerial Software Development Kit (SDK) provides the PHY layer, accelerated on Graphics Processing Unit (GPU), with the higher layers from the OAI open-source project interfaced with the PHY through the Small Cell Forum (SCF) Functional Application Platform Interface (FAPI). An E2 agent provides connectivity to the O-RAN Software Community (OSC) nearreal-time RIC. We discuss software integration, network infrastructure, and a digital twin framework for RF planning. We then profile the performance with up to 4 Commercial Off-the-Shelf (COTS) smartphones for each base station with iPerf and video streaming applications, as well as up to 25 emulated User Equipments (UEs), measuring a cell rate higher than 1.65 Gbps in downlink and 143 Mbps in uplink.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
