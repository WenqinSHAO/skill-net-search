"""Regression checks for high-impact author and institution parsing cases."""
import unittest
import json
from unittest.mock import patch

from bs4 import BeautifulSoup

from collect import parenthetical_authors, usenix_authors
from export import build_tables, institution_parts, metadata_tables
from summarize_audit import title_key
from build_completeness import author_agreement
from complete_metadata import pdf_fields, user_list
from collect import ROOT


class FoundationTests(unittest.TestCase):
    def test_department_conjunction_does_not_create_phantom_institution(self):
        raw = 'School of Computer Science and Technology, University of Science and Technology of China, Hefei, Anhui, China'
        self.assertEqual([x[0] for x in institution_parts(raw)], ['University of Science and Technology of China'])
    def test_pdf_abstract_and_keywords_do_not_include_footer_or_other_column(self):
        class Extraction:
            stdout = 'ABSTRACT\nA cost-\neffective system.\nCCS CONCEPTS\nNetworks\nKEYWORDS\nRDMA, Reliability\n†Work done while interns at Tencent.\nPermission to copy\n'
        with patch('complete_metadata.subprocess.run', return_value=Extraction()):
            result = pdf_fields({'cache_file': 'fixture.pdf'})
        self.assertEqual(result['abstract'], 'A cost-effective system.')
        self.assertEqual(result['keywords'], ['RDMA', 'Reliability'])

    def test_user_list_reconciles_exact_primary_paper_ids(self):
        papers = json.loads((ROOT / 'data/publications.json').read_text())['publications']
        checked = user_list(papers)
        self.assertFalse(any(r['status'] == 'unmatched_or_ambiguous' for r in checked))
        self.assertEqual(len([r for r in checked if r['paper_id']]), 32)
    def test_city_university_is_not_university_of_hong_kong(self):
        self.assertEqual([x[0] for x in institution_parts('City University of Hong Kong')], ['City University of Hong Kong'])

    def test_cuhk_shenzhen_is_not_cuhk_hong_kong(self):
        for raw in ['The Chinese University of Hong Kong, Shenzhen', 'The Chinese Universities of Hong Kong, Shenzhen, Shenzhen, China']:
            self.assertEqual([x[0] for x in institution_parts(raw)], ['Chinese University of Hong Kong, Shenzhen'])

    def test_unaffiliated_address_is_not_institution(self):
        self.assertEqual(institution_parts('Unaffiliated, Boston, USA')[0][0], '')
        self.assertEqual(institution_parts('Unaffiliated, Boston, USA')[0][3], 'explicit_none')

    def test_user_primary_metadata_complete_and_posters_separate(self):
        compact = metadata_tables(build_tables())
        self.assertEqual(len(compact['Publications']), 32)
        self.assertEqual(len(compact['Poster_Publications']), 2)
        for paper in compact['Publications']:
            self.assertTrue(paper['abstract'])
            self.assertTrue(paper['abstract_status'].startswith('complete_'))
            self.assertEqual(paper['metadata_status'], 'required_metadata_complete')
            self.assertIn(paper['affiliation_status'], ['pdf_verified', 'publisher_deposit_verified'])
        turbo = next(p for p in compact['Publications'] if p['title'].startswith('Turbo:'))
        self.assertNotIn('Corresponding', turbo['author_keywords'])
        self.assertNotIn('interns', turbo['author_keywords'])

    def test_dorado_prefers_publication_assignment_and_preserves_conflict(self):
        tables = build_tables()
        paper = next(p for p in tables['Publications'] if p['title'].startswith('Dorado:'))
        self.assertIn('program conflict', paper['metadata_notes'])
        lin = [a for a in tables['Author_Affiliations'] if a['paper_id'] == paper['paper_id'] and a['author_name'] == 'Guozhi Lin']
        self.assertEqual([a['institution'] for a in lin], ['University of Chinese Academy of Sciences'])

    def test_ledger_author_agreement_requires_complete_order(self):
        expected = [{"name": "Alice 0001"}, {"name": "Bob"}]
        self.assertTrue(author_agreement(expected, [{"name": "Alice"}, {"name": "Bob"}]))
        self.assertFalse(author_agreement(expected, [{"name": "Alice"}]))
        self.assertFalse(author_agreement(expected, [{"name": "Bob"}, {"name": "Alice"}]))

    def test_completeness_accounts_for_every_cell_and_known_paper(self):
        tables = build_tables()
        ledger = tables["Proceedings_Ledger"]
        self.assertEqual(len({p["ledger_id"] for p in ledger}), len(ledger))
        self.assertEqual({p["project_paper_id"] for p in ledger if p["project_paper_id"]},
                         {p["paper_id"] for p in tables["Publications"]})
        self.assertEqual(len(tables["Completeness"]), 40)
        self.assertEqual(sum(c["inventory_records"] for c in tables["Completeness"]), len(ledger))
        for cell in tables["Completeness"]:
            self.assertEqual(cell["inventory_records"], sum(cell[k] for k in ["tencent_confirmed_pdf", "tencent_supported_pdf_pending", "no_tencent_program_supported", "no_tencent_program_only", "no_tencent_pdf_screened", "unresolved"]))
            self.assertEqual(cell["affiliation_completeness"], "not_established")

    def test_reviewed_flexwan_title_variant_does_not_add_paper(self):
        rows = [p for p in build_tables()["Proceedings_Ledger"] if p["title"].startswith("FlexWAN:")]
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]["project_paper_id"])
        self.assertTrue(rows[0]["title_variant_review_required"])

    def test_grouped_usenix_authors_preserve_order(self):
        node = BeautifulSoup('<p>Alice, Bob, and Carol, <em>Tencent;</em> Dan, <em>University of Michigan</em></p>', 'html.parser')
        authors = usenix_authors(node)
        self.assertEqual([a['name'] for a in authors], ['Alice', 'Bob', 'Carol', 'Dan'])
        self.assertEqual(authors[1]['affiliations_raw'], ['Tencent'])

    def test_dual_usenix_affiliation(self):
        node = BeautifulSoup('<p>Alice, <em>Peking University and Tencent Inc.;</em> Bob, <em>Tencent</em></p>', 'html.parser')
        authors = usenix_authors(node)
        self.assertEqual(len(authors), 2)
        self.assertEqual({i[0] for i in institution_parts(authors[0]['affiliations_raw'][0])}, {'Peking University', 'Tencent'})

    def test_grouped_sigcomm_authors(self):
        authors = parenthetical_authors('Alice, Bob (Tencent); Carol (University of Michigan)')
        self.assertEqual([a['name'] for a in authors], ['Alice', 'Bob', 'Carol'])

    def test_and_within_institution_names(self):
        for institution in ['Hong Kong University of Science and Technology', 'Nanjing University of Science and Technology', 'Beijing University of Posts and Telecommunications']:
            self.assertEqual([i[0] for i in institution_parts(institution)], [institution])

    def test_comma_separated_multiple_institutions(self):
        result = institution_parts('Tsinghua University, Tencent Inc., and Beijing University of Posts and Telecommunications')
        self.assertEqual({i[0] for i in result}, {'Tsinghua University', 'Tencent', 'Beijing University of Posts and Telecommunications'})

    def test_longer_name_wins_over_nested_alias(self):
        self.assertEqual([i[0] for i in institution_parts('Chinese University of Hong Kong')], ['Chinese University of Hong Kong'])

    def test_explicit_unaffiliated_is_not_institution(self):
        self.assertEqual(institution_parts('Unaffiliated')[0][:3], ('', 'Unaffiliated', 'unaffiliated'))

    def test_audit_title_decodes_markup_and_punctuation(self):
        self.assertEqual(title_key('Don&apos;t Forget the User: It&apos;s Time'), title_key('Don’t Forget the User — It’s Time'))
        self.assertEqual(title_key('&lt;u&gt;un&lt;/u&gt;certainty'), title_key('uncertainty'))

    def test_cetc_is_industry_not_academic_partner(self):
        self.assertEqual(institution_parts('CETC')[0][::2], ('CETC', 'industry'))

    def test_annual_counts_separate_posters_and_scope_candidates(self):
        tables = build_tables()
        for row in tables['Annual_Stats']:
            records = [p for p in tables['Publications'] if (p['venue'], p['year']) == (row['venue'], row['year'])]
            self.assertEqual(row['posters'], sum(p['publication_type'] == 'poster' for p in records))
            self.assertEqual(row['primary_venue_records'], row['networking_scope_included'] + row['boundary_candidates'])
            self.assertEqual(row['primary_venue_records'] + row['posters'], len(records))

    def test_poster_preserves_raw_names_not_index_identity_errors(self):
        records = build_tables()['Publications']
        too = next(p for p in records if p['doi'] == '10.1145/3603269.3610841')
        self.assertEqual(too['publication_type'], 'poster')
        self.assertTrue(too['authors_ordered'].startswith('Xu Yan; Tong Li;'))
        self.assertIn('Haiyang Wang', too['authors_ordered'])
        self.assertEqual(too['author_list_check'], 'exact_order_match')


if __name__ == '__main__':
    unittest.main()
