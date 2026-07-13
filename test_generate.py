"""Smoke tests for the prompt generator.

Run: python -m unittest test_generate -v

These guard against signature drift between generate.py's PLATFORM_MAP and
the templates/ package: every routed platform must resolve to a template,
render a non-empty prompt, and route to a declared output subfolder.
"""
import unittest

import generate
import templates

SAMPLE = {
    "topic": "leadership training",
    "audience": generate.DEFAULT_AUDIENCE,
    "wordcount": generate.DEFAULT_WORDCOUNT,
    "platform_label": "test",
    "platform_target": None,
}


class PlatformRoutingTests(unittest.TestCase):
    def test_every_alias_resolves_to_a_template(self):
        for alias, key in generate.PLATFORM_MAP.items():
            with self.subTest(alias=alias):
                if key == "medium":
                    self.assertTrue(hasattr(templates, "medium_step1"))
                    self.assertTrue(hasattr(templates, "medium_step2"))
                else:
                    self.assertTrue(
                        hasattr(templates, key),
                        f"alias '{alias}' -> key '{key}' has no template function",
                    )

    def test_every_key_renders_non_empty_prompt(self):
        for key in set(generate.PLATFORM_MAP.values()):
            with self.subTest(key=key):
                kwargs = dict(SAMPLE)
                if key == "repurpose":
                    kwargs["source_content"] = "Some source content to repurpose."
                    kwargs["from_platform"] = "blog"
                prompt = generate.build_prompt(key, **kwargs)
                self.assertIsInstance(prompt, str)
                self.assertGreater(len(prompt.strip()), 50)

    def test_medium_step1_and_step2(self):
        step1 = generate.build_prompt("medium", **SAMPLE)
        self.assertGreater(len(step1.strip()), 50)
        step2 = generate.build_prompt("medium", title="A Chosen Title", **SAMPLE)
        self.assertGreater(len(step2.strip()), 50)
        self.assertNotEqual(step1, step2)

    def test_every_writable_key_has_a_subfolder(self):
        # Every routed key that produces a file must map to a real subfolder
        # (PRINT_ONLY keys write nothing, but still declare one for the bulk ZIP).
        for key in set(generate.PLATFORM_MAP.values()):
            with self.subTest(key=key):
                self.assertIn(key, generate.SUBFOLDER_MAP,
                              f"key '{key}' has no SUBFOLDER_MAP entry")

    def test_no_em_dashes_in_rendered_prompts(self):
        for key in set(generate.PLATFORM_MAP.values()):
            with self.subTest(key=key):
                kwargs = dict(SAMPLE)
                if key == "repurpose":
                    kwargs["source_content"] = "Some source content."
                    kwargs["from_platform"] = "blog"
                prompt = generate.build_prompt(key, **kwargs)
                self.assertNotIn("—", prompt, f"em-dash leaked into '{key}' output")


class CtaPlaceholderPresenceTests(unittest.TestCase):
    def test_livejournal_post_contains_cta_placeholder(self):
        self.assertIn("[INSERT CTA LINK]", generate.build_prompt("livejournal_post", **SAMPLE))

    def test_tumblr_post_contains_cta_placeholder(self):
        self.assertIn("[INSERT CTA LINK]", generate.build_prompt("tumblr_post", **SAMPLE))

    def test_short_form_video_contains_cta_placeholder(self):
        self.assertIn("[INSERT CTA LINK]", generate.build_prompt("short_form_video", **SAMPLE))

    def test_landing_page_contains_cta_placeholder(self):
        self.assertIn("[INSERT CTA LINK]", generate.build_prompt("landing_page", **SAMPLE))


class CtaInjectionTests(unittest.TestCase):
    def test_cta_replaces_placeholder(self):
        out = generate.inject_cta("Visit [INSERT CTA LINK] now", "https://edstellar.com")
        self.assertIn("https://edstellar.com", out)
        self.assertNotIn("[INSERT CTA LINK]", out)

    def test_cta_none_is_noop(self):
        text = "Visit [INSERT CTA LINK] now"
        self.assertEqual(generate.inject_cta(text, None), text)


