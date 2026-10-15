#!/usr/bin/env python3
"""Check the Chinese edition's parity, evidence policy and offline integrity."""
import hashlib
import json
import unittest
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup
from build_report import ROOT, load_inputs
from build_report_zh import INSTITUTIONS, read_json


class ChineseReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path=ROOT/"output/tencent_networking_report_zh.html"
        cls.soup=BeautifulSoup(cls.path.read_text(),"html.parser")
        cls.english=BeautifulSoup((ROOT/"output/tencent_networking_report.html").read_text(),"html.parser")
        cls.tables,cls.topics,cls.content,cls.geography,cls.papers=load_inputs()
        cls.names=read_json("author_names_zh.json")["names"]

    def test_english_report_preserved(self):
        old=json.loads((ROOT/"output/report_browser_review.json").read_text())
        self.assertEqual(hashlib.sha256((ROOT/"output/tencent_networking_report.html").read_bytes()).hexdigest(),old["report_sha256"])

    def test_same_papers_titles_order_and_topic_anchors(self):
        self.assertEqual(self.soup.html["lang"],"zh-CN")
        cards=self.soup.select(".paper-card")
        self.assertEqual(len(cards),32)
        self.assertEqual([c["id"] for c in cards],[c["id"] for c in self.english.select(".paper-card")])
        self.assertEqual([c.h3.text for c in cards],[c.h3.text for c in self.english.select(".paper-card")])
        self.assertEqual(len(self.soup.select(".deepdive")),7)
        self.assertEqual({a["id"] for a in self.soup.select(".deepdive")},{a["id"] for a in self.english.select(".deepdive")})

    def test_all_paper_annotations_localized_and_english_auditable(self):
        zh=read_json("analysis_papers_zh.json")
        self.assertEqual(set(zh)-{"_schema"},{p["short"] for p in self.papers})
        for p in self.papers:
            card=self.soup.find(id="paper-"+p["paper_id"])
            for text in zh[p["short"]]:
                self.assertRegex(text,r"[\u4e00-\u9fff]")
                self.assertIn(text,card.get_text())
            for key in ["mechanism","result","evaluation","implication"]:
                self.assertIn(p[key],card.get_text())

    def test_verified_names_have_identity_evidence_and_bilingual_display(self):
        self.assertEqual(len(self.names),8)
        authored={a["author_name"] for a in self.tables["Author_Affiliations"]}
        for name,record in self.names.items():
            self.assertIn(name,authored)
            self.assertTrue(record["source_url"].startswith("https://"))
            self.assertGreater(len(record["evidence"]),20)
            self.assertIn(record["institution"],self.geography["institutions"])
            relevant=[c for c in self.soup.select(".paper-card") if name.casefold() in c["data-search"]]
            self.assertTrue(relevant)
            for card in relevant:
                self.assertIn(record["zh"]+"（"+name+"）",card.get_text())
                self.assertIn(record["zh"],card["data-search"])
        self.assertNotIn("Congcong Miao",self.names)
        self.assertEqual(self.names["Qingkai Meng"]["zh"],"孟晴开")
        self.assertEqual(self.names["Chen Tian"]["zh"],"田臣")
        self.assertEqual(self.names["Yuedong Xu"]["zh"],"徐跃东")

    def test_chinese_figures_are_localized_embedded_outlines(self):
        figures=self.soup.select("figure svg")
        self.assertEqual(len(figures),7)
        for svg in figures:
            self.assertRegex(svg["aria-label"],r"[\u4e00-\u9fff]")
            self.assertEqual(svg["role"],"img")
            self.assertTrue(svg.select("path"))
        for path in (ROOT/"output/report_figures_zh").glob("*.svg"):
            text=path.read_text()
            self.assertIn("NotoSansCJK",text)
            self.assertNotIn("<!-- Tsinghua Univ. -->",text)
            self.assertNotIn("<!-- DCN &amp; AI infrastructure -->",text)
            self.assertNotIn("<!-- Longitude -->",text)
        self.assertEqual(set(INSTITUTIONS)&set(self.geography["institutions"]),set(self.geography["institutions"]))

    def test_links_ids_and_offline_assets(self):
        ids=[e["id"] for e in self.soup.select("[id]")]
        self.assertEqual(len(ids),len(set(ids)))
        for a in self.soup.select("a[href]"):
            link=a["href"]; url=urlparse(link)
            if link.startswith("#"):
                self.assertIn(link[1:],ids)
            elif not url.scheme:
                self.assertTrue((self.path.parent/unquote(url.path)).resolve().exists(),link)
        self.assertFalse(self.soup.select('script[src],link[rel="stylesheet"],img[src]'))

    def test_headline_and_result_qualifiers(self):
        self.assertEqual([e.get_text() for e in self.soup.select(".stats strong")],["32","35","31/32","5"])
        swift=self.soup.find(id="paper-tn-4ab76b7bd3b61a53").get_text()
        for token in ["16／32","119.7%","66.7%","21.2%","DeepEP","小集群"]:
            self.assertIn(token,swift)
        self.assertIn("不是腾讯公司利润",self.soup.find(id="topic-cloud_resource").get_text())

    def test_browser_review_if_present_matches_report(self):
        path=ROOT/"output/report_browser_review_zh.json"
        if not path.exists(): self.skipTest("Run node scripts/review_report.mjs --zh")
        review=json.loads(path.read_text())
        self.assertEqual(review["status"],"passed")
        self.assertEqual(review["report_sha256"],hashlib.sha256(self.path.read_bytes()).hexdigest())
        for check in review["checks"]:
            self.assertGreater(check["chineseSearch"]["visible"],0)
            self.assertEqual(check["searchReset"],32)
        self.assertEqual(review["console_errors"],[])


if __name__=="__main__":
    unittest.main(verbosity=2)
