import argparse
import csv
import os
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

import templates
import textprompts
from config import DEFAULTS, audience_for_platform, brand_for_url, market_for_brand

# Prompts can contain characters outside the Windows console's legacy code page.
# Force UTF-8 so printing never crashes with UnicodeEncodeError.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

PLATFORM_MAP = {
    # Existing
    "gmb":              "gmb",
    "google":           "gmb",
    "pinterest":        "pinterest",
    "medium":           "medium",
    "suggestion":       "blog_suggestion",
    "suggestions":      "blog_suggestion",
    "ideas":            "blog_suggestion",
    "linkedin":         "blog_writing",
    "wordpress":        "blog_writing",
    "blog":             "blog_writing",
    "devto":            "blog_writing_md",
    "dev.to":           "blog_writing_md",
    "hashnode":         "blog_writing_md",
    # New platforms
    "linkedin_post":    "linkedin_post",
    "linkedin-post":    "linkedin_post",
    "linkedinpost":     "linkedin_post",
    "twitter":          "twitter_thread",
    "twitter_thread":   "twitter_thread",
    "x":                "twitter_thread",
    "thread":           "twitter_thread",
    "youtube":          "youtube_desc",
    "youtube_desc":     "youtube_desc",
    "yt":               "youtube_desc",
    "newsletter":       "newsletter",
    "email":            "newsletter",
    "quora":            "quora",
    "instagram":        "instagram",
    "ig":               "instagram",
    # New workflows
    "content_brief":    "content_brief",
    "brief":            "content_brief",
    "faq":              "faq",
    "meta":             "meta",
    "case_study":       "case_study",
    "casestudy":        "case_study",
    "press_release":    "press_release",
    "pressrelease":     "press_release",
    "pr":               "press_release",
    "repurpose":        "repurpose",
    "calendar":         "content_calendar",
    "content_calendar": "content_calendar",
    # New platforms
    "haro":             "haro",
    "connectively":     "haro",
    "featured":         "haro",
    "linkedin_carousel": "linkedin_carousel",
    "carousel":         "linkedin_carousel",
    "video_script":     "video_script",
    "video":            "video_script",
    "script":           "video_script",
    "geo":              "geo",
    "aeo":              "geo",
    "ai_search":        "geo",
    "podcast":          "podcast",
    "show_notes":       "podcast",
    "guest_article":    "guest_article",
    "guest":            "guest_article",
    "byline":           "guest_article",
    "livejournal":      "livejournal_post",
    "lj":               "livejournal_post",
    "tumblr":           "tumblr_post",
    # New content types
    "short_form_video": "short_form_video",
    "shorts":           "short_form_video",
    "reels":            "short_form_video",
    "tiktok":           "short_form_video",
    "landing_page":     "landing_page",
    "landing":          "landing_page",
    "lp":               "landing_page",
    "comparison_page":  "comparison_page",
    "comparison":       "comparison_page",
    "vs":               "comparison_page",
    "alternative":      "comparison_page",
    "business_case_one_pager": "business_case_one_pager",
    "business_case":    "business_case_one_pager",
    "one_pager":        "business_case_one_pager",
    "internal_pitch":   "business_case_one_pager",
    # Creator / influencer / personal-brand types
    "influencer_outreach": "influencer_outreach",
    "outreach":         "influencer_outreach",
    "influencer":       "influencer_outreach",
    "ugc_brief":        "ugc_brief",
    "ugc":              "ugc_brief",
    "creator_brief":    "ugc_brief",
    "personal_brand_post": "personal_brand_post",
    "personal_brand":   "personal_brand_post",
    "personal_post":    "personal_brand_post",
    "creator_media_kit": "creator_media_kit",
    "media_kit":        "creator_media_kit",
    "mediakit":         "creator_media_kit",
}

MD_KEYS   = {"blog_writing_md"}
HTML_KEYS = {"medium", "livejournal_post", "tumblr_post"}

PRINT_ONLY = {"gmb", "pinterest"}

