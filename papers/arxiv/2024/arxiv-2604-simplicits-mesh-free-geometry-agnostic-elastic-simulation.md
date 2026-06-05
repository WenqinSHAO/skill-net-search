---
id: arxiv-2604
title: "Simplicits: Mesh-Free, Geometry-Agnostic, Elastic Simulation"
conference: arXiv 2024
date: 2024-07
authors:
  - name: "Vismay Modi"
    affiliation: ""
    is_industry: false
  - name: "Nicholas Sharp"
    affiliation: ""
    is_industry: false
  - name: "Or Perel"
    affiliation: ""
    is_industry: false
  - name: "Shinjiro Sueda"
    affiliation: ""
    is_industry: false
  - name: "David I. W. Levin"
    affiliation: ""
    is_industry: false
topics:
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "The proliferation of 3D representations, from explicit meshes to implicit neural fields and more, motivates the need for simulators agnostic to representation. We present a data-, mesh-, and grid-free solution for elastic simulation for any object in any geometric representation undergoing large, no"
url: "https://research.nvidia.com/publication/2024-07_simplicits-mesh-free-geometry-agnostic-elastic-simulation"
status: new
---

# Simplicits: Mesh-Free, Geometry-Agnostic, Elastic Simulation

## 摘要

The proliferation of 3D representations, from explicit meshes to implicit neural fields and more, motivates the need for simulators agnostic to representation. We present a data-, mesh-, and grid-free solution for elastic simulation for any object in any geometric representation undergoing large, nonlinear deformations. We note that every standard geometric representation can be reduced to an occupancy function queried at any point in space, and we define a simulator atop this common interface. For each object, we fit a small implicit neural network encoding spatially varying weights that act as a reduced deformation basis. These weights are trained to learn physically significant motions in the object via random perturbations. Our loss ensures we find a weight-space basis that best minimizes deformation energy by stochastically evaluating elastic energies through Monte Carlo sampling of the deformation volume.At runtime, we simulate in the reduced basis and sample the deformations back to the original domain.Our experiments demonstrate the versatility, accuracy, and speed of this approach on data including signed distance functions, point clouds, neural primitives, tomography scans, radiance fields, Gaussian splats, surface meshes, and volume meshes, as well as showing a variety of material energies, contact models, and time integration schemes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
