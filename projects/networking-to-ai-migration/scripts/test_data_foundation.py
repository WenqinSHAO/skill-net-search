#!/usr/bin/env python3
"""Regression checks for foundational data-scope and zone-classification rules."""

from publication_scope import annotate_scope
from classify_zones import classify_paper


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def test_scope_exclusions():
    cases = [
        ({"title": "A journal paper", "venue": "IEEE/ACM Trans. Netw.", "is_journal": True}, "journal_article"),
        ({"title": "An arXiv paper", "venue": "CoRR"}, "venue:CoRR"),
        ({"title": "Proceedings of a Conference", "venue": "ASPLOS"}, "proceedings_volume"),
        ({"title": "IMC '21: ACM Internet Measurement Conference, Virtual Event, USA, November 2-4, 2021", "venue": "Internet Measurement Conference", "record_type": "inproceedings", "authors": []}, "proceedings_volume"),
        ({"title": "HotNets '20: The 19th ACM Workshop on Hot Topics in Networks, Virtual Event, USA, November 4-6, 2020", "venue": "HotNets", "record_type": "inproceedings", "authors": []}, "proceedings_volume"),
        ({"title": "No venue"}, "missing_venue"),
        ({"title": "A thesis", "venue": "University", "record_type": "phdthesis"}, "record_type:phdthesis"),
    ]
    for paper, reason in cases:
        annotate_scope(paper)
        assert_equal(paper["included_in_analysis"], False, reason)
        assert_equal(paper["exclusion_reason"], reason, reason)


def test_systems_venue_needs_ai_signal_for_zone2():
    generic = {
        "title": "Automatically Reasoning About How Systems Code Uses the CPU Cache",
        "venue": "OSDI",
        "record_type": "inproceedings",
    }
    assert_equal(classify_paper(generic), "Unclassified", "generic systems venue")

    ai_infra = {
        "title": "POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference",
        "venue": "OSDI",
        "record_type": "inproceedings",
    }
    assert_equal(classify_paper(ai_infra), "Zone 2", "AI infra systems paper")


def test_unknown_no_signal_is_unclassified():
    paper = {
        "title": "A Study of Something Without Useful Keywords",
        "venue": "Some New Venue",
        "record_type": "inproceedings",
    }
    assert_equal(classify_paper(paper), "Unclassified", "unknown no-signal venue")


def test_ai_venue_with_infra_signal_can_be_zone2():
    paper = {
        "title": "Efficient KV Cache Offloading for LLM Serving",
        "venue": "ICML",
        "record_type": "inproceedings",
    }
    assert_equal(classify_paper(paper), "Zone 2", "AI venue infra override")


if __name__ == "__main__":
    test_scope_exclusions()
    test_systems_venue_needs_ai_signal_for_zone2()
    test_unknown_no_signal_is_unclassified()
    test_ai_venue_with_infra_signal_can_be_zone2()
    print("data foundation checks passed")