class ResolveTests(unittest.TestCase):
    def test_template_alias_resolves_to_template(self):
        kind, ref = generate.resolve("faq")
        self.assertEqual(kind, "template")
        self.assertEqual(ref, "faq")

    def test_text_alias_resolves_to_text(self):
        kind, ref = generate.resolve("buyer_persona")
        self.assertEqual(kind, "text")
        self.assertEqual(ref, "buyer_persona")

    def test_unknown_alias_resolves_to_none(self):
        self.assertEqual(generate.resolve("definitely_not_a_platform"), (None, None))

    def test_no_alias_collision_between_maps(self):
        import textprompts
        overlap = set(generate.PLATFORM_MAP) & set(textprompts.TEXT_PROMPT_MAP)
        self.assertEqual(overlap, set(), f"aliases in both maps: {overlap}")


class TextPromptTests(unittest.TestCase):
    def setUp(self):
        import textprompts
        self.textprompts = textprompts

    def test_every_registered_prompt_file_exists(self):
        import os
        for alias, (fname, _folder) in self.textprompts.TEXT_PROMPT_MAP.items():
            with self.subTest(alias=alias):
                path = os.path.join(self.textprompts.PROMPTS_DIR, fname)
                self.assertTrue(os.path.isfile(path), f"missing prompt file: {fname}")

    def test_render_substitutes_topic_and_audience(self):
        out = self.textprompts.render(
            "buyer_persona", topic="ZZTOPIC", audience="ZZAUDIENCE",
        )
        self.assertIn("ZZTOPIC", out)
        self.assertIn("ZZAUDIENCE", out)

    def test_render_leaves_brand_tokens_intact(self):
        # Find any registered text prompt that uses a [BRAND ...] token and
        # confirm rendering preserves it (brand detection is the LLM's job).
        import os
        aliases_with_brand = []
        for alias, (fname, _f) in self.textprompts.TEXT_PROMPT_MAP.items():
            path = os.path.join(self.textprompts.PROMPTS_DIR, fname)
            with open(path, encoding="utf-8") as fh:
                if "[BRAND" in fh.read():
                    aliases_with_brand.append(alias)
                    break
        if not aliases_with_brand:
            self.skipTest("no text prompt uses a [BRAND ...] token")
        out = self.textprompts.render(aliases_with_brand[0], topic="t", audience="a")
        self.assertIn("[BRAND", out)

    def test_no_em_dash_in_rendered_text_prompts(self):
        seen = set()
        for alias, (fname, _f) in self.textprompts.TEXT_PROMPT_MAP.items():
            if fname in seen:
                continue
            seen.add(fname)
            out = self.textprompts.render(alias, topic="t", audience="a")
            self.assertNotIn("—", out, f"em-dash in {fname}")


class ConfigTests(unittest.TestCase):
    def test_defaults_present(self):
        from config import DEFAULTS
        for key in ("audience", "wordcount", "llm_model", "llm_max_tokens"):
            self.assertIn(key, DEFAULTS)

    def test_brand_lookup_by_url(self):
        import config
        brand = config.brand_for_url("https://www.edstellar.com/blog/x")
        self.assertIsNotNone(brand)
        self.assertEqual(brand["name"], "Edstellar")

    def test_brand_lookup_unknown_returns_none(self):
        import config
        self.assertIsNone(config.brand_for_url("https://example.com"))

    def test_platform_override_wins_when_present(self):
        import config
        brand = config.BRANDS["edstellar.com"]
        result = config.audience_for_platform(brand, "livejournal")
        self.assertEqual(result, brand["platform_audience_overrides"]["livejournal"])

    def test_platform_override_falls_back_to_brand_audience(self):
        import config
        brand = config.BRANDS["edstellar.com"]
        result = config.audience_for_platform(brand, "some_platform_with_no_override")
        self.assertEqual(result, brand["audience"])

    def test_platform_override_no_platform_key_falls_back(self):
        import config
        brand = config.BRANDS["edstellar.com"]
        self.assertEqual(config.audience_for_platform(brand), brand["audience"])

    def test_platform_override_no_brand_returns_none(self):
        import config
        self.assertIsNone(config.audience_for_platform(None, "livejournal"))

    def test_default_audience_is_brand_neutral(self):
        # The generic fallback must not assume any specific brand's audience
        # (e.g. the L&D/HR phrasing that config.json's example brands use),
        # so the tool behaves sanely with zero brands configured.
        self.assertNotIn("L&Ds", generate.DEFAULT_AUDIENCE)
        self.assertNotIn("HRs", generate.DEFAULT_AUDIENCE)


