---
id: "arxiv-3073"
title: "Design of a Standard-Compliant Real-Time Neural Receiver for 5G NR"
conference: "arXiv 2024"
date: "2024-09"
authors:
  - name: "Reinhard Wiesmayr"
    affiliation: "ETH Zurich"
    is_industry: false
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fayçal Aït Aoudia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jakob Hoydis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jakub Zakrzewski"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexander Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Telecommunications"
abstract: "We detail the steps required to deploy a multiuser multiple-input multiple-output (MU-MIMO) neural receiver (NRX) in an actual cellular communication system. This raises several exciting research challenges, including the need for realtime inference and compatibility with the 5G NR standard. As the "
url: "https://research.nvidia.com/publication/2024-09_design-standard-compliant-real-time-neural-receiver-5g-nr"
status: "new"
---

# Design of a Standard-Compliant Real-Time Neural Receiver for 5G NR

## 摘要

We detail the steps required to deploy a multiuser multiple-input multiple-output (MU-MIMO) neural receiver (NRX) in an actual cellular communication system. This raises several exciting research challenges, including the need for realtime inference and compatibility with the 5G NR standard. As the network configuration in a practical setup can change dynamically within milliseconds, we propose an adaptive NRX architecture capable of supporting dynamic modulation and coding scheme (MCS) configurations without the need for any re-training and without additional inference cost. We optimize the latency of the neural network (NN) architecture to achieve inference times of less than 1ms on an NVIDIA A100 GPU using the TensorRT inference library. These latency constraints effectively limit the size of the NN and we quantify the resulting signal-to-noise ratio (SNR) degradation as less than 0.7 dB when compared to a preliminary non-real-time NRX architecture. Finally, we explore the potential for site-specific adaptation of the receiver by investigating the required size of the training dataset and the number of fine-tuning iterations to optimize the NRX for specific radio environments using a ray tracing-based channel model. The resulting NRX is ready for deployment in a real-time 5G NR system and the source code including the TensorRT experiments is available online.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
