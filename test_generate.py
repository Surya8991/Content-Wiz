"""Smoke tests for the prompt generator.

Run: python -m unittest test_generate -v

These guard against signature drift between generate.py's PLATFORM_MAP and
templates.py: every routed platform must resolve to a template, render a
non-empty prompt, and route to a declared output subfolder.
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


class CtaInjectionTests(unittest.TestCase):
    def test_cta_replaces_placeholder(self):
        out = generate.inject_cta("Visit [INSERT CTA LINK] now", "https://edstellar.com")
        self.assertIn("https://edstellar.com", out)
        self.assertNotIn("[INSERT CTA LINK]", out)

    def test_cta_none_is_noop(self):
        text = "Visit [INSERT CTA LINK] now"
        self.assertEqual(generate.inject_cta(text, None), text)


if __name__ == "__main__":
    unittest.main()