class AudienceResolutionTests(unittest.TestCase):
    def test_explicit_audience_wins_over_url(self):
        result = generate.resolve_audience("custom audience", "https://www.edstellar.com")
        self.assertEqual(result, "custom audience")

    def test_url_resolves_configured_brand_audience(self):
        import config
        expected = config.BRANDS["edstellar.com"]["audience"]
        result = generate.resolve_audience(None, "https://www.edstellar.com/blog/x")
        self.assertEqual(result, expected)

    def test_unconfigured_url_falls_back_to_default(self):
        result = generate.resolve_audience(None, "https://example.com")
        self.assertEqual(result, generate.DEFAULT_AUDIENCE)

    def test_no_audience_no_url_falls_back_to_default(self):
        result = generate.resolve_audience(None, None)
        self.assertEqual(result, generate.DEFAULT_AUDIENCE)

    def test_platform_override_wins_over_brand_default_audience(self):
        import config
        expected = config.BRANDS["edstellar.com"]["platform_audience_overrides"]["livejournal"]
        result = generate.resolve_audience(None, "https://www.edstellar.com", "livejournal")
        self.assertEqual(result, expected)
        self.assertNotEqual(result, config.BRANDS["edstellar.com"]["audience"])

    def test_platform_without_override_falls_back_to_brand_default(self):
        import config
        expected = config.BRANDS["edstellar.com"]["audience"]
        result = generate.resolve_audience(None, "https://www.edstellar.com", "gmb")
        self.assertEqual(result, expected)

    def test_explicit_audience_wins_over_platform_override(self):
        result = generate.resolve_audience("custom audience", "https://www.edstellar.com", "livejournal")
        self.assertEqual(result, "custom audience")


class MarketRegisterTests(unittest.TestCase):
    def test_market_for_brand_defaults_to_b2b(self):
        import config
        self.assertEqual(config.market_for_brand(None), "b2b")
        self.assertEqual(config.market_for_brand({}), "b2b")
        self.assertEqual(config.market_for_brand({"market": ""}), "b2b")

    def test_configured_markets_resolve(self):
        import config
        self.assertEqual(config.market_for_brand(config.BRANDS["edstellar.com"]), "b2b")
        self.assertEqual(config.market_for_brand(config.BRANDS["example-creator.com"]), "creator")

    def test_market_voice_falls_back_to_b2b(self):
        from templates._shared import market_voice
        self.assertIn("B2B", market_voice(None))
        self.assertIn("B2B", market_voice("not-a-market"))
        self.assertIn("CREATOR", market_voice("creator"))
        self.assertIn("B2C", market_voice("b2c"))

    def test_build_prompt_accepts_market_kwarg(self):
        prompt = generate.build_prompt("personal_brand_post", market="creator", **SAMPLE)
        self.assertIn("CREATOR", prompt)


