---
id: "arxiv-3032"
title: "BYOC: A &quot;Bring Your Own Core&quot; Framework for Heterogeneous-ISA Research"
conference: "arXiv 2020"
date: "2020-03"
authors:
  - name: "Jonathan Balkind"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Katie Lim"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Michael Schaffner"
    affiliation: "ETH Zürich"
    is_industry: false
  - name: "Fei Gao"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Grigory Chirkov"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Ang Li"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Alexey Lavrov"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Tri M. Nguyen"
    affiliation: "Harvard Medical School"
    is_industry: false
  - name: "Yaosheng Fu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Florian Zaruba"
    affiliation: "ETH Zürich"
    is_industry: false
  - name: "Kunal Gulati"
    affiliation: "BITS Pilani"
    is_industry: false
  - name: "Luca Benini"
    affiliation: "ETH Zürich"
    is_industry: false
  - name: "David Wentzlaf"
    affiliation: "Princeton University"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3373376.3378479"
abstract: "Heterogeneous architectures and heterogeneous-ISA designs are growing areas of computer architecture and system software research. Unfortunately, this line of research is significantly hindered by the lack of experimental systems and modifiable hardware frameworks. This work proposes BYOC, a \"Bring "
url: "https://research.nvidia.com/publication/2020-03_byoc-bring-your-own-core-framework-heterogeneous-isa-research"
status: "new"
---

# BYOC: A &quot;Bring Your Own Core&quot; Framework for Heterogeneous-ISA Research

## 摘要

Heterogeneous architectures and heterogeneous-ISA designs are growing areas of computer architecture and system software research. Unfortunately, this line of research is significantly hindered by the lack of experimental systems and modifiable hardware frameworks. This work proposes BYOC, a "Bring Your Own Core" framework that is specifically designed to enable heterogeneous-ISA and heterogeneous system research. BYOC is an open-source hardware framework that provides a scalable cache coherence system, that includes out-of-the-box support for four different ISAs (RISCV 32-bit, RISC-V 64-bit, x86, and SPARCv9) and has been connected to ten different cores. The framework also supports multiple loosely coupled accelerators and is a fully working system supporting SMP Linux. The Transaction-Response Interface (TRI) introduced with BYOC has been specifically designed to make it easy to add in new cores&nbsp;with new ISAs and memory interfaces. This work demonstrates multiple multi-ISA designs running on FPGA and characterises the communication costs. This work describes many of the architectural design trade-offs for building such a flexible system. BYOC is well suited to be the premiere platform for heterogeneous-ISA architecture, system software, and compiler research.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
