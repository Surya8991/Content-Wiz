"""Review, output safety, configuration, and workspace regression tests."""
import contextlib
import csv
import io
import json
import os
import sys
import tempfile
import types
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import MagicMock, patch

import config
import generate
import llm
from test_generate import _single_run_args


class ReliabilityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stdout, self.stderr = io.StringIO(), io.StringIO()
        self.stack.enter_context(contextlib.redirect_stdout(self.stdout))
        self.stack.enter_context(contextlib.redirect_stderr(self.stderr))
        self.stack.enter_context(patch.dict(os.environ, {"CONTENT_WIZ_WORKSPACE": str(self.root)}))

    def tracker(self, rows):
        path = self.root / "tracker.csv"
        generate._write_tracker(path, ["File", "Status", "Reviewed By", "Review Date"], rows)
        self.stack.enter_context(patch.object(generate, "_publish_tracker_path", return_value=str(path)))
        return path

    def test_review_does_not_match_filename_suffix(self):
        path = self.tracker([{"File": "post.txt", "Status": "Draft"},
                             {"File": "other_post.txt", "Status": "Draft"}])
        self.assertEqual(generate.review_update("post.txt", "Approved", reviewer="Alice"), 0)
        rows = generate._read_tracker(path)[1]
        self.assertEqual([r["Status"] for r in rows], ["Approved", "Draft"])

    def test_ambiguous_basename_rejected_but_exact_path_accepted(self):
        path = self.tracker([{"File": "a/post.txt", "Status": "Draft"},
                             {"File": "b/post.txt", "Status": "Draft"}])
        before = path.read_bytes()
        self.assertEqual(generate.review_update("post.txt", "Approved", reviewer="Alice"), 1)
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(generate.review_update("a/post.txt", "Approved", reviewer="Alice"), 0)

    def test_publishing_requires_status_name_and_valid_date(self):
        for status, reviewer, date in [("Draft", "Alice", "2026-01-01"),
                                      ("Approved", "", "2026-01-01"),
                                      ("Approved", "Alice", "not-a-date")]:
            with self.subTest(status=status, reviewer=reviewer, date=date):
                path = self.tracker([{"File": "post.txt", "Status": status,
                                      "Reviewed By": reviewer, "Review Date": date}])
                before = path.read_bytes()
                self.assertEqual(generate.review_update("post.txt", "Published"), 1)
                self.assertEqual(path.read_bytes(), before)

    def test_approved_row_can_publish_and_reset_clears_review(self):
        path = self.tracker([{"File": "post.txt", "Status": "Draft"}])
        self.assertEqual(generate.review_update("post.txt", "Approved", reviewer="Alice"), 0)
        self.assertEqual(generate.review_update("post.txt", "Published"), 0)
        self.assertEqual(generate._read_tracker(path)[1][0]["Reviewed By"], "Alice")
        self.assertEqual(generate.review_update("post.txt", "Draft"), 0)
        row = generate._read_tracker(path)[1][0]
        self.assertEqual((row["Reviewed By"], row["Review Date"]), ("", ""))

    def test_html_code_and_raw_markup_remain_literal(self):
        raw = '```\n<script>alert(1)</script>\n```\n\n<img src=x onerror=alert(1)>\n\n`<b>&</b>`'
        blocks = json.loads(generate._to_gutenberg(raw))["blocks"]
        markup = "".join(b["innerHTML"] for b in blocks)
        self.assertNotIn("<script>", markup)
        self.assertNotIn("<img ", markup)
        self.assertIn("&lt;script&gt;", markup)
        self.assertIn("<code>&lt;b&gt;&amp;&lt;/b&gt;</code>", markup)

    def test_urls_and_image_attributes_cannot_inject_html(self):
        for url in ("javascript:alert", "java&#115;cript:alert", "data:text/html,test", "java\nscript:alert"):
            with self.subTest(url=url):
                self.assertIsNone(generate._safe_html_url(url))
                self.assertNotIn("<a ", generate._md_inline_to_html(f"[click]({url})"))
        raw = '![a" onerror="bad](https://example.com/a" onload="bad)'
        markup = json.loads(generate._to_gutenberg(raw))["blocks"][0]["innerHTML"]
        class Tags(HTMLParser):
            def handle_starttag(self, tag, attrs):
                if tag == "img":
                    self.attrs = dict(attrs)
        parser = Tags()
        parser.feed(markup)
        self.assertEqual(set(parser.attrs), {"src", "alt"})
        self.assertNotIn("<img", generate._to_gutenberg("![alt](javascript:bad)"))

    def test_safe_markdown_still_renders(self):
        result = generate._md_inline_to_html('**bold** *italic* [link](https://example.com?a=1&b=2)')
        self.assertIn("<strong>bold</strong>", result)
        self.assertIn("<em>italic</em>", result)
        self.assertIn('href="https://example.com?a=1&amp;b=2"', result)

    def test_cluster_failure_records_error_and_separates_prompt(self):
        source = self.root / "clusters.csv"
        source.write_text("cluster_id,primary_keyword,supporting_keywords\nc1,main,child\n", encoding="utf-8")
        args = _single_run_args(keyword_cluster=str(source), output_dir=str(self.root / "output"),
                                generate=True, dry_run=False)
        with patch("llm.generate_content", side_effect=[RuntimeError("API unavailable"), "Finished child"]):
            with self.assertRaises(SystemExit) as raised:
                generate.run_keyword_cluster(args)
        self.assertEqual(raised.exception.code, 2)
        folder = self.root / "output" / "Keyword_Clusters"
        fallback = next((folder / "failed_prompts").glob("*.prompt.txt"))
        self.assertTrue(fallback.read_text(encoding="utf-8").startswith("GENERATION FAILED - PROMPT ONLY"))
        failures = json.loads(next(folder.glob("failures_*.json")).read_text(encoding="utf-8"))
        self.assertEqual(failures[0]["role"], "pillar")
        self.assertEqual(len(failures), 1)
        self.assertFalse(list(folder.glob("*pillar*")))
        self.assertIn("Finished child", [p.read_text(encoding="utf-8") for p in folder.glob("*.*")])
        self.assertNotIn(fallback.name, next(folder.glob("*manifest.txt")).read_text(encoding="utf-8"))

    def test_invalid_config_reports_field_and_uses_independent_fallback(self):
        cases = [([], "config"), ({"defaults": None}, "defaults"),
                 ({"brands": []}, "brands"), ({"defaults": {"llm_max_tokens": -1}}, "llm_max_tokens"),
                 ({"defaults": {"llm_models": []}}, "llm_models"),
                 ({"defaults": {"llm_pricing": {"local": {"": {"input": -1, "output": 0}}}}}, "input"),
                 ({"brands": {"example.com": {"market": "invalid"}}}, "market"),
                 ({"brands": {"example.com": {"platform_audience_overrides": {"blog": 42}}}}, "blog")]
        path = self.root / "config.json"
        for data, field in cases:
            with self.subTest(field=field), patch.object(config, "_CONFIG_PATH", str(path)):
                path.write_text(json.dumps(data), encoding="utf-8")
                self.stderr.seek(0)
                self.stderr.truncate()
                result = config.load()
                self.assertEqual(result, config._FALLBACK)
                self.assertIsNot(result, config._FALLBACK)
                self.assertIn(field, self.stderr.getvalue())

    def test_workspace_controls_inputs_outputs_and_tracker(self):
        source = self.root / "source.md"
        source.write_text("Source material", encoding="utf-8")
        self.assertEqual(generate.default_output_dir(), str(self.root / "output"))
        self.assertEqual(generate._resolve_contained_path("source.md"), source.resolve())
        self.assertIsNone(generate._resolve_contained_path("../outside.md"))
        args = _single_run_args(platform="twitter", repurpose="source.md", dry_run=False, log_publish=True)
        generate.run_single(args)
        self.assertTrue(list((self.root / "output").rglob("*.*")))
        tracker = Path(generate._publish_tracker_path())
        self.assertEqual(tracker.parent, self.root / "data")
        with tracker.open(encoding="utf-8", newline="") as stream:
            self.assertEqual(next(csv.DictReader(stream))["Status"], "Draft")

    def test_bulk_rejects_unsupported_options_before_execution(self):
        options = [("--tone", "formal"), ("--language", "German"), ("--locale", "de"),
                   ("--voice-samples", "voice.txt"), ("--log-publish",), ("--variants", "2"),
                   ("--keywords", "words.txt"), ("--with-image-brief",),
                   ("--fetch-competitors", "https://example.com"), ("--audience", "Readers"),
                   ("--wordcount", "1000"), ("--url", "https://example.com")]
        for option in options:
            with self.subTest(option=option), patch.object(sys, "argv", ["generate", "--bulk", "batch.csv", *option]):
                with patch.object(generate, "run_bulk") as run, self.assertRaises(SystemExit) as raised:
                    generate.main()
                self.assertEqual(raised.exception.code, 2)
                run.assert_not_called()
                self.assertIn(option[0], self.stderr.getvalue())


