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