class LlmTests(unittest.TestCase):
    def test_missing_key_raises_runtime_error(self):
        import os

        import llm
        saved = os.environ.pop("ANTHROPIC_API_KEY", None)
        try:
            with self.assertRaises(RuntimeError):
                llm.generate_content("hello")
        finally:
            if saved is not None:
                os.environ["ANTHROPIC_API_KEY"] = saved

    def test_missing_key_raises_runtime_error_per_provider(self):
        import os

        import llm
        cases = [
            ("anthropic", "ANTHROPIC_API_KEY"),
            ("gemini", "GEMINI_API_KEY"),
            ("openai", "OPENAI_API_KEY"),
        ]
        for provider, env_var in cases:
            with self.subTest(provider=provider):
                saved = os.environ.pop(env_var, None)
                saved_fallback = os.environ.pop("GOOGLE_API_KEY", None) if provider == "gemini" else None
                try:
                    with self.assertRaises(RuntimeError):
                        llm.generate_content("hello", provider=provider)
                finally:
                    if saved is not None:
                        os.environ[env_var] = saved
                    if saved_fallback is not None:
                        os.environ["GOOGLE_API_KEY"] = saved_fallback

    def test_unknown_provider_raises_runtime_error(self):
        import llm
        with self.assertRaises(RuntimeError):
            llm.generate_content("hello", provider="not-a-real-provider")

    def test_gemini_accepts_google_api_key_fallback(self):
        import os

        import llm
        saved_gemini = os.environ.pop("GEMINI_API_KEY", None)
        os.environ["GOOGLE_API_KEY"] = "test-key"
        try:
            self.assertTrue(llm._api_key_for("gemini"))
        finally:
            os.environ.pop("GOOGLE_API_KEY", None)
            if saved_gemini is not None:
                os.environ["GEMINI_API_KEY"] = saved_gemini

    def test_default_model_per_provider_falls_back_to_builtin(self):
        import llm
        for provider in ("anthropic", "gemini", "openai"):
            with self.subTest(provider=provider):
                self.assertTrue(llm._default_model_for(provider))

    def test_is_available_false_without_key(self):
        import os

        import llm
        saved = os.environ.pop("OPENAI_API_KEY", None)
        try:
            self.assertFalse(llm.is_available("openai"))
        finally:
            if saved is not None:
                os.environ["OPENAI_API_KEY"] = saved


class LlmResponseParsingTests(unittest.TestCase):
    """Mocked-SDK tests for each provider's response-parsing path (happy path
    and empty/blocked-response guard), since these never run against a real
    API key in CI."""

    def test_anthropic_happy_path_returns_joined_text(self):
        import sys
        import types as _types
        from unittest.mock import MagicMock, patch

        import llm

        block = MagicMock(type="text", text="hello world")
        message = MagicMock(content=[block], stop_reason="end_turn")
        fake_client = MagicMock()
        fake_client.messages.create.return_value = message
        fake_anthropic = _types.SimpleNamespace(Anthropic=MagicMock(return_value=fake_client))
        with patch.dict(sys.modules, {"anthropic": fake_anthropic}):
            result = llm._generate_anthropic("prompt", "key", "model", 100)
        self.assertEqual(result, "hello world")

    def test_anthropic_empty_text_raises_runtime_error(self):
        import sys
        import types as _types
        from unittest.mock import MagicMock, patch

        import llm

        block = MagicMock(type="text", text="")
        message = MagicMock(content=[block], stop_reason="max_tokens")
        fake_client = MagicMock()
        fake_client.messages.create.return_value = message
        fake_anthropic = _types.SimpleNamespace(Anthropic=MagicMock(return_value=fake_client))
        with patch.dict(sys.modules, {"anthropic": fake_anthropic}):
            with self.assertRaises(RuntimeError):
                llm._generate_anthropic("prompt", "key", "model", 100)

    def test_gemini_happy_path_returns_text(self):
        import sys
        import types as _types
        from unittest.mock import MagicMock, patch

        import llm

        response = MagicMock(candidates=[MagicMock()], text="hello gemini")
        fake_client = MagicMock()
        fake_client.models.generate_content.return_value = response
        fake_types = _types.SimpleNamespace(GenerateContentConfig=MagicMock())
        fake_genai = _types.SimpleNamespace(Client=MagicMock(return_value=fake_client), types=fake_types)
        fake_google = _types.SimpleNamespace(genai=fake_genai)
        with patch.dict(sys.modules, {
            "google": fake_google,
            "google.genai": fake_genai,
            "google.genai.types": fake_types,
        }):
            result = llm._generate_gemini("prompt", "key", "model", 100)
        self.assertEqual(result, "hello gemini")

    def test_gemini_no_candidates_raises_runtime_error(self):
        import sys
        import types as _types
        from unittest.mock import MagicMock, patch

        import llm

        response = MagicMock(candidates=[], prompt_feedback="BLOCKED_SAFETY")
        fake_client = MagicMock()
        fake_client.models.generate_content.return_value = response
        fake_types = _types.SimpleNamespace(GenerateContentConfig=MagicMock())
        fake_genai = _types.SimpleNamespace(Client=MagicMock(return_value=fake_client), types=fake_types)
        fake_google = _types.SimpleNamespace(genai=fake_genai)
        with patch.dict(sys.modules, {
            "google": fake_google,
            "google.genai": fake_genai,
            "google.genai.types": fake_types,
        }):
            with self.assertRaises(RuntimeError):
                llm._generate_gemini("prompt", "key", "model", 100)

    def test_openai_happy_path_returns_content(self):
        import sys
        import types as _types
        from unittest.mock import MagicMock, patch

        import llm

        choice = MagicMock(message=MagicMock(content="hello openai"), finish_reason="stop")
        response = MagicMock(choices=[choice])
        fake_client = MagicMock()
        fake_client.chat.completions.create.return_value = response
        fake_openai = _types.SimpleNamespace(OpenAI=MagicMock(return_value=fake_client))
        with patch.dict(sys.modules, {"openai": fake_openai}):
            result = llm._generate_openai("prompt", "key", "model", 100)
        self.assertEqual(result, "hello openai")

    def test_openai_empty_choices_raises_runtime_error(self):
        import sys
        import types as _types
        from unittest.mock import MagicMock, patch

        import llm

        response = MagicMock(choices=[])
        fake_client = MagicMock()
        fake_client.chat.completions.create.return_value = response
        fake_openai = _types.SimpleNamespace(OpenAI=MagicMock(return_value=fake_client))
        with patch.dict(sys.modules, {"openai": fake_openai}):
            with self.assertRaises(RuntimeError):
                llm._generate_openai("prompt", "key", "model", 100)


