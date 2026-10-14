# Tencent networking research and academic partnerships

## Intent

Survey Tencent's networking research over time and identify its academic collaborators, by research area, institution, author, geography, and year. The fundamental deliverable is an Excel workbook with publication metadata and individual, publication-time author affiliations. The folder spelling `tecent_network` is intentional.

This project follows the local [net-research workflow](../../SKILL.md) and the evidence/data/analysis separation used in the neighboring NVIDIA and networking researcher projects.

## Scope

Target: all publicly discoverable networking publications from Tencent's founding in 1998 through the collection date. There is no intended recent-year cutoff. Coverage must be established venue by venue and year by year; a search result count is never a completeness claim.

The active sweep is **2019–2026: NSDI, SIGCOMM, CoNEXT/PACMNET, IMC and HotNets**. ICNP and mobile-centric conferences are excluded by request. As of 2026-10-10, the inventory has 32 primary-venue records (31 included in networking scope and one boundary candidate) plus two SIGCOMM posters. This is an observed corpus, not an exhaustive total. The added CoNEXT 2021 paper links Tencent with Tsinghua; CETC is an additional industry coauthor. IMC and HotNets currently have zero confirmed Tencent-coauthored records, not proven zero output.

Include papers with a Tencent-affiliated author, including Tencent Cloud and Tencent research units. Retain industry-only papers to describe the company's research portfolio. Separately track papers with funding, deployment, or acknowledgements but no Tencent author; these signals do not establish coauthorship. Subsidiaries and acquired companies require explicit historical entity evidence before inclusion.

Networking includes datacenter fabrics, RDMA, transport and congestion control, WAN/optical networking, routing, cloud virtualization, programmable networks, measurement/reliability, CDN/edge, mobile/wireless, real-time media, and network security. AI infrastructure is included where communication, interconnects, network scheduling, or network-dependent training/serving is a substantive contribution. Generic ML, social-network analysis, and unrelated storage/database work are not automatically networking.

Conference and journal papers, workshops, posters/demos, and preprints should be collected with distinct publication types. Related versions must be linked before analysis to prevent double counting. Journals and preprints are not silently discarded.

## Outputs and reproducibility

- `output/tencent_networking_metadata.xlsx`: compact, metadata-completed handoff for the **32 primary papers manually listed by the user**, with individual author-affiliation rows, source checks, and the two posters in separate sheets. All 32 have sourced full abstracts and reviewed author assignments: 27 PDF-verified and five publisher-deposit-verified. This does not certify exhaustive venue coverage or global person identities.
- `data/publications.json`: evidence-backed project records, stable project IDs, shared-index links when an exact match exists.
- `data/coverage.json`: each attempted venue/year URL, fetch/parser outcome, and remaining search work.
- `raw/`: cached official pages and their acquisition times.
- Raw caches and PDFs remain local and are excluded from Git. Committed JSON/CSV/workbooks retain source URLs and cache references; checks requiring cached evidence need those local files or a fresh source acquisition.
- `output/tencent_networking_publications.xlsx`: filterable publication, author-affiliation, institution, collaboration, coverage, and quality sheets.
- `output/*.csv`: portable equivalents of each data table.
- `output/quality_report.json`: missing fields and structural checks.
- `data/manual_checks.json`: independently reviewed inclusions, exclusions, and affiliation discrepancies.
- `data/independent_openalex.json`: separate Tencent institution-index discovery, including source query logs; the index is demonstrably incomplete for USENIX.
- `data/program_discovery.json`: actual CoNEXT Angular program templates plus IMC and HotNets programs/accepted lists, with failed fetches preserved.
- `data/audit_summary.json`: title-overlap diagnostics against a separate DBLP-derived catalog, including PACMNET; not a recall estimate.
- Workbook `Annual_Stats`, `Independent_Checks`, `Discovery_Audit`, and `PDF_Checks`: counts, independent decisions, and first-two-page PDF screening evidence.
- `data/proceedings_ledger.json` and workbook `Proceedings_Ledger`: paper-level union of independent bibliographic catalogs and official listings across all 40 active venue/year cells, including non-Tencent records. Inventory rows still need title/publication-type reconciliation and must not be treated as a finalized research-paper denominator.
- Workbook `Completeness`, `Unresolved_Queue`, `Source_Parse_Log`, and `Excluded_Records`: cell-level decision totals, unresolved records, unsupported/stale sources, and excluded agenda/editorial records. No cell is currently certified affiliation-complete.
- `data/ledger_pdf_audit.json`: 143 additional successful NSDI first-two-page PDF checks, including 18 existing Tencent records; screening is not full individual affiliation verification.
- `data/user_program_check.json`: exact venue/year/title reconciliation of the user's official-program list, including the documented FlexWAN title variant; `NA` remains a user observation rather than certified absence.
- `data/metadata_audit.json`, `metadata_review_decisions.json`, and `metadata_pdf_checks.json`: publisher-deposited ordered-author checks, explicit reviewed assignments/discrepancies, and eight additional SIGCOMM PDF acquisitions. Recovered author keywords are sourced separately from analyst tags.

