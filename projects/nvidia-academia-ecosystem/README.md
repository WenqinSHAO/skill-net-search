# NVIDIA-Academia Ecosystem

## Intent

Understand how NVIDIA sources, incubates, and converts academic research into products.
Answer:

1. **Domains** — Which research areas does NVIDIA engage with most? Distribution over time.
2. **Partners** — Who are the academic collaborators? Profile (institutions, geography, concentration).
3. **Transfer pipeline** — What fraction of published work reaches product? Typical latency? Which paths (GTC → SDK → hardware)?
4. **Criticality** — Which academic-sourced ideas became load-bearing for NVIDIA's business?
5. **Exemplar stories** — Full-arc narratives: paper → incubation → product.
6. **GPT-moment shift** — Did patterns change before vs. after late 2022?

## Scope

### In scope

- Papers with NVIDIA-affiliated authors + academic co-authors (co-authored research)
- Academic papers explicitly funded or sponsored by NVIDIA (acknowledgements, grants)
- Academic work that NVIDIA later built on (citations in NVIDIA papers, tech blog references)
- NVIDIA-authored papers at academic venues (even without academic co-authors — captures NVIDIA's research output profile)
- NVIDIA Technical Blog posts that reference published research
- GTC talks that cite or derive from academic work
- Product features traceable to specific papers (CUDA libraries, TensorRT, architectures, interconnects)
- Time window: 2020–2026

### Out of scope

- Pure industry collaborations without academic partners
- NVIDIA's internal-only research that never surfaces publicly
- Marketing content without research lineage
- Patent-only work (unless it also appears as a paper)

## Project-Specific Data Model

Each paper in this project tracks the following, on top of the shared-layer record:

### NVIDIA Role
One or more of:
- `nvidia_author` — NVIDIA employee is a co-author
- `nvidia_funded` — NVIDIA provided funding, hardware, or sponsorship (check acknowledgements)
- `nvidia_built_on` — NVIDIA later cited, blogged about, or built product on this work
- `academic_lead` — academic institution led, NVIDIA collaborated

### Academic Partners
- `institutions: [string]` — normalized institution names
- `key_researchers: [string]` — named individuals driving the work
- `partner_type: [academic_lab | industry_academic_joint | individual_collaborator]`

### Transfer Pipeline
- `transfer_stage: none | cited_by_nvidia | tech_blog | gtc_presented | sdk_feature | hardware_feature | product_shipped`
- `transfer_evidence: [url]` — links to blog posts, GTC talks, product docs, release notes
- `transfer_date: YYYY-MM` — earliest evidence of transfer
- `paper_to_product_latency_months: int` — months from paper publication to first transfer evidence

### Domain
Use a project-specific taxonomy (can evolve):
- `GPU_architecture` — SM design, tensor cores, memory hierarchy
- `Interconnect_networking` — NVLink, NVSwitch, InfiniBand, Spectrum
- `CUDA_ecosystem` — compilers, libraries (cuBLAS, cuDNN, CUTLASS), tools
- `DL_training` — distributed training, parallelism, MoE, optimization
- `DL_inference` — serving, KV cache, quantization, pruning
- `Graphics_rendering` — ray tracing, DLSS, neural rendering
- `Simulation_HPC` — digital twins, scientific computing, physics simulation
- `Robotics_autonomous` — Isaac, DRIVE, embodied AI
- `Foundation_models` — LLMs, VLMs, generative models (NVIDIA's own or co-developed)
- `Data_systems` — storage, data loading, preprocessing at scale

### Criticality Assessment (subjective, done during analysis)
- `criticality: unknown | incidental | supporting | load_bearing`
  - `load_bearing`: without this line of work, a major NVIDIA product or strategy would be materially different
  - `supporting`: contributes to but doesn't define a product
  - `incidental`: interesting but no clear product linkage

## Data Sources

### Tier 1 — Academic publications (high confidence, structured)
- Conference proceedings: NSDI, OSDI, SOSP, ISCA, MICRO, ASPLOS, SIGCOMM, NeurIPS, ICML, ICLR, CVPR, ICCV, SC, HPCA, ATC, EuroSys, FAST
- arXiv: search `nvidia` in author affiliations across cs.AR, cs.DC, cs.LG, cs.CL, cs.CV
- NVIDIA Research publications page: research.nvidia.com/publications

### Tier 2 — Product and technical communication (medium confidence, needs cross-referencing)
- NVIDIA Technical Blog: developer.nvidia.com/blog — search for posts referencing papers, research collaborations
- GTC session catalogs: past GTC events 2020–2026, sessions tagged "research" or co-presented with academics
- NVIDIA Developer News: developer.nvidia.com/news

### Tier 3 — Indirect signals (lower confidence, supplementary)
- NVIDIA GitHub repos: repos with academic paper implementations (e.g., NVIDIA/NeMo, NVIDIA/Megatron-LM, NVIDIA/TensorRT-LLM)
- Citations: papers heavily cited by NVIDIA's own publications
- Press coverage of NVIDIA-academia partnerships

## Hunting Strategy

1. **Batch 1 — Seed from NVIDIA Research page**: Scrape the publications list. This gives us the core co-authored set with canonical metadata.
2. **Batch 2 — Conference sweep 2020–2026**: For each Tier-1 conference, filter by NVIDIA-affiliated authors. This catches work not self-listed on the research page.
3. **Batch 3 — Tech blog and GTC trace**: For papers already in the database, search for matching tech blog posts and GTC sessions to establish transfer evidence.
4. **Batch 4 — arXiv supplement**: Search arXiv for NVIDIA collaborations not captured in conference proceedings (workshops, preprints that later shipped).

Each batch imports into the shared layer first (canonical record in `papers/`, entry in `index/all_papers.json`), then project-specific annotations go into `projects/nvidia-academia-ecosystem/papers/{paper-id}.md`.

## Paper Set

*To be populated — starting with Batch 1.*

## Open Ends

- How to systematically discover NVIDIA-funded academic work (acknowledgements are not always structured)?
- What's the right granularity for "product" — chip generation (H100, B200), SDK version (CUDA 12.x), or individual feature (FlashAttention in TensorRT-LLM)?
- Should NVIDIA-authored papers without academic co-authors be tracked for the "profile of NVIDIA research output" angle, or kept out of scope?
- The `criticality` field is inherently subjective — should we defer scoring until we have enough data, or score as we go and refine?
- How to weight GTC sessions? Some are forward-looking vision, some are shipping product. Need a taxonomy.