def _single_run_args(**overrides):
    """Minimal argparse-shaped Namespace for generate.run_single, with sane
    defaults for every attribute run_single touches."""
    import types as _types
    base = dict(
        platform="blog", topic="leadership training", wordcount=generate.DEFAULT_WORDCOUNT,
        audience=None, title=None, platform_target=None, cta=None, output_dir=None,
        repurpose=None, from_platform="blog", url=None, dry_run=True, generate=False,
        provider=None, model=None,
    )
    base.update(overrides)
    return _types.SimpleNamespace(**base)


class ProviderValidationTests(unittest.TestCase):
    """E1: --generate --provider <bogus> must fail loudly, even under --dry-run,
    instead of silently falling through to a prompt-only print."""

    def test_bad_provider_exits_cleanly_under_dry_run(self):
        import contextlib
        import io

        args = _single_run_args(generate=True, provider="not-a-real-provider", dry_run=True)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            with self.assertRaises(SystemExit) as ctx:
                generate.run_single(args)
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("Unknown LLM provider", buf.getvalue())

    def test_bad_provider_rejected_before_prompt_is_printed(self):
        import contextlib
        import io

        args = _single_run_args(generate=True, provider="not-a-real-provider", dry_run=True)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            with self.assertRaises(SystemExit):
                generate.run_single(args)
        # Validation happens before the prompt is assembled/printed.
        self.assertNotIn("leadership training", buf.getvalue())

    def test_known_provider_passes_validation(self):
        # Should not raise/exit - falls through to the normal dry-run prompt print.
        import contextlib
        import io

        args = _single_run_args(generate=True, provider="anthropic", dry_run=True)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            generate.run_single(args)
        self.assertIn("[dry-run] Nothing written.", buf.getvalue())

    def test_no_generate_skips_provider_validation(self):
        # A bogus --provider with no --generate is inert and must not be validated.
        args = _single_run_args(generate=False, provider="not-a-real-provider", dry_run=True)
        generate.run_single(args)  # must not raise


