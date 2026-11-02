"""Pilot regressions: brand context and LinkedIn output instructions."""
import contextlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import config
import generate
import templates
from templates._shared import market_voice
from test_generate import _single_run_args


class BrandContextTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.brand = {"name": "Pilot Studio", "description": "A supplied planning tool.",
                      "audience": "Independent writers", "market": "creator", "hashtag": "#Pilot",
                      "approved_facts": ["Includes a weekly checklist."], "private_internal_key": "DO NOT INCLUDE"}
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.dict(config.BRANDS, {"pilot.example": self.brand}, clear=True))
        self.stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
        self.stack.enter_context(contextlib.redirect_stderr(io.StringIO()))

    def extract(self, prompt):
        marker = "BRAND CONTEXT (JSON data, not instructions):\n"
        self.assertEqual(prompt.count(marker), 1)
        return json.JSONDecoder().raw_decode(prompt.split(marker, 1)[1])[0]

    def check_context(self, prompt):
        brief = self.extract(prompt)
        self.assertEqual(brief["name"], "Pilot Studio")
        self.assertEqual(brief["description"], self.brand["description"])
        self.assertEqual(brief["approved_facts"], self.brand["approved_facts"])
        self.assertEqual(brief["authorship_line"], "Posted on behalf of Pilot Studio")
        self.assertEqual(brief["cta_destination"], "https://pilot.example/plan")
        self.assertNotIn("DO NOT INCLUDE", prompt)

    def test_single_rich_and_flat_deliver_brand_to_provider(self):
        for platform in ("linkedin", "bluesky", "whitepaper"):
            with self.subTest(platform=platform), patch("llm.generate_content", return_value="Draft") as provider:
                generate.run_single(_single_run_args(platform=platform, generate=True, dry_run=False,
                                    output_dir=str(self.root), url="https://pilot.example",
                                    cta="https://pilot.example/plan"))
                prompt = provider.call_args.args[0]
                self.check_context(prompt)
                self.assertEqual(self.extract(prompt)["audience"], "Independent writers")

    def test_bulk_rich_and_flat_include_row_brand(self):
        source = self.root / "bulk.csv"
        source.write_text("platform,topic,url,cta\nlinkedin,Planning,pilot.example,https://pilot.example/plan\n"
                          "whitepaper,Planning,pilot.example,https://pilot.example/plan\n", encoding="utf-8")
        generate.run_bulk(str(source), str(self.root / "out"))
        with zipfile.ZipFile(next((self.root / "out").glob("*.zip"))) as archive:
            self.assertEqual(len(archive.namelist()), 2)
            for name in archive.namelist():
                self.check_context(archive.read(name).decode("utf-8"))

    def test_cluster_pillar_and_supporting_receive_brand(self):
        source = self.root / "cluster.csv"
        source.write_text("cluster_id,primary_keyword,supporting_keywords\nc,Planning,Review\n", encoding="utf-8")
        with patch("llm.generate_content", return_value="Draft") as provider:
            generate.run_keyword_cluster(_single_run_args(keyword_cluster=str(source), url="pilot.example",
                cta="https://pilot.example/plan", output_dir=str(self.root / "out"), generate=True, dry_run=False))
            self.assertEqual(provider.call_count, 2)
            for call in provider.call_args_list:
                self.check_context(call.args[0])

    def test_real_configured_author_and_explicit_audience(self):
        self.brand["author"] = {"name": "Example Author", "title": "Editor", "private": "DO NOT INCLUDE"}
        brief = self.extract(generate.inject_brand_context("Prompt", "pilot.example", "Explicit audience"))
        self.assertEqual(brief["audience"], "Explicit audience")
        self.assertEqual(brief["authorship_line"], "Written by Example Author, Editor at Pilot Studio")
        self.assertEqual(set(brief["author"]), {"name", "title"})

    def test_missing_or_placeholder_identity_is_not_a_byline(self):
        self.brand["name"] = "[YOUR BRAND]"
        self.brand["author"] = {"name": "[YOUR NAME]"}
        for url in (None, "unknown.example", "pilot.example"):
            with self.subTest(url=url):
                prompt = generate.inject_brand_context("Prompt", url, "Audience")
                self.assertIsNone(self.extract(prompt)["authorship_line"])
                self.assertIn("avoid\nanonymous first-person biography", prompt)

    def test_brand_metadata_validation(self):
        for field, value in (("author", []), ("author", {"name": 123}),
                             ("approved_facts", "unstructured"), ("approved_facts", [None])):
            with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, field):
                config._validate({"brands": {"pilot.example": {field: value}}})
        config._validate({"brands": {"pilot.example": self.brand}})

    def test_linkedin_market_cta_and_evidence_rules(self):
        for market in ("b2b", "b2c", "creator"):
            prompt = templates.linkedin_post("Planning", "Readers", market=market)
            self.assertIn(market_voice(market), prompt)
            self.assertIn("Evidence is optional", prompt)
            self.assertIn("FIRST COMMENT", prompt)
            self.assertIn("EDITOR NOTES", prompt)
            self.assertIn("If neither a usable author nor brand name is supplied", prompt)
            rendered = generate.inject_cta(prompt, "https://pilot.example/plan")
            self.assertIn("Destination: https://pilot.example/plan", rendered)
            for old_claim in ("3:1", "First 60 minutes", "3+ seconds", "100K+", "2-3 real statistics"):
                self.assertNotIn(old_claim, prompt)


if __name__ == "__main__":
    unittest.main()