# Maps each template key to its output/ subfolder. Keep in sync with README tree.
SUBFOLDER_MAP = {
    "gmb":               "GMB",
    "pinterest":         "Pinterest",
    "medium":            "Medium",
    "blog_suggestion":   "Blog_Suggestions",
    "blog_writing":      "Blog",
    "blog_writing_md":   "DevTo_Hashnode",
    "linkedin_post":     "LinkedIn",
    "twitter_thread":    "Twitter",
    "youtube_desc":      "YouTube",
    "newsletter":        "Newsletter",
    "quora":             "Quora",
    "instagram":         "Instagram",
    "content_brief":     "Content_Brief",
    "faq":               "FAQ",
    "meta":              "Meta",
    "case_study":        "Case_Study",
    "press_release":     "Press_Release",
    "repurpose":         "DataBank",
    "content_calendar":  "Content_Calendar",
    "haro":              "HARO",
    "linkedin_carousel": "LinkedIn_Carousel",
    "video_script":      "Video_Scripts",
    "geo":               "GEO",
    "podcast":           "Podcast",
    "guest_article":     "Guest_Articles",
    "livejournal_post":  "LiveJournal",
    "tumblr_post":       "Tumblr",
    "short_form_video":  "Short_Form_Video",
    "landing_page":      "Landing_Pages",
    "comparison_page":   "Comparison_Pages",
    "business_case_one_pager": "Business_Case",
    "influencer_outreach": "Influencer_Outreach",
    "ugc_brief":         "UGC_Briefs",
    "personal_brand_post": "Personal_Brand",
    "creator_media_kit": "Media_Kit",
}


def subfolder_for(key):
    return SUBFOLDER_MAP.get(key, "Misc")


def resolve_audience(explicit_audience, url, platform_key=None):
    """Pick the effective audience: an explicit --audience wins, otherwise a
    brand configured for `url` in config.json's `brands` map (honoring that
    brand's `platform_audience_overrides` for `platform_key`, if any), otherwise
    the generic DEFAULTS["audience"] fallback."""
    if explicit_audience:
        return explicit_audience
    brand = brand_for_url(url) if url else None
    audience = audience_for_platform(brand, platform_key)
    return audience or DEFAULT_AUDIENCE


DEFAULT_AUDIENCE  = DEFAULTS["audience"]
DEFAULT_WORDCOUNT = DEFAULTS["wordcount"]


def resolve_key(platform_str):
    return PLATFORM_MAP.get(platform_str.lower().strip())


def resolve(platform_str):
    """Return (kind, ref) where kind is 'template' or 'text', or (None, None).

    'template' -> ref is a templates.py key. 'text' -> ref is the normalized alias.
    """
    norm = platform_str.lower().strip()
    if norm in PLATFORM_MAP:
        return "template", PLATFORM_MAP[norm]
    if textprompts.is_text_prompt(norm):
        return "text", norm
    return None, None


def print_platform_list():
    print("Automated (rich templates):")
    seen = {}
    for alias, key in sorted(PLATFORM_MAP.items()):
        seen.setdefault(key, []).append(alias)
    for key in sorted(seen):
        print(f"  {SUBFOLDER_MAP.get(key, 'Misc'):<20} {key:<18} aliases: {', '.join(seen[key])}")
    print("\nText prompts (flat prompt files):")
    files = {}
    for alias, (fname, folder) in sorted(textprompts.TEXT_PROMPT_MAP.items()):
        files.setdefault((fname, folder), []).append(alias)
    for (fname, folder), aliases in sorted(files.items()):
        print(f"  {folder:<24} aliases: {', '.join(aliases)}")


def default_output_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def make_filename(platform_label, key, index=None):
    safe      = re.sub(r"[^\w]+", "_", platform_label.lower())
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix    = f"_{index:03d}" if index is not None else ""
    ext       = ".md" if key in MD_KEYS else ".html" if key in HTML_KEYS else ".txt"
    return f"{safe}{suffix}_{timestamp}{ext}"


def build_prompt(key, topic, audience, wordcount, platform_label, platform_target,
                 title=None, from_platform="blog", source_content=None, market=None):
    kwargs = {
        "topic":          topic,
        "audience":       audience,
        "platform":       platform_target or platform_label,
        "wordcount":      wordcount,
        "title":          title,
        "from_platform":  from_platform,
        "source_content": source_content or "",
        # Brand's market register (b2b/b2c/creator). Every template takes **_,
        # so templates that don't consume it are unaffected.
        "market":         market or "b2b",
    }

    if key == "medium":
        return templates.medium_step2(**kwargs) if title else templates.medium_step1(**kwargs)

    fn = getattr(templates, key, None)
    if fn is None:
        raise ValueError(f"No template found for key '{key}'.")
    return fn(**kwargs)


