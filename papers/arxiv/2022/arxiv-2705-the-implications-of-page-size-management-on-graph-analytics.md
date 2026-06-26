---
id: "arxiv-2705"
title: "The Implications of Page Size Management on Graph Analytics"
conference: "arXiv 2022"
date: "2022-11"
authors:
  - name: "Aninda Manocha"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Zi Yan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Esin Tureci"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Juan Luis Aragón"
    affiliation: "University of Murcia"
    is_industry: false
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Margaret Martonosi"
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
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9975438"
abstract: "Graph representations of data are ubiquitous in analytic applications. However, graph workloads are notorious for having irregular memory access patterns with variable access frequency per address, which cause high translation lookaside buffer (TLB) miss rates and significant address translation ove"
url: "https://research.nvidia.com/publication/2022-11_implications-page-size-management-graph-analytics"
status: "new"
---

# The Implications of Page Size Management on Graph Analytics

## 摘要

Graph representations of data are ubiquitous in analytic applications. However, graph workloads are notorious for having irregular memory access patterns with variable access frequency per address, which cause high translation lookaside buffer (TLB) miss rates and significant address translation overheads during workload execution. Furthermore, these access patterns sparsely span a large address space, yielding memory footprints greater than total TLB coverage by orders of magnitude. It is widely recognized that employing huge pages can alleviate some of these bottlenecks. However, in real systems, huge pages are not always available and the OS often provisions huge pages suboptimally, significantly reducing peak application performance. State-of-the-art huge page management techniques employ heuristics, such as huge page region utilization, to guide page size decisions. However, these heuristics are often only optimal for specific memory access patterns, or footprint sizes, and do not sufficiently adapt to dynamic workload characteristics.This work performs a comprehensive characterization of the effects of page size allocation policy and page placement on graph application throughput. We show that when system memory is nearly full or fragmented (the common case in real systems), huge page resources available to an application are limited and their utility must be maximized. We demonstrate that (1) awareness of single-use memory can eliminate the use of precious huge page resources for data that receives little benefit and (2) coupling degree-aware preprocessing of graph data with programmer-guided use of huge pages boosts performance by 1.26 – 1.57× over using 4KB pages alone, while achieving 77.3 – 96.3% the performance of unbounded huge page usage and requiring only 0.58 – 2.92% of the memory resources. This manual, domain-specific optimization of huge page efficiency in memory constrained systems demonstrates that huge pages are a new class of resource that must be intelligently managed by programmers or next-generation OS policies to optimize application performance.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
