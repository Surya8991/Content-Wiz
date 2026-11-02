"""Regression coverage for generation preflight, batch failures, and output safety."""
import contextlib
import csv
import io
import tempfile
import unittest
import zipfile
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import generate
from test_generate import _single_run_args


class ExecutionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.out = self.root / "out"
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
        self.stack.enter_context(contextlib.redirect_stderr(io.StringIO()))
        self.provider = self.stack.enter_context(patch("llm.generate_content", return_value="Finished content"))

    def cluster_args(self, **overrides):
        source = self.root / "cluster.csv"
        source.write_text("cluster_id,primary_keyword,supporting_keywords\nc1,main,child\n", encoding="utf-8")
        options = dict(keyword_cluster=str(source), output_dir=str(self.out), generate=True, dry_run=False)
        options.update(overrides)
        return _single_run_args(**options)

    def bulk_csv(self, rows=None):
        source = self.root / "bulk.csv"
        source.write_text(rows or "platform,topic\nfaq,one\nfaq,two\n", encoding="utf-8")
        return str(source)

    def test_cluster_dry_run_has_no_calls_or_files(self):
        generate.run_keyword_cluster(self.cluster_args(dry_run=True))
        self.provider.assert_not_called()
        self.assertFalse(self.out.exists())

    def test_cluster_budget_checks_total_before_any_call(self):
        with patch("llm.estimate_cost_usd", return_value=(0.6, {})), self.assertRaises(SystemExit) as raised:
            generate.run_keyword_cluster(self.cluster_args(budget_cap=1.0))
        self.assertEqual(raised.exception.code, 3)
        self.provider.assert_not_called()
        self.assertFalse(self.out.exists())

    def test_cluster_unknown_pricing_blocks_generation(self):
        with patch("llm.estimate_cost_usd", return_value=(None, {})), self.assertRaises(SystemExit) as raised:
            generate.run_keyword_cluster(self.cluster_args(budget_cap=100))
        self.assertEqual(raised.exception.code, 3)
        self.provider.assert_not_called()

    def test_cluster_normal_generation_writes_posts_and_manifest(self):
        generate.run_keyword_cluster(self.cluster_args())
        self.assertEqual(self.provider.call_count, 2)
        files = list(self.out.rglob("*.*"))
        self.assertEqual(len(files), 3)
        self.assertEqual(sum(p.read_text(encoding="utf-8") == "Finished content" for p in files), 2)

    def test_single_zero_cap_is_enforced_without_estimate_flag(self):
        args = _single_run_args(generate=True, dry_run=False, budget_cap=0, output_dir=str(self.out))
        with patch("llm.estimate_cost_usd", return_value=(0.01, {})), self.assertRaises(SystemExit) as raised:
            generate.run_single(args)
        self.assertEqual(raised.exception.code, 3)
        self.provider.assert_not_called()
        self.assertFalse(self.out.exists())

    def test_single_unknown_pricing_blocks_generation(self):
        args = _single_run_args(generate=True, dry_run=False, budget_cap=100, output_dir=str(self.out))
        with patch("llm.estimate_cost_usd", return_value=(None, {})), self.assertRaises(SystemExit):
            generate.run_single(args)
        self.provider.assert_not_called()

    def test_budget_rejects_invalid_values(self):
        for cap in (-1, float("nan"), float("inf")):
            with self.subTest(cap=cap), self.assertRaises(SystemExit) as raised:
                generate._preflight_cost(["prompt"], cap=cap)
            self.assertEqual(raised.exception.code, 3)

    def test_single_variants_are_all_budgeted(self):
        args = _single_run_args(generate=True, dry_run=False, budget_cap=1, variants=2, output_dir=str(self.out))
        with patch("llm.estimate_cost_usd", return_value=(0.6, {})) as estimate, self.assertRaises(SystemExit):
            generate.run_single(args)
        self.assertEqual(estimate.call_count, 2)
        self.assertIn("VARIANT 2 OF 2", estimate.call_args.args[0])
        self.provider.assert_not_called()

    def test_bulk_estimates_each_actual_prompt(self):
        with patch("llm.estimate_cost_usd", side_effect=[(0.1, {}), (2.0, {})]) as estimate:
            with self.assertRaises(SystemExit) as raised:
                generate.run_bulk(self.bulk_csv(), str(self.out), generate_content=True, budget_cap=1)
        self.assertEqual(raised.exception.code, 3)
        self.assertEqual(estimate.call_count, 2)
        self.assertNotEqual(estimate.call_args_list[0].args[0], estimate.call_args_list[1].args[0])
        self.provider.assert_not_called()
        self.assertFalse(self.out.exists())

    def test_bulk_unknown_pricing_blocks_generation(self):
        with patch("llm.estimate_cost_usd", return_value=(None, {})), self.assertRaises(SystemExit):
            generate.run_bulk(self.bulk_csv(), str(self.out), generate_content=True, budget_cap=100)
        self.provider.assert_not_called()
        self.assertFalse(self.out.exists())

    def test_bulk_unexpected_failures_are_logged_and_exit_nonzero(self):
        self.provider.side_effect = ValueError("simulated SDK failure")
        for workers in (1, 2):
            output = self.root / str(workers)
            with self.subTest(workers=workers), self.assertRaises(SystemExit) as raised:
                generate.run_bulk(self.bulk_csv(), str(output), generate_content=True, parallel=workers)
            self.assertEqual(raised.exception.code, 2)
            with next(output.glob("log*.csv")).open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 2)
            self.assertTrue(all("simulated SDK failure" in row["status"] for row in rows))

    def test_bulk_generated_scheduler_export_contains_payload(self):
        payload = 'Finished content, with commas\nand "quotes"'
        self.provider.return_value = payload
        generate.run_bulk(self.bulk_csv(), str(self.out), generate_content=True, parallel=2,
                          scheduler_format="buffer")
        with next(self.out.glob("buffer*.csv")).open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual([r["Text"] for r in rows], [payload, payload])
        with zipfile.ZipFile(next(self.out.glob("*.zip"))) as archive:
            self.assertEqual(len(archive.namelist()), 2)
            self.assertIsNone(archive.testzip())

    def test_scheduler_does_not_export_prompts_or_errors(self):
        self.out.mkdir()
        rows = [{"status": status, "filename": "x"} for status in ("ok", "error: failed")]
        path = generate.export_buffer_csv(rows, str(self.out), {"x": "prompt instructions"})
        with open(path, encoding="utf-8", newline="") as stream:
            self.assertEqual(list(csv.DictReader(stream)), [])

    def test_bulk_text_prompt_preserves_brand_url(self):
        source = self.bulk_csv("platform,topic,url\nwhitepaper,test,https://example.com\n")
        generate.run_bulk(source, str(self.out))
        with zipfile.ZipFile(next(self.out.glob("*.zip"))) as archive:
            prompt = archive.read(archive.namelist()[0]).decode("utf-8")
        self.assertIn("Brand URL: https://example.com", prompt)

    def test_repeated_single_runs_in_same_second_preserve_both_outputs(self):
        args = _single_run_args(platform="faq", dry_run=False, output_dir=str(self.out))
        with patch("generate.datetime") as clock:
            clock.now.return_value = datetime(2026, 1, 1)
            generate.run_single(args)
            args.topic = "Different topic"
            generate.run_single(args)
        files = list(self.out.rglob("*.*"))
        self.assertEqual(len(files), 2)
        self.assertNotEqual(files[0].read_text(encoding="utf-8"), files[1].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