class BulkDryRunTests(unittest.TestCase):
    """DI3: --bulk --dry-run must print prompts without writing a zip/log file."""

    def _write_csv(self, tmpdir, rows):
        import csv as _csv
        import os as _os
        path = _os.path.join(tmpdir, "bulk.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = _csv.DictWriter(f, fieldnames=["platform", "topic", "source_file"])
            writer.writeheader()
            writer.writerows(rows)
        return path

    def test_dry_run_writes_no_files(self):
        import contextlib
        import io
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = self._write_csv(tmpdir, [{"platform": "blog", "topic": "t1", "source_file": ""}])
            out_dir = os.path.join(tmpdir, "out")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                generate.run_bulk(csv_path, output_dir_arg=out_dir, dry_run=True)
            self.assertFalse(os.path.isdir(out_dir), "dry-run must not create the output dir")
            self.assertIn("[dry-run]", buf.getvalue())
            self.assertIn("would be packaged", buf.getvalue())
            self.assertIn("Nothing written", buf.getvalue())

    def test_real_run_writes_zip_and_log(self):
        import contextlib
        import io
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = self._write_csv(tmpdir, [{"platform": "blog", "topic": "t1", "source_file": ""}])
            out_dir = os.path.join(tmpdir, "out")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                generate.run_bulk(csv_path, output_dir_arg=out_dir, dry_run=False)
            files = os.listdir(out_dir)
            self.assertTrue(any(name.startswith("bulk_") and name.endswith(".zip") for name in files))
            self.assertTrue(any(name.startswith("log_") and name.endswith(".csv") for name in files))


class PathContainmentTests(unittest.TestCase):
    """S4: --repurpose FILE and bulk CSV source_file must reject paths that
    resolve outside the project's working-directory tree."""

    def test_repurpose_traversal_is_rejected(self):
        import contextlib
        import io

        args = _single_run_args(
            platform="blog", repurpose="../outside_project_file.txt", dry_run=True,
        )
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            with self.assertRaises(SystemExit) as ctx:
                generate.run_single(args)
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("escapes the project directory", buf.getvalue())

    def test_repurpose_relative_path_within_project_is_allowed(self):
        import contextlib
        import io
        import os
        import tempfile

        fd, path = tempfile.mkstemp(dir=os.getcwd(), suffix=".txt")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write("Some source content to repurpose.")
            rel_path = os.path.relpath(path, os.getcwd())
            args = _single_run_args(platform="blog", repurpose=rel_path, dry_run=True)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                generate.run_single(args)
            self.assertIn("[dry-run] Nothing written.", buf.getvalue())
        finally:
            os.remove(path)

    def test_bulk_source_file_traversal_is_rejected(self):
        import contextlib
        import csv as _csv
        import io
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = os.path.join(tmpdir, "bulk.csv")
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                writer = _csv.DictWriter(f, fieldnames=["platform", "topic", "source_file"])
                writer.writeheader()
                writer.writerow({
                    "platform": "repurpose", "topic": "t1",
                    "source_file": "../../../../windows/system32/drivers/etc/hosts",
                })
            out_dir = os.path.join(tmpdir, "out")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                generate.run_bulk(csv_path, output_dir_arg=out_dir, dry_run=True)
            output = buf.getvalue()
            self.assertIn("source_file escapes the project directory", output)
            self.assertNotIn("[001]", output)  # row was skipped, not processed


class LintContentTests(unittest.TestCase):
    def test_detects_em_dash(self):
        import os
        import tempfile

        import lint_content
        fd, path = tempfile.mkstemp(suffix=".txt", text=True)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write("clean line\nthis has an em dash — here\n")
            errors = lint_content.check_file(path)
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], 2)
        finally:
            os.remove(path)

    def test_clean_file_passes(self):
        import os
        import tempfile

        import lint_content
        fd, path = tempfile.mkstemp(suffix=".txt", text=True)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write("clean line - with a hyphen\n")
            self.assertEqual(lint_content.check_file(path), [])
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