class CompletionTests(unittest.TestCase):
    def test_anthropic_rejects_nonempty_truncated_response(self):
        client = MagicMock()
        client.messages.create.return_value = types.SimpleNamespace(
            content=[types.SimpleNamespace(type="text", text="Partial")], stop_reason="max_tokens")
        with patch.dict(sys.modules, {"anthropic": types.SimpleNamespace(Anthropic=lambda **kwargs: client)}):
            with self.assertRaises(llm.IncompleteResponseError):
                llm._generate_anthropic("p", "key", "model", 10)

    def test_gemini_rejects_nonempty_truncated_response(self):
        client = MagicMock()
        client.models.generate_content.return_value = types.SimpleNamespace(
            candidates=[types.SimpleNamespace(finish_reason=types.SimpleNamespace(name="MAX_TOKENS"))], text="Partial")
        fake_types = types.SimpleNamespace(GenerateContentConfig=MagicMock())
        genai = types.SimpleNamespace(Client=lambda **kwargs: client, types=fake_types)
        with patch.dict(sys.modules, {"google": types.SimpleNamespace(genai=genai),
                                     "google.genai": genai, "google.genai.types": fake_types}):
            with self.assertRaises(llm.IncompleteResponseError):
                llm._generate_gemini("p", "key", "model", 10)

    def test_openai_and_local_reject_nonempty_truncated_responses(self):
        client = MagicMock()
        client.chat.completions.create.return_value = types.SimpleNamespace(choices=[
            types.SimpleNamespace(message=types.SimpleNamespace(content="Partial"), finish_reason="length")])
        with patch.dict(sys.modules, {"openai": types.SimpleNamespace(OpenAI=lambda **kwargs: client)}):
            for handler in (llm._generate_openai, llm._generate_local):
                with self.subTest(handler=handler.__name__), self.assertRaises(llm.IncompleteResponseError):
                    handler("p", "key", "model", 10)

    def test_incomplete_response_is_not_retried(self):
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test"}), patch.object(
                llm, "_generate_anthropic", side_effect=llm.IncompleteResponseError("truncated")) as handler:
            with self.assertRaises(llm.IncompleteResponseError):
                llm.generate_content("p", provider="anthropic")
        self.assertEqual(handler.call_count, 1)


if __name__ == "__main__":
    unittest.main()
