---
id: arxiv-2984
title: "Planaria: Dynamic Architecture Fission for Spatial Multi-Tenant Acceleration of Deep Neural Networks"
conference: arXiv 2020
date: 2020-07
authors:
  - name: "Soroush Ghodrati"
    affiliation: ""
    is_industry: false
  - name: "Byung Hoon Ahn"
    affiliation: ""
    is_industry: false
  - name: "Joon Kyung Kim"
    affiliation: ""
    is_industry: false
  - name: "Sean Kinzer"
    affiliation: ""
    is_industry: false
  - name: "Brahmendra Reddy Yatham"
    affiliation: ""
    is_industry: false
  - name: "Navateja Alla"
    affiliation: ""
    is_industry: false
  - name: "Hardik Sharma"
    affiliation: ""
    is_industry: false
  - name: "Mohammad Alian"
    affiliation: ""
    is_industry: false
  - name: "Eiman Ebrahimi"
    affiliation: ""
    is_industry: false
  - name: "Nam Sung Kim"
    affiliation: ""
    is_industry: false
  - name: "Cliff Young"
    affiliation: ""
    is_industry: false
  - name: "Hadi Esmaeilzadeh"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9251939"
abstract: "Deep Neural Networks (DNNs) have reinvigorated real-world applications that rely on learning patterns of data and are permeating into different industries and markets. Cloud infrastructure and accelerators that offer INFerence-as-a-Service (INFaaS) have become the enabler of this rather quick and in"
url: "https://research.nvidia.com/publication/2020-07_planaria-dynamic-architecture-fission-spatial-multi-tenant-acceleration-deep"
status: new
---

# Planaria: Dynamic Architecture Fission for Spatial Multi-Tenant Acceleration of Deep Neural Networks

## 摘要

Deep Neural Networks (DNNs) have reinvigorated real-world applications that rely on learning patterns of data and are permeating into different industries and markets. Cloud infrastructure and accelerators that offer INFerence-as-a-Service (INFaaS) have become the enabler of this rather quick and invasive shift in the industry. To that end, mostly acceleratorbased INFaaS (Google’s TPU [1], NVIDIA T4 [2], Microsoft Brainwave [3], etc.) has become the backbone of many real-life applications. However, as the demand for such services grows, merely scaling-out the number of accelerators is not economically cost-effective. Although multi-tenancy has propelled datacenter scalability, it has not been a primary factor in designing DNN accelerators due to the arms race for higher speed and efficiency. This paper sets out to explore this timely requirement of multitenancy through a new dimension: dynamic architecture fission. To that end, we define Planaria1 that can dynamically fission (break) into multiple smaller yet full-fledged DNN engines at runtime. This microarchitectural capability enables spatially colocating multiple DNN inference services on the same hardware, offering simultaneous multi-tenant DNN acceleration. To realize this dynamic reconfigurability, we first devise breakable omnidirectional systolic arrays for DNN acceleration that allows omnidirectional flow of data. Second, it uses this capability and a unique organization of on-chip memory, interconnection, and compute resources to enable fission in systolic array based DNN accelerators. Architecture fission and its associated flexibility enables an extra degree of freedom for task scheduling, that even allows breaking the accelerator with regard to the server load, DNN topology, and task priority. As such, it can simultaneously co-locate DNNs to enhance utilization, throughput, QoS, and fairness. We compare the proposed design to PREMA [4], a recent effort that offers multi-tenancy by time-multiplexing the DNN accelerator across multiple tasks. We use the same frequency, the same amount of compute and memory resources for both accelerators. The results show significant benefits with (soft, medium, hard) QoS requirements, in throughput (7.4×, 7.2×, 12.2×), SLA satisfaction rate (45%, 15%, 16%), and fairness (2.1×, 2.3×, 1.9×).

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