Run from this directory:

```bash
python3 scripts/collect.py --start-year 2010 --end-year 2026
python3 scripts/enrich.py
python3 scripts/discover_programs.py
python3 scripts/audit_openalex.py
python3 scripts/audit_pdfs.py
python3 scripts/import_extension.py
python3 scripts/complete_metadata.py
python3 scripts/summarize_audit.py
python3 scripts/collect_completeness_sources.py
python3 scripts/build_completeness.py
python3 scripts/verify_ledger_pdfs.py
python3 scripts/build_completeness.py
python3 scripts/export.py
python3 scripts/validate.py
python3 scripts/test_foundation.py
```

Collection requires the libraries in `requirements.txt`; PDF screening additionally requires `pdftotext`. Export and structural validation use the Python standard library. Rerunning collection reuses cached pages. `--refresh` deliberately fetches them again. The original collector targets NSDI and SIGCOMM; `discover_programs.py` covers CoNEXT, IMC and HotNets for 2019–2026. `import_extension.py` imports the specifically reviewed extension records; it is not an automatic exhaustive classifier. Older proceedings and other venues still require additional collectors. Errors and unsupported layouts remain visible in Coverage. No credentials are required. Optional `scripts/validate.py --excel-reader-path /path/to/openpyxl` independently reads every workbook cell.

The workbook uses modern `.xlsx`, an Excel-readable successor to `.xls`; JSON and CSV are the reproducible data foundation. Generated outputs should not be hand-edited. Put corrections in `data/overrides.json`, keyed by project paper ID; the exporter applies these without modifying raw evidence. Corrections should include their supporting URLs. Rerun enrichment after collection to restore PDF/abstract supplements from the cache.

## Data rules

Author order is preserved. One row represents one author-affiliation assignment on one publication; dual affiliations generate multiple rows. Store the raw affiliation beside its normalized institution, and use the affiliation at publication time rather than the author's current job. Affiliation normalization and automatic author-group parsing are explicitly labeled. Exact DBLP author-list comparisons are structural checks, not affiliation verification.

The 2026-10-14 metadata pass cross-checks every DOI-bearing record against publisher-deposited author order. `author_list_check_source` identifies the check source; the original DBLP-specific outcome is retained as `dblp_author_list_check`. Reviewed publication-time affiliations have `pdf_verified` or `publisher_deposit_verified` evidence states. The latter is not a claim that the PDF was retrieved. Five primary-paper PDFs remain unacquired from ACM; their abstracts are complete official-program fields and their individual affiliation mappings come from reviewed publisher deposits.