def _resolve_contained_path(path, base_dir=None):
    """Resolve `path` and verify it stays within `base_dir`'s tree (default: CWD).

    Containment boundary is the current working directory - the tool is run from
    the project root, and both --repurpose files and bulk-CSV source_file entries
    are expected to live inside it. Returns the resolved Path, or None if `path`
    escapes that boundary (absolute path elsewhere, ../ traversal, UNC path, etc.).
    """
    base = Path(base_dir or os.getcwd()).resolve()
    resolved = Path(path).resolve()
    try:
        resolved.relative_to(base)
    except ValueError:
        return None
    return resolved


def _validate_provider_or_exit(provider):
    """When --generate is passed, validate --provider against llm's known provider
    list before doing anything else (even under --dry-run), so a bogus provider
    fails loudly instead of silently falling through to a prompt-only print."""
    import llm  # deferred: avoids a hard dependency on any provider SDK unless --generate is used
    try:
        llm._resolve_provider(provider)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)


def inject_cta(prompt, cta):
    if cta:
        return prompt.replace("[INSERT CTA LINK]", cta)
    return prompt


def write_bulk_log(log_rows, path):
    with open(path, "w", newline="", encoding="utf-8") as lf:
        writer = csv.DictWriter(lf, fieldnames=["row", "platform", "topic", "filename", "status"])
        writer.writeheader()
        writer.writerows(log_rows)


def parse_bulk_row(row, i):
    platform = row.get("platform", "").strip()
    topic    = row.get("topic",    "").strip()
    if not platform or not topic:
        return None, f"Row {i}: skipped - missing platform or topic"
    url = row.get("url", "").strip() or None
    try:
        wordcount = int(row.get("wordcount", DEFAULT_WORDCOUNT) or DEFAULT_WORDCOUNT)
    except ValueError:
        return None, f"Row {i}: skipped - invalid wordcount"
    return {
        "platform":        platform,
        "topic":           topic,
        "wordcount":       wordcount,
        "audience":        resolve_audience(row.get("audience", "").strip() or None, url, platform.lower()),
        "market":          market_for_brand(brand_for_url(url) if url else None),
        "title":           row.get("title",           "").strip() or None,
        "platform_target": row.get("platform_target", "").strip() or None,
        "cta":             row.get("cta",             "").strip() or None,
        "from_platform":   row.get("from_platform",   "blog").strip() or "blog",
        "source_file":     row.get("source_file",     "").strip() or None,
    }, None


def run_single(args):
    if args.generate:
        _validate_provider_or_exit(args.provider)

    output_dir = args.output_dir or default_output_dir()
    effective_audience = resolve_audience(args.audience, args.url, (args.platform or "").lower().strip())

    kind = None
    key = None
    source_content = None

    if args.repurpose:
        resolved_repurpose = _resolve_contained_path(args.repurpose)
        if resolved_repurpose is None:
            print(f"Error: --repurpose path escapes the project directory: {args.repurpose}")
            sys.exit(1)
        if not resolved_repurpose.exists():
            print(f"Error: repurpose file not found: {args.repurpose}")
            sys.exit(1)
        with open(resolved_repurpose, "r", encoding="utf-8") as f:
            source_content = f.read()
        kind, key = "template", "repurpose"
        normalized = "repurpose"
        # --platform is the TARGET platform when repurposing; treat it as platform_target
        effective_platform_target = args.platform
    else:
        normalized = args.platform.lower().strip()
        kind, key = resolve(normalized)
        if kind is None:
            print(f"Unknown platform: '{args.platform}'\n")
            print_platform_list()
            sys.exit(1)
        effective_platform_target = args.platform_target

    if kind == "text":
        prompt = textprompts.render(
            normalized, topic=args.topic, audience=effective_audience,
            wordcount=args.wordcount, cta=args.cta, url=args.url,
        )
        folder = textprompts.subfolder_for(normalized)
        out_key = "text"
    else:
        prompt = build_prompt(
            key,
            topic=args.topic,
            audience=effective_audience,
            wordcount=args.wordcount,
            platform_label=normalized,
            platform_target=effective_platform_target,
            title=args.title,
            from_platform=args.from_platform or "blog",
            source_content=source_content,
            market=market_for_brand(brand_for_url(args.url) if args.url else None),
        )
        prompt = inject_cta(prompt, args.cta)
        folder = subfolder_for(key)
        out_key = key

    print("\n" + "=" * 60)
    print(prompt)
    print("=" * 60)

    if args.dry_run:
        print("\n[dry-run] Nothing written.")
        return

    content, out_key = _maybe_generate(prompt, out_key, args)

    # PRINT_ONLY only applies to prompt output, not generated content.
    if out_key in PRINT_ONLY and not args.generate:
        return

    os.makedirs(output_dir, exist_ok=True)
    filename = make_filename(normalized, out_key)
    subdir   = os.path.join(output_dir, folder)
    os.makedirs(subdir, exist_ok=True)
    filepath = os.path.join(subdir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    label = "Content" if args.generate else "Prompt"
    print(f"\n{label} saved to: {os.path.relpath(filepath)}")


def _maybe_generate(prompt, out_key, args):
    """If --generate, call the LLM and return (content, key); else return the prompt."""
    if not args.generate:
        return prompt, out_key
    import llm  # deferred: avoids a hard dependency on any provider SDK unless --generate is used
    provider_label = args.provider or "the configured default provider"
    print(f"\nGenerating content via {provider_label}...")
    try:
        content = llm.generate_content(prompt, model=args.model, provider=args.provider)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)
    return content, out_key


