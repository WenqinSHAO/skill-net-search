# Illustrated report: analysis and review plan

## Analytical contract

Use the 32 user-reviewed primary papers as the descriptive portfolio, with a clearly marked 31-paper networking-core sensitivity check. Keep the two posters out of headline shares. The five-venue 2019–2026 corpus is not all Tencent research; 2019/2020 observed zeros and the dated 2026 endpoint are not complete-output claims. Publication year is not project start or deployment year.

One reviewed primary topic per paper makes the topic partition sum to 100%. Overlapping mechanism/workload tags are separate. Classify Tencent-only, other-industry collaboration without academia, and academic/research coauthorship separately. Academic/research presence includes dual affiliations; that is not proof of an independently funded university project. Neither author order nor coauthorship assigns contribution roles.

## Stages and acceptance gates

1. **Content skeleton and questions:** overview; topics and annual composition; university/research geography; recurring researcher cohorts; topic deep dives; implications; methods and unresolved questions; searchable paper-level evidence appendix.
2. **Reviewed analysis layer:** store topic decisions, per-paper mechanism/results/context, geographic evidence, and synthesis separately from collected metadata. Fix normalization errors before aggregation. No silent edits to raw sources or shared records.
3. **Reproducible figures:** partition, year-by-topic counts and composition, collaboration type, partner recurrence, partner/topic matrix, world + East Asia map, observed affiliation trajectories, and a technology-stack schematic. Publish the chart data as CSV/JSON and plot code.
4. **Draft:** distinguish paper-reported results, analyst synthesis and forward-looking hypotheses. Every quantitative benefit has a paper source, baseline/context and a non-additivity warning. No inference of market share, revenue, formal partnerships or individual contributions from bibliometrics.
5. **Review and improve:** verify denominators and geography coverage, exclude posters, preserve the boundary paper, check overlapping fractions and name ambiguity, reconcile every illustrated number to exported tables, and check all HTML links/anchors.
6. **Layout:** self-contained HTML with inline SVG, responsive cards/tables, print styling, accessible chart descriptions and readable source links. Review desktop and mobile browser renders, not only source code.

## Questions needing investigation

- How much of the apparent recent growth is acceptance/publication timing, venue coverage or retrospective disclosure rather than new R&D investment?
- Which academic partners contributed theory, systems design, implementation or evaluation? Author affiliations establish presence; detailed role attribution needs contribution statements or corroborated first-person evidence.
- Are similar named researchers across papers the same person? Track verified identifiers where present; otherwise report recurring name strings and observed affiliation combinations rather than global identities or career histories.
- Does a reported deployment or benchmark translate to durable competitive advantage? Separate plausible cost/reliability/iteration-speed mechanisms from verified causal business outcomes.
- How do RTC, cloud gateways, WAN and AI fabrics actually integrate in production? Cross-paper architectural alignment is not proof of a common deployed stack.
- What is missing for traditional CDN/caching, INFOCOM/ToN and non-top-five venues? Do not infer absence from this selected corpus.
- Which five primary papers still lack retrievable final PDFs? Use their complete official abstracts/publisher author mappings, but flag detailed implementation/role comparisons as lower confidence.
- How sensitive are partner counts to Dorado's conflicting official affiliations, dual affiliations, departmental normalization and inclusion of Hestia?

## Deliverables

- `data/analysis_papers.json`: reviewed topic/evidence annotations.
- `data/analysis_geography.json`: institutional location evidence and explicitly approximate plotting coordinates.
- `data/analysis_results.json`, `output/analysis_*.csv`: reproducible aggregates.
- `scripts/build_report.py`: calculations, SVG figures and HTML assembly.
- `scripts/test_analysis.py`: numerical and report-integrity checks.
- `output/tencent_networking_report.html`: illustrated offline report.
- `output/report_figures/`: reusable SVG figures and browser review captures.
- `output/report_review.json`: review results and explicitly unresolved questions.

## First report status · 2026-10-15

The content skeleton, reviewed 32-paper classification/evidence matrix, seven SVG/PNG figures, full HTML draft, source-linked contribution examples and desktop/mobile layout pass are implemented. The geographic footprint has 35 academic/research institutions; city coordinates are approximate anchors, one institute remains city-unresolved, and NJUST's official page remains unreadable to the local collector. Three otherwise-blocked locations were cross-checked through official web pages and retain that different acquisition status.

Review improvements include a department-normalization fix, exclusive-topic versus overlapping-AI-tag separation, non-additive benchmark caveats, paper-level rather than author-row partner counts, prefixed inline SVG IDs, deduplicated city bubbles, map-label spacing, mobile figure scrolling and a search-reset behavior on evidence links. Tests reconcile the main/core denominators, weighted edges, country presence, evidence files, local downloads, anchors and HTML structure. Browser checks cover desktop/mobile overflow, search and citation navigation, chart presence and console errors. See the generated review JSON files for results tied to the actual report hash.

The output is a usable first illustrated report, not the end of the open investigations: fine-grained contribution ownership, causal competitive advantage, missing final PDFs and confirmed future strategy remain explicitly unanswered.

## Chinese edition · 2026-10-15

`output/tencent_networking_report_zh.html` is a separate offline Chinese edition; the English report and source metadata remain unchanged. All seven figures, seven topic deep dives, cohorts, methods and 32 paper-level interpretations are localized. Original titles and expandable English annotations/source caveats remain available for exact checking. Chinese SVGs embed CJK glyph outlines rather than relying on reader-installed fonts.

Eight author names have primary-source Chinese-name verification in `data/author_names_zh.json`, with institution/email/publication identity checks and bilingual display. Unverified names remain English; no pinyin-based guessing or historical affiliation replacement. The ambiguous artificial-intelligence institute's official Chinese identity also remains unresolved rather than invented.

Rebuild with `python3 scripts/build_report_zh.py`; review with `node scripts/review_report.mjs --zh` then `python3 scripts/test_report_zh.py`. Eight localization/parity tests complement the 13 English analysis tests and 22 metadata foundation tests. Desktop (1440 px) and mobile (390 px) browser checks cover figures, anchors, overflow, English/Chinese searches and citation resets, with a final-report hash recorded in `output/report_browser_review_zh.json`.