Important retained discrepancies: Dorado's final program conflicts with its accepted list and publisher deposit for three affiliations; the selected assignments follow the publisher deposit. Holmes spells the last author "Juncheng Jiang" in the manuscript but "Junchen Jiang" on its cover, official BibTeX and bibliography; both spellings are retained. XFir's coauthor publication-list text omits two authors, while the final PDF and publisher deposit agree on all 18. City University of Hong Kong, University of Hong Kong, CUHK and CUHK Shenzhen are distinct normalized entities. The 2019 poster still lacks an accessible primary-source abstract. Missing fields are never fabricated.

Author IDs are paper-local authorship IDs. A name key is only a discovery aid: homonyms are not merged into a global person identity. ORCID/DBLP person identifiers, author histories, and manual evidence are required before person-level network claims.

Author/publisher keywords remain separate from analyst tags. The exporter suggests tags from titles for unreviewed records. The initial set has primary-program scope/tag reviews in `data/overrides.json`; the tag status distinguishes these from provisional title rules. PDF review remains pending. A paper can have both DCN and AI infrastructure tags. Funding and deployment do not substitute for affiliation evidence.

Missing information stays empty and is listed in Quality. Every abstract has a source URL. Every affiliation assignment retains the official author line and source. Cached program metadata is useful evidence, but PDF author blocks are the final reconciliation source when program and paper disagree.

## Paper set

The current collection is enumerated in `output/publications.csv` and the workbook's Publications sheet, with an inclusion reason for every record. Records with Tencent author evidence but unreviewed networking relevance have `scope_status=candidate`. The first sweep is a working corpus, not an exhaustive inventory.

## Analysis questions

1. Which networking areas grow, persist, or decline across years?
2. Which academic institutions and named researchers coauthor work in DCN, AI infrastructure, and other areas?
3. How geographically diverse are the observed academic collaborators? Geography denotes institution location, not author nationality or deployment location.
4. Which partners recur across areas and years, and which ties are episodic?
5. Which papers report Tencent deployments, and how do these relate to academic collaboration?

The Collaboration sheet provides one observed Tencent-to-academic-institution edge per paper, with both full and fractional paper counts. Filter `publication_type` when analyzing main-venue papers versus posters. These are coauthorship observations, not evidence of formal partnerships, contractual relationships, or research leadership. Institution counts can exceed publication counts. Country fields stay unknown unless supplied by reviewed institution metadata.

## Open ends

See [COLLECTION_PLAN.md](COLLECTION_PLAN.md) for the staged collection, audit, and analysis workflow and its completion criteria.

- Complete historical proceedings, particularly before 2010; failed/unsupported pages are not zero-publication years.
- Close the remaining CoNEXT/PACMNET, IMC and HotNets affiliation/proceedings gaps, especially early-year papers, poster/companion records and 2026. The independent local catalog predates the current sweep; 2026 catalog coverage is incomplete. Inherited CoNEXT `toc.html` templates can be stale and are excluded from title-overlap diagnostics.
- Later broaden to INFOCOM, ToN, APNet, ICCCN, relevant systems/security venues, arXiv, and Chinese-language outlets. ICNP and mobile-centric conferences are out of scope.
- Search Tencent technical/research pages and academic collaborators' publication lists; search in English and Chinese.
- Reconcile individual affiliations against PDFs, extract publisher keywords, fill DOI gaps, and review taxonomy assignments.
- Resolve author identities and multi-campus institution geography with dated evidence.
- Link conference, journal, workshop, and preprint versions and audit deduplication.
- Continue the independent audit: institution-index searches, paper-header screening and reviewed author-history leads now exist, but none individually proves complete recall. HotNets 2022–2025 screening covers 164 publicly linked paper PDFs; older years still need equivalent PDF coverage. Index-derived TOO poster affiliations remain explicitly pending PDF review.
- Shared-database import follows SPEC.md deduplication and validation; this first project collection links existing shared IDs without changing the shared database.
