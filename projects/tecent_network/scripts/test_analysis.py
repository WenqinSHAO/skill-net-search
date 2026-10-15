#!/usr/bin/env python3
"""Validate report denominators, evidence links and single-file HTML integrity."""
import json
import math
import unittest
import hashlib
from datetime import datetime, timezone
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

from build_report import ROOT, aggregate, load_inputs, percent
from export import metadata_tables, build_tables


class AnalysisTests(unittest.TestCase):
    def test_consistent_percentage_rounding(self):
        self.assertEqual(percent(6.25), '6.3%')
        self.assertEqual(percent(25), '25.0%')
    @classmethod
    def setUpClass(cls):
        cls.tables, cls.topics, cls.content, cls.geography, cls.papers = load_inputs()
        cls.results = json.loads((ROOT / 'data/analysis_results.json').read_text())
        cls.html_path = ROOT / 'output/tencent_networking_report.html'
        cls.soup = BeautifulSoup(cls.html_path.read_text(), 'html.parser')

    def test_exact_reviewed_denominator_and_no_posters(self):
        self.assertEqual(len(self.papers), 32)
        self.assertFalse(any(p['publication_type'] == 'poster' for p in self.papers))
        self.assertEqual(sum(p['scope_status'] == 'included' for p in self.papers), 31)

    def test_partition_not_overlapping_tags(self):
        rows = self.results['topic_partition']
        self.assertEqual(sum(r['papers'] for r in rows), 32)
        self.assertTrue(math.isclose(sum(r['share_percent'] for r in rows), 100))
        self.assertEqual(sum(r['networking_core_papers'] for r in rows), 31)
        self.assertTrue(math.isclose(sum(r['networking_core_share_percent'] for r in rows), 100))
        self.assertTrue(all(p['topic'] in self.topics for p in self.papers))

    def test_year_cells_reconcile(self):
        self.assertEqual(len(self.results['year_topics']), 8*7)
        self.assertEqual(sum(r['papers'] for r in self.results['year_topics']), 32)
        for year in range(2019, 2027):
            rows = [r for r in self.results['year_topics'] if r['year'] == year]
            self.assertEqual(sum(r['papers'] for r in rows), sum(p['year'] == year for p in self.papers))

    def test_collaboration_classes_and_tencent_only(self):
        self.assertEqual(self.results['collaboration_counts'], {'Academic/research collaboration': 31, 'Tencent-only': 1})
        self.assertEqual([p['short'] for p in self.papers if p['collaboration_type'] == 'Tencent-only'], ['LADR'])
        self.assertEqual(sum(self.results['first_author_classes'].values()), 32)

    def test_partner_edges_are_paper_local_deduplicated(self):
        edges = self.results['edges']
        self.assertEqual(len(edges), len({(e['paper_id'],e['institution']) for e in edges}))
        for p in self.papers:
            weight = sum(e['fractional_count'] for e in edges if e['paper_id'] == p['paper_id'])
            self.assertTrue(math.isclose(weight, 1 if p['partners'] else 0))
        self.assertTrue(math.isclose(sum(p['fractional_paper_credit'] for p in self.results['partners']), 31))

    def test_geography_roster_has_no_phantom_departments(self):
        names = {p['institution'] for p in self.results['partners']}
        self.assertEqual(names, set(self.geography['institutions']))
        self.assertEqual(len(names), 35)
        self.assertNotIn('School of Computer Science', names)
        self.assertNotIn('Tencent', names)
        self.assertNotIn('JaguarMicro', names)
        self.assertEqual(sum(p['latitude_approx'] is None for p in self.results['partners']), 1)
        self.assertTrue(all(p['source_url'].startswith('https://') for p in self.results['partners']))

    def test_country_counts_use_paper_presence_not_author_count(self):
        for row in self.results['country_distribution']:
            expected = {e['paper_id'] for e in self.results['edges'] if e['country'] == row['country']}
            self.assertEqual(row['papers'], len(expected))
            self.assertTrue(math.isclose(row['paper_share_percent'], len(expected)/32*100))

    def test_ai_label_is_not_all_datacenter_work(self):
        self.assertEqual([p['short'] for p in self.papers if 'AI workload' in p['tags']], ['Holmes','Astral','SwiftEP','DistDPU','Pegasus'])
        self.assertEqual(self.results['explicit_ai_workload_papers'], 5)
        self.assertNotIn('AI workload', next(p for p in self.papers if p['short'] == 'Turbo')['tags'])

    def test_evidence_and_role_caches_exist(self):
        raw = json.loads((ROOT / 'data/publications.json').read_text())['publications']
        for p in raw:
            if p.get('user_reviewed_primary_set'):
                self.assertTrue((ROOT / p['abstract_source_cache']).is_file())
        roles = json.loads((ROOT / 'data/analysis_role_evidence.json').read_text())['checks']
        for role in roles:
            self.assertTrue((ROOT / role['source_cache']).is_file())
            self.assertIn(role['paper'], {p['short'] for p in self.papers})

    def test_html_anchors_and_unique_svg_ids(self):
        ids = [x['id'] for x in self.soup.select('[id]')]
        self.assertEqual(len(ids), len(set(ids)))
        for a in self.soup.select('a[href^="#"]'):
            self.assertIn(a['href'][1:], set(ids))
        self.assertEqual(len(self.soup.select('figure svg')), 7)
        self.assertEqual(len(self.soup.select('.paper-card')), 32)
        self.assertTrue(all(s.get('role') == 'img' and s.get('aria-label') for s in self.soup.select('figure svg')))

    def test_offline_report_and_local_downloads(self):
        self.assertFalse(self.soup.select('script[src],link[rel="stylesheet"],img[src]'))
        for a in self.soup.select('a[href]'):
            url = urlparse(a['href'])
            if not url.scheme and not a['href'].startswith('#'):
                self.assertTrue((self.html_path.parent / unquote(url.path)).resolve().exists(), a['href'])

    def test_recomputed_aggregate_matches_saved_results(self):
        recomputed = aggregate(self.papers, self.topics, self.results['partners'])
        for field in ['topic_partition','year_topics','country_distribution','region_year','collaboration_counts','explicit_ai_workload_papers','first_author_classes']:
            self.assertEqual(recomputed[field], self.results[field], field)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AnalysisTests)
    result = unittest.TextTestRunner().run(suite)
    locations = json.loads((ROOT / 'data/analysis_results.json').read_text())['partners']
    review = {
        'status': 'passed' if result.wasSuccessful() else 'failed',
        'checked_at': datetime.now(timezone.utc).isoformat(), 'analysis_tests_run': result.testsRun,
        'failures': len(result.failures), 'errors': len(result.errors),
        'report_sha256': hashlib.sha256((ROOT / 'output/tencent_networking_report.html').read_bytes()).hexdigest(),
        'content_review': [
            'All 32 primary papers classified; posters excluded; 31-paper core sensitivity retained.',
            'Topic partition is exclusive; workload/mechanism tags and countries are explicitly overlapping.',
            'Full/fractional institution edges reconcile without duplicating dual-affiliation rows.',
            'Reported results, production/prototype/simulation settings and analyst hypotheses are separated.',
            'Competitive mechanisms are not presented as causal business outcomes or a disclosed roadmap.',
            'Academic role claims are limited to explicit PDF credits; recurring names are not global identities.',
            'Matplotlib SVG identifiers are prefixed to prevent collisions in the single-file report.',
            'Desktop/mobile figures reviewed; crowded map labels corrected; mobile charts horizontally scrollable.'
        ],
        'residual_geographic_issues': [{k:r[k] for k in ['institution','source_status','source_url']} for r in locations if r['source_status'] in ['official_page_empty_or_challenge','country_only_in_affiliation_city_unresolved','official_location_fetch_failed','official_location_reference_not_cached']],
        'unresolved_substantive_questions': [
            'Final PDFs unacquired for five primary papers.', 'Component-level contribution ownership and researcher identity disambiguation.',
            'Causal competitive advantage, complete company research output and a confirmed future roadmap.',
            'Publication-time campus precision and expanded traditional CDN/caching coverage.'
        ],
        'browser_review': 'See output/report_browser_review.json for separate desktop/mobile interaction checks.'
    }
    (ROOT / 'output/report_review.json').write_text(json.dumps(review, ensure_ascii=False, indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
