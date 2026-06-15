# Data Foundation Audit

This project fixes the cohort definition as:

- researchers with at least one paper in SIGCOMM, NSDI, CoNEXT, HotNets, or IMC during 2018-2022.

Before interpreting region, sector, or transition labels, the publication
history must be cleaned to match the analysis scope.

## Current Foundation Rules

Records are retained for auditability but excluded from metrics when they are:

- DBLP journals/articles
- CoRR/arXiv records
- proceedings volumes
- books, theses, `www`, `data`, and other non-conference DBLP record types
- missing venue
- duplicate records for the same researcher

Included records receive:

- `analysis_id`
- `included_in_analysis`
- `exclusion_reason`
- `zone`
- `zone_confidence`
- `classification_reason`

## Labeling Policy Still Under Review

The following labels are intentionally not treated as settled:

- region
- industry vs academia
- transition taxonomy
- Zone 2 AI infrastructure vs generic systems
- Zone 3 pure AI/ML vs AI applied to networking/systems

Current code should therefore preserve low-confidence and unclassified states
rather than silently forcing every record into a headline category.

## Known Historical Issues

Earlier pipeline outputs included journals and CoRR records despite the stated
scope. Broad systems venues also defaulted to Zone 2, causing generic systems
papers and proceedings volumes to be treated as AI infrastructure. Those outputs
should be considered exploratory only.

## Current Coverage Snapshot

After changing the cohort threshold to `>=1`, the broad cohort contains 3,571 researchers from 1,146 checked top-networking conference papers.

The currently fetched full-publication-history artifacts still cover the previous 492-person core subset. The itinerary builder records this explicitly:

- `broad_cohort_size`: 3,571
- `researchers_in_input`: 492
- `cohort_members_missing_publication_history`: 3,079

The current `top100_itineraries.json` is therefore a discovery subset from the already-fetched core researchers, not yet from the full broad cohort. A full broad-cohort itinerary pass requires fetching the remaining DBLP author histories.
