---
id: "siggraph-0066"
title: "StrokeStrip: Joint Parameterization and Fitting of Stroke Clusters"
conference: "SIGGRAPH 2021"
date: "2021-08"
authors:
  - name: "Dave Pagurek van Mossel"
    affiliation: "UBC"
    is_industry: false
  - name: "Chenxi Liu"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Nicholas Vining"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mikhail Bessmeltsev"
    affiliation: "Universite de Montreal"
    is_industry: false
  - name: "Alla Sheffer"
    affiliation: "University of British Columbia"
    is_industry: false
topics:
  - Applied_perception
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Computer Graphics"
  - "Human Computer Interaction"
external_links:
  - name: "Technical Report"
    url: "https://www.cs.ubc.ca/labs/imager/tr/2021/StrokeStrip/"
abstract: "When creating freeform drawings, artists routinely employ clusters of overdrawn strokes to convey intended, aggregate curves. The ability to algorithmically fit these intended curves to their corresponding clusters is central to many applications that use artist drawings as inputs. However, while hu"
url: "https://research.nvidia.com/publication/2021-08_strokestrip-joint-parameterization-and-fitting-stroke-clusters"
status: "new"
---

# StrokeStrip: Joint Parameterization and Fitting of Stroke Clusters

## 摘要

When creating freeform drawings, artists routinely employ clusters of overdrawn strokes to convey intended, aggregate curves. The ability to algorithmically fit these intended curves to their corresponding clusters is central to many applications that use artist drawings as inputs. However, while human observers effortlessly envision the intended curves given stroke clusters as input, existing fitting algorithms lack robustness and frequently fail when presented with input stroke clusters with non-trivial geometry or topology. We present&nbsp;StrokeStrip, a new and robust method for fitting intended curves to vector-format stroke clusters. Our method generates fitting outputs consistent with viewer expectations across a vast range of input stroke cluster configurations. We observe that viewers perceive stroke clusters as continuous, varying-width&nbsp;strips&nbsp;whose paths are described by the intended curves. An arc length parameterization of these strips defines a natural mapping from a strip to its path. We recast the curve fitting problem as one of parameterizing the cluster strokes using a&nbsp;joint&nbsp;1D parameterization that is the restriction of the natural arc length parameterization of this strip to the strokes in the cluster. We simultaneously compute the joint cluster parameterization and implicitly reconstruct the&nbsp;a priori&nbsp;unknown strip geometry by solving a variational problem using a discrete-continuous optimization framework. We use this parameterization to compute parametric aggregate curves whose shape reflects the geometric properties of the cluster strokes at the corresponding isovalues. We demonstrate StrokeStrip outputs to be significantly better aligned with observer preferences compared to those of prior art; in a perceptual study viewers preferred our fitting outputs by a factor of 12:1 compared to alternatives. We further validate our algorithmic choices via a range of ablation studies; extend our framework to raster data; and illustrate applications that benefit from the parameterizations produced. &nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
