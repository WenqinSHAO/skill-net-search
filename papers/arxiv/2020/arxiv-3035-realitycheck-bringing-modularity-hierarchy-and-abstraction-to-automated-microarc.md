---
id: arxiv-3035
title: "RealityCheck: Bringing Modularity, Hierarchy, and Abstraction to Automated Microarchitectural Memory Consistency Verification"
conference: arXiv 2020
date: 2020-03
authors:
  - name: "Daniel Lustig"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yatin A. Manerkar"
    affiliation: ""
    is_industry: false
  - name: "Margaret Martonosi"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
abstract: "Modern SoCs are heterogeneous parallel systems comprised of components developed by distinct teams and possibly even different vendors. The memory consistency model (MCM) of processors in such SoCs specifies the ordering rules which constrain the values that can be read by load instructions in paral"
url: "https://research.nvidia.com/publication/2020-03_realitycheck-bringing-modularity-hierarchy-and-abstraction-automated"
status: new
---

# RealityCheck: Bringing Modularity, Hierarchy, and Abstraction to Automated Microarchitectural Memory Consistency Verification

## 摘要

Modern SoCs are heterogeneous parallel systems comprised of components developed by distinct teams and possibly even different vendors. The memory consistency model (MCM) of processors in such SoCs specifies the ordering rules which constrain the values that can be read by load instructions in parallel programs running on such systems. The implementation of required MCM orderings can span components which may be designed and implemented by many different teams. Ideally, each team would be able to specify the orderings enforced by their components independently and then connect them together when conducting MCM verification. However, no prior automated approach for formal hardware MCM verification provided this. To bring automated hardware MCM verification in line with the realities of the design process, we present RealityCheck, a methodology and tool for automated formal MCM verification of modular microarchitectural ordering specifications. RealityCheck allows users to specify their designs as a hierarchy of distinct modules connected to each other rather than a single flat specification. It can then automatically verify litmus test programs against these modular specifications. RealityCheck also provides support for abstraction, which enables scalable verification by breaking up the verification of the entire design into smaller verification problems. We present results for verifying litmus tests on 7 different designs using RealityCheck. These include in-order and out-of-order pipelines, a non-blocking cache, and a heterogeneous processor. Our case studies cover the TSO and RISC-V (RVWMO) weak memory models. RealityCheck is capable of verifying 98 RVWMO litmus tests in under 4 minutes each, and its capability for abstraction enables up to a 32.1% reduction in litmus test verification time for RVWMO.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
