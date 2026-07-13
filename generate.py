import argparse
import csv
import os
import sys
import zipfile
from datetime import datetime
import templates

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
}

MD_KEYS   = {"blog_writing_md"}
HTML_KEYS = {"medium"}

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
}


def subfolder_for(key):
    return SUBFOLDER_MAP.get(key, "Misc")

DEFAULT_AUDIENCE  = "L&Ds, HRs, and Decision makers in the organization"
DEFAULT_WORDCOUNT = 1000
AVAILABLE_PLATFORMS = ", ".join(sorted(set(PLATFORM_MAP.keys())))


def resolve_key(platform_str):
    return PLATFORM_MAP.get(platform_str.lower().strip())


def default_output_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def make_filename(platform_label, key, index=None):
    safe      = platform_label.lower().replace(".", "").replace("-", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix    = f"_{index:03d}" if index is not None else ""
    ext       = ".md" if key in MD_KEYS else ".html" if key in HTML_KEYS else ".txt"
    return f"{safe}{suffix}_{timestamp}{ext}"


def build_prompt(key, topic, audience, wordcount, platform_label, platform_target,
                 title=None, from_platform="blog", source_content=None):
    kwargs = {
        "topic":          topic,
        "audience":       audience,
        "platform":       platform_target or platform_label,
        "wordcount":      wordcount,
        "title":          title,
        "from_platform":  from_platform,
        "source_content": source_content or "",
    }

    if key == "medium":
        return templates.medium_step2(**kwargs) if title else templates.medium_step1(**kwargs)

    fn = getattr(templates, key, None)
    if fn is None:
        raise ValueError(f"No template found for key '{key}'.")
    return fn(**kwargs)


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
    return {
        "platform":        platform,
        "topic":           topic,
        "wordcount":       int(row.get("wordcount", DEFAULT_WORDCOUNT) or DEFAULT_WORDCOUNT),
        "audience":        row.get("audience",        "").strip() or DEFAULT_AUDIENCE,
        "title":           row.get("title",           "").strip() or None,
        "platform_target": row.get("platform_target", "").strip() or None,
        "cta":             row.get("cta",             "").strip() or None,
        "from_platform":   row.get("from_platform",   "blog").strip() or "blog",
        "source_file":     row.get("source_file",     "").strip() or None,
    }, None


def run_single(args):
    output_dir = args.output_dir or default_output_dir()
    os.makedirs(output_dir, exist_ok=True)

    source_content = None
    if args.repurpose:
        if not os.path.exists(args.repurpose):
            print(f"Error: repurpose file not found: {args.repurpose}")
            sys.exit(1)
        with open(args.repurpose, "r", encoding="utf-8") as f:
            source_content = f.read()
        key = "repurpose"
        normalized = "repurpose"
        # --platform is the TARGET platform when repurposing; treat it as platform_target
        effective_platform_target = args.platform
    else:
        normalized = args.platform.lower().strip()
        key = resolve_key(normalized)
        if key is None:
            print(f"Unknown platform: '{args.platform}'")
            print(f"Available platforms: {AVAILABLE_PLATFORMS}")
            sys.exit(1)
        effective_platform_target = args.platform_target

    prompt = build_prompt(
        key,
        topic=args.topic,
        audience=args.audience,
        wordcount=args.wordcount,
        platform_label=normalized,
        platform_target=effective_platform_target,
        title=args.title,
        from_platform=args.from_platform or "blog",
        source_content=source_content,
    )
    prompt = inject_cta(prompt, args.cta)

    print("\n" + "=" * 60)
    print(prompt)
    print("=" * 60)

    if key in PRINT_ONLY:
        return

    filename = make_filename(normalized, key)
    subdir   = os.path.join(output_dir, subfolder_for(key))
    os.makedirs(subdir, exist_ok=True)
    filepath = os.path.join(subdir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"\nPrompt saved to: {os.path.relpath(filepath)}")


def run_bulk(csv_path, output_dir_arg=None, global_cta=None):
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found: {csv_path}")
        sys.exit(1)

    output_dir = output_dir_arg or default_output_dir()
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

    print(f"\nProcessing {len(jobs)} job(s) from {os.path.basename(csv_path)}...\n")

    timestamp     = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename  = f"bulk_{timestamp}.zip"
    zip_path      = os.path.join(output_dir, zip_filename)
    log_rows      = []

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for i, job in jobs:
            platform = job["platform"]
            key = resolve_key(platform)

            if key is None:
                msg = f"unknown platform '{platform}'"
                errors.append(f"Row {i}: {msg}")
                log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                                  "filename": "", "status": f"error: {msg}"})
                continue

            source_content = None
            if job["source_file"]:
                if os.path.exists(job["source_file"]):
                    with open(job["source_file"], "r", encoding="utf-8") as sf:
                        source_content = sf.read()
                else:
                    msg = f"source_file not found: {job['source_file']}"
                    errors.append(f"Row {i}: {msg}")
                    log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                                      "filename": "", "status": f"error: {msg}"})
                    continue

            try:
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
                )
                cta = job["cta"] or global_cta
                prompt = inject_cta(prompt, cta)
            except Exception as e:
                errors.append(f"Row {i}: error building prompt - {e}")
                log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                                  "filename": "", "status": f"error: {e}"})
                continue

            filename = make_filename(platform, key, index=i)
            arcname  = f"{subfolder_for(key)}/{filename}"
            zf.writestr(arcname, prompt)
            log_rows.append({"row": i, "platform": platform, "topic": job["topic"],
                              "filename": arcname, "status": "ok"})
            print(f"  [{i:03d}] {arcname}")

    if errors:
        print("\nIssues:")
        for e in errors:
            print(f"  {e}")

    log_filename = f"log_{timestamp}.csv"
    write_bulk_log(log_rows, os.path.join(output_dir, log_filename))

    ok_count = sum(1 for r in log_rows if r["status"] == "ok")
    print(f"\n{ok_count} prompt(s) packaged into: {os.path.relpath(zip_path)}")
    print(f"Run log saved to:           {os.path.relpath(os.path.join(output_dir, log_filename))}")


def main():
    parser = argparse.ArgumentParser(
        description="Edstellar Content Distribution Prompt Generator",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--platform",        help="Target platform. Run without args to see full list.")
    parser.add_argument("--topic",           help="Blog/post topic or niche")
    parser.add_argument("--wordcount",       type=int, default=DEFAULT_WORDCOUNT,
                        help=f"Word count target (default: {DEFAULT_WORDCOUNT})")
    parser.add_argument("--audience",        default=DEFAULT_AUDIENCE,
                        help="Target audience description")
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

    args = parser.parse_args()

    if args.bulk:
        run_bulk(args.bulk, output_dir_arg=args.output_dir, global_cta=args.cta)
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
