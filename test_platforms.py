"""Regression tests for additional global and regional platform builders."""
import contextlib
import csv
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import generate
import textprompts
from templates._shared import market_voice
from test_generate import _single_run_args

PLATFORMS = {'bluesky_post': ('Bluesky', ['bluesky', 'bsky', 'bluesky_post'], 'Bluesky'),
 'mastodon_post': ('Mastodon', ['mastodon', 'mastodon_post'], 'Mastodon'),
 'telegram_channel_post': ('Telegram Channels',
                           ['telegram', 'telegram_channel', 'telegram_channel_post'],
                           'Telegram'),
 'whatsapp_channel_update': ('WhatsApp Channels',
                             ['whatsapp', 'whatsapp_channel', 'whatsapp_channel_update'],
                             'WhatsApp_Channels'),
 'youtube_community_post': ('YouTube Community posts',
                            ['youtube_community', 'youtube_post', 'youtube_community_post'],
                            'YouTube_Community'),
 'snapchat_story': ('Snapchat', ['snapchat', 'snapchat_story', 'snapchat_spotlight'], 'Snapchat'),
 'twitch_stream': ('Twitch', ['twitch', 'twitch_stream'], 'Twitch'),
 'kick_stream': ('Kick', ['kick', 'kick_stream'], 'Kick'),
 'spotify_episode': ('Spotify', ['spotify', 'spotify_episode'], 'Spotify'),
 'patreon_post': ('Patreon', ['patreon', 'patreon_post'], 'Patreon'),
 'product_hunt_launch': ('Product Hunt', ['product_hunt', 'producthunt', 'product_hunt_launch'], 'Product_Hunt'),
 'slack_community_post': ('Slack', ['slack', 'slack_community', 'slack_community_post'], 'Slack'),
 'nextdoor_post': ('Nextdoor', ['nextdoor', 'nextdoor_post'], 'Nextdoor'),
 'lemon8_post': ('Lemon8', ['lemon8', 'lemon8_post'], 'Lemon8'),
 'wechat_article': ('WeChat', ['wechat', 'wechat_article'], 'WeChat'),
 'weibo_post': ('Weibo', ['weibo', 'weibo_post'], 'Weibo'),
 'xiaohongshu_note': ('Xiaohongshu / RED', ['xiaohongshu', 'rednote', 'xiaohongshu_note'], 'Xiaohongshu'),
 'douyin_script': ('Douyin', ['douyin', 'douyin_script'], 'Douyin'),
 'bilibili_video': ('Bilibili', ['bilibili', 'bilibili_video'], 'Bilibili'),
 'line_message': ('LINE Official Account', ['line', 'line_message', 'line_official'], 'LINE')}


class AdditionalPlatformTests(unittest.TestCase):
    def test_aliases_route_and_render_each_market_with_cta(self):
        for key, (name, aliases, folder) in PLATFORMS.items():
            for alias in aliases:
                with self.subTest(alias=alias):
                    self.assertEqual(generate.resolve(alias), ("template", key))
                    self.assertEqual(generate.subfolder_for(key), folder)
            for market in ("b2b", "b2c", "creator"):
                with self.subTest(key=key, market=market):
                    prompt = generate.build_prompt(key, topic="Team onboarding", audience="New managers",
                                                   wordcount=1000, platform_label=aliases[0],
                                                   platform_target=None, market=market)
                    self.assertIn(name, prompt)
                    self.assertIn("Team onboarding", prompt)
                    self.assertIn("New managers", prompt)
                    self.assertIn(market_voice(market), prompt)
                    self.assertIn("data/HARO_DataBank.csv", prompt)
                    self.assertIn("human review", prompt)
                    self.assertIn("[INSERT CTA LINK]", prompt)
                    rendered = generate.inject_cta(prompt, "https://example.com/resource")
                    self.assertIn("https://example.com/resource", rendered)
                    self.assertNotIn("[INSERT CTA LINK]", rendered)

    def test_single_run_writes_each_platform_folder(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            for key, (_, aliases, folder) in PLATFORMS.items():
                with self.subTest(key=key):
                    generate.run_single(_single_run_args(platform=aliases[0], output_dir=temp, dry_run=False))
                    files = list((Path(temp) / folder).glob("*.txt"))
                    self.assertEqual(len(files), 1)
                    self.assertIn("DELIVERABLES:", files[0].read_text(encoding="utf-8"))

    def test_bulk_generation_packages_all_platform_payloads(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            root = Path(temp)
            source = root / "platforms.csv"
            with source.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(["platform", "topic"])
                for _, aliases, _ in PLATFORMS.values():
                    writer.writerow([aliases[0], "Onboarding"])
            with patch("llm.generate_content", return_value="Finished draft") as provider:
                generate.run_bulk(str(source), str(root / "output"), generate_content=True, parallel=4)
            self.assertEqual(provider.call_count, len(PLATFORMS))
            with zipfile.ZipFile(next((root / "output").glob("*.zip"))) as archive:
                folders = {name.split("/")[0] for name in archive.namelist()}
                self.assertEqual(folders, {row[2] for row in PLATFORMS.values()})
                self.assertIsNone(archive.testzip())
                self.assertTrue(all(archive.read(name) == b"Finished draft" for name in archive.namelist()))

    def test_facebook_short_aliases_keep_existing_prompt(self):
        canonical = textprompts.TEXT_PROMPT_MAP["facebook_post"]
        for alias in ("facebook", "fb"):
            with self.subTest(alias=alias):
                self.assertEqual(textprompts.TEXT_PROMPT_MAP[alias], canonical)
                self.assertEqual(generate.resolve(alias)[0], "text")
                self.assertNotIn(alias, generate.PLATFORM_MAP)

    def test_list_and_readme_include_new_aliases(self):
        result = io.StringIO()
        with contextlib.redirect_stdout(result):
            generate.print_platform_list()
        readme = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")
        for _, aliases, folder in PLATFORMS.values():
            for alias in aliases:
                self.assertIn(alias, result.getvalue())
                self.assertIn("`" + alias + "`", readme)
            self.assertIn(folder, readme)


if __name__ == "__main__":
    unittest.main()
