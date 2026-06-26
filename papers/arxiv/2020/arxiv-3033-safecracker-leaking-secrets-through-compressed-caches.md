---
id: "arxiv-3033"
title: "Safecracker: Leaking Secrets through Compressed Caches"
conference: "arXiv 2020"
date: "2020-03"
authors:
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andres Sanchez"
    affiliation: "MIT"
    is_industry: false
  - name: "Christopher W. Fletcher"
    affiliation: "University of Illinois at Urbana-Champaign"
    is_industry: false
  - name: "Daniel Sanchez"
    affiliation: "MIT"
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
    url: "https://dl.acm.org/doi/10.1145/3373376.3378453"
abstract: "The hardware security crisis brought on by recent speculative execution attacks has shown that it is crucial to adopt a security-conscious approach to architecture research, analyzing the security of promising architectural techniques before they are deployed in hardware. This paper offers the first"
url: "https://research.nvidia.com/publication/2020-03_safecracker-leaking-secrets-through-compressed-caches"
status: "new"
---

# Safecracker: Leaking Secrets through Compressed Caches

## 摘要

The hardware security crisis brought on by recent speculative execution attacks has shown that it is crucial to adopt a security-conscious approach to architecture research, analyzing the security of promising architectural techniques before they are deployed in hardware. This paper offers the first security analysis of cache compression, one such promising technique that is likely to appear in future processors. We find that cache compression is insecure because the compressibility of a cache line reveals information about its contents. Compressed caches introduce a new side channel that is especially insidious, as simply storing data transmits information about it. We present two techniques that make attacks on compressed caches practical. Pack+Probe allows an attacker to learn the compressibility of victim cache lines, and Safecracker leaks secret data efficiently by strategically changing the values of nearby data. Our evaluation on a proof-of-concept application shows that, on a common compressed cache architecture, Safecracker lets an attacker compromise a secret key in under 10ms, and worse, leak large fractions of program memory when used in conjunction with latent memory safety vulnerabilities. We also discuss potential ways to close this new compression-induced side channel. We hope this work prevents insecure cache compression techniques from reaching mainstream processors.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