def run_bulk(csv_path, output_dir_arg=None, global_cta=None, dry_run=False):
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found: {csv_path}")
        sys.exit(1)

    output_dir = output_dir_arg or default_output_dir()
    if not dry_run:
        os.makedirs(output_dir, exist_ok=True)

    jobs = []
    errors = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        for i, row in enumerate(csv.DictReader(f), start=1):
            job, err = parse_bulk_row(row, i)
            if err:
                errors.append(err)
            else:
                jobs.append((i, job))

    if not jobs:
        print("No valid rows found in the CSV.")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)

    # Up-front validation: surface every unresolved platform before writing anything.
    unresolved = [(i, job["platform"]) for i, job in jobs if resolve(job["platform"])[0] is None]
    if unresolved:
        print("Warning: these rows have unknown platforms and will be skipped:")
        for i, platform in unresolved:
            print(f"  Row {i}: '{platform}'")
        print()

    print(f"Processing {len(jobs)} job(s) from {os.path.basename(csv_path)}...\n")

    timestamp     = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename  = f"bulk_{timestamp}.zip"
    zip_path      = os.path.join(output_dir, zip_filename)
    log_filename  = f"log_{timestamp}.csv"
    log_path      = os.path.join(output_dir, log_filename)
    log_rows      = []

    def process_job(i, job, zf):
        """Build the prompt for one row. Writes it into `zf` (real run), or just
        prints it when `zf` is None (--dry-run: nothing touches disk). Appends
        to the enclosing `errors`/`log_rows` lists as it goes."""
        platform = job["platform"]
        kind, key = resolve(platform)

        if kind is None:
            msg = f"unknown platform '{platform}'"
            errors.append(f"Row {i}: {msg}")
            log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                              "filename": "", "status": f"error: {msg}"})
            return

        source_content = None
        if job["source_file"]:
            resolved_src = _resolve_contained_path(job["source_file"])
            if resolved_src is None:
                msg = f"source_file escapes the project directory: {job['source_file']}"
                errors.append(f"Row {i}: {msg}")
                log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                                  "filename": "", "status": f"error: {msg}"})
                return
            if resolved_src.exists():
                with open(resolved_src, "r", encoding="utf-8") as sf:
                    source_content = sf.read()
            else:
                msg = f"source_file not found: {job['source_file']}"
                errors.append(f"Row {i}: {msg}")
                log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                                  "filename": "", "status": f"error: {msg}"})
                return

        try:
            cta = job["cta"] or global_cta
            if kind == "text":
                prompt = textprompts.render(
                    platform.lower(), topic=job["topic"], audience=job["audience"],
                    wordcount=job["wordcount"], cta=cta,
                )
                folder = textprompts.subfolder_for(platform.lower())
                file_key = "text"
            else:
                prompt = build_prompt(
                    key,
                    topic=job["topic"],
                    audience=job["audience"],
                    wordcount=job["wordcount"],
                    platform_label=platform.lower(),
                    platform_target=job["platform_target"],
                    title=job["title"],
                    from_platform=job["from_platform"],
                    source_content=source_content,
                    market=job["market"],
                )
                prompt = inject_cta(prompt, cta)
                folder = subfolder_for(key)
                file_key = key
        except Exception as e:
            errors.append(f"Row {i}: error building prompt - {e}")
            log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                              "filename": "", "status": f"error: {e}"})
            return

        filename = make_filename(platform, file_key, index=i)
        arcname  = f"{folder}/{filename}"

        if zf is None:
            print(f"\n[{i:03d}] {arcname}")
            print("-" * 60)
            print(prompt)
            print("-" * 60)
        else:
            zf.writestr(arcname, prompt)
            print(f"  [{i:03d}] {arcname}")

        log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                          "filename": arcname, "status": "ok"})

    if dry_run:
        for i, job in jobs:
            process_job(i, job, None)
    else:
        try:
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for i, job in jobs:
                    process_job(i, job, zf)
        finally:
            # Flush whatever log rows were produced so far, even if the loop above
            # crashed partway through - a truncated zip should never ship with no log.
            write_bulk_log(log_rows, log_path)

    if errors:
        print("\nIssues:")
        for e in errors:
            print(f"  {e}")

    ok_count = sum(1 for r in log_rows if r["status"] == "ok")
    if dry_run:
        print(f"\n[dry-run] {ok_count} prompt(s) would be packaged. Nothing written.")
    else:
        print(f"\n{ok_count} prompt(s) packaged into: {os.path.relpath(zip_path)}")
        print(f"Run log saved to:           {os.path.relpath(log_path)}")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Brand Content Distribution Prompt Generator",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--platform",        help="Target platform. Run without args to see full list.")
    parser.add_argument("--topic",           help="Blog/post topic or niche")
    parser.add_argument("--wordcount",       type=int, default=DEFAULT_WORDCOUNT,
                        help=f"Word count target (default: {DEFAULT_WORDCOUNT})")
    parser.add_argument("--audience",        default=None,
                        help="Target audience description. If omitted, resolved from "
                             "--url via config.json's brands map, else falls back to "
                             f"'{DEFAULT_AUDIENCE}'")
    parser.add_argument("--title",           default=None,
                        help="(Medium Step 2) Article title chosen from Step 1")
    parser.add_argument("--platform-target", default=None, dest="platform_target",
                        help="Secondary platform label (Blog Suggestion, Calendar, etc.)")
    parser.add_argument("--cta",             default=None,
                        help="Actual CTA URL - replaces [INSERT CTA LINK] in the output")
    parser.add_argument("--output-dir",      default=None, dest="output_dir",
                        help="Custom output directory (default: ./output)")
    parser.add_argument("--repurpose",       default=None, metavar="FILE",
                        help="Path to existing content file to repurpose for --platform")
    parser.add_argument("--from-platform",   default="blog", dest="from_platform",
                        help="Source platform of the repurposed content (default: blog)")
    parser.add_argument("--bulk",            default=None, metavar="CSV_FILE",
                        help="CSV file for bulk generation. Outputs a ZIP + log CSV.")
    parser.add_argument("--url",             default=None,
                        help="Brand URL. Matched against config.json's brands map to "
                             "auto-fill --audience when --audience is omitted; also "
                             "passed through to text prompts for brand auto-detection.")
    parser.add_argument("--list",            action="store_true", dest="list_platforms",
                        help="List all platforms/aliases and exit")
    parser.add_argument("--dry-run",         action="store_true", dest="dry_run",
                        help="Print the assembled prompt without writing any file")
    parser.add_argument("--generate",        action="store_true",
                        help="Call an LLM and save finished content (needs that provider's API key; "
                             "see --provider)")
    parser.add_argument("--provider",        default=None,
                        help="LLM provider for --generate: anthropic (Claude, needs ANTHROPIC_API_KEY), "
                             "gemini (needs GEMINI_API_KEY or GOOGLE_API_KEY), or openai (Codex/GPT, "
                             "needs OPENAI_API_KEY). Defaults to config.json's defaults.llm_provider "
                             "('anthropic' if unset).")
    parser.add_argument("--model",           default=None,
                        help="Override the LLM model id used by --generate (defaults to the "
                             "selected provider's entry in config.json's defaults.llm_models)")

    args = parser.parse_args()

    if args.list_platforms:
        print_platform_list()
        return

    if args.bulk:
        run_bulk(args.bulk, output_dir_arg=args.output_dir, global_cta=args.cta, dry_run=args.dry_run)
    elif args.repurpose:
        if not args.platform:
            parser.error("--platform is required with --repurpose (specifies the target platform)")
        if not args.topic:
            parser.error("--topic is required (describes the content focus)")
        run_single(args)
    else:
        if not args.platform or not args.topic:
            parser.error("--platform and --topic are required (or use --bulk CSV_FILE)")
        run_single(args)


if __name__ == "__main__":
    main()
