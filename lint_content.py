"""Content-rule linter. Enforces the project's hard content rules on the files
that feed the generator, so violations cannot silently land.

Currently enforced (error): no em-dash (U+2014) anywhere in prompt/strategy/
template source. Warnings are advisory and never fail the build.

Usage:
    python lint_content.py                   # lint the default fileset
    python lint_content.py path ...          # lint specific files
    python lint_content.py --check-urls DIR  # check all URLs in DIR for dead links
    python lint_content.py --check-banned-phrases DIR

Exit code 1 if any error is found.
"""
import os
import re
import sys
import urllib.request
import urllib.error

from templates._shared import BANNED_CTA_PHRASES

EM_DASH = "—"

# Files the linter should never scan: they reference the banned character on
# purpose (to detect it) and would otherwise self-flag.
SELF_REFERENTIAL = {"lint_content.py", "test_generate.py"}

DEFAULT_TARGET_DIRS = ["prompts", "strategies", "templates"]
DEFAULT_TARGET_FILES = ["generate.py", "textprompts.py", "README.md"]

SCAN_EXTS = {".txt", ".md", ".py", ".csv"}

# Opt-in banned-phrase check (e.g. `--check-banned-phrases output/`). Never
# run by default, output/ is real client content and this must not change
# existing CI/pre-commit behavior unexpectedly. Sourced from the same
# canonical list templates reference, so output/ and template source are
# always checked against one definition, not two that can drift apart.
BANNED_PHRASES = BANNED_CTA_PHRASES

BANNED_PHRASE_EXTS = {".md", ".html", ".csv"}

# Template-source regression guard (runs by default): confirms a banned CTA
# phrase never sneaks into a template's own example/scaffold text (the exact
# bug that let gmb()'s real output land on "Click on learn more" verbatim,
# and the later bug that let growth.py suggest "Discover" as a CTA verb
# unguarded). Scans every template module by default - not just the one
# file that happened to use the "DO NOT USE" convention - because each of
# the six CTA-bearing templates writes its own hand-rolled "bad example"
# prose (Bad:/NOT/Avoid:/etc.) and any of them can regress the same way.
# _shared.py is excluded: it *defines* BANNED_CTA_PHRASES, so every phrase
# appears there verbatim as a list literal, not as unguarded scaffold text.
BANNED_CTA_REGRESSION_EXCLUDE = {"_shared.py", "__init__.py"}


def _iter_banned_cta_regression_targets(root):
    tdir = os.path.join(root, "templates")
    if not os.path.isdir(tdir):
        return
    for name in sorted(os.listdir(tdir)):
        if os.path.splitext(name)[1] != ".py":
            continue
        if name in BANNED_CTA_REGRESSION_EXCLUDE:
            continue
        yield os.path.join("templates", name)


# Lines containing one of these markers anywhere on the line as a banned
# phrase mean the phrase is being named as forbidden (or as a "bad"
# example / spam-word list / algorithm-penalized example), not actually
# used as scaffold/example text the model is meant to copy - skip flagging
# it. Checked across the *whole line* rather than a fixed character
# lookbehind: these are short, single-concept instructional bullets (one
# CTA rule per line), not multi-topic paragraphs, so an earlier or later
# marker on the same line reliably describes the same example - a fixed-
# width window was proven too narrow in practice (e.g. growth.py's
# `* Bad:  "Click here" / "Read more" / "Learn more"` puts "Bad:" more than
# 25 characters before "Learn more", and `Self-promotional CTAs like "DM me
# to learn more" - LinkedIn's algorithm penalizes these` puts the negation
# signal *after* the phrase entirely).
# ("n't" deliberately excluded here: "Don't miss out" contains it inherently,
# which would make that phrase un-flaggable everywhere; it's instead handled
# by the heading-based block detection below.)
_NEGATION_MARKERS = (
    "not ", "avoid", "never", "banned", "bad:", "spam", "penalize",
)

# A heading line matching one of these (case-insensitive) opens a block
# where subsequent bullet lines enumerating banned phrases are expected
# and should not be flagged; the block ends at the next blank line or the
# first non-bullet line.
_NEGATION_HEADERS = ("do not use", "don't use", "banned phrase", "avoid these", "never use")


def _iter_default_targets(root):
    for d in DEFAULT_TARGET_DIRS:
        dpath = os.path.join(root, d)
        if not os.path.isdir(dpath):
            continue
        for name in sorted(os.listdir(dpath)):
            if os.path.splitext(name)[1] in SCAN_EXTS:
                yield os.path.join(dpath, name)
    for name in DEFAULT_TARGET_FILES:
        fpath = os.path.join(root, name)
        if os.path.isfile(fpath):
            yield fpath


def check_file(path):
    """Return a list of (lineno, message) error tuples for one file."""
    if os.path.basename(path) in SELF_REFERENTIAL:
        return []
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                if EM_DASH in line:
                    col = line.index(EM_DASH) + 1
                    errors.append((lineno, f"em-dash (U+2014) at column {col}"))
    except (OSError, UnicodeDecodeError) as exc:
        errors.append((0, f"could not read file: {exc}"))
    return errors


def _iter_files_under(dpath, exts):
    for dirpath, _dirnames, filenames in os.walk(dpath):
        for name in sorted(filenames):
            if os.path.splitext(name)[1].lower() in exts:
                yield os.path.join(dirpath, name)


def check_file_for_banned_phrases(path, phrases=None):
    """Return a list of (lineno, message) tuples for one file, one per
    banned-phrase occurrence. Case-insensitive substring match."""
    phrases = phrases if phrases is not None else BANNED_PHRASES
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                lowered = line.lower()
                for phrase in phrases:
                    if phrase.lower() in lowered:
                        errors.append((lineno, f"banned phrase found: '{phrase}'"))
    except (OSError, UnicodeDecodeError) as exc:
        errors.append((0, f"could not read file: {exc}"))
    return errors


def check_file_for_banned_cta_regression(path, phrases=None):
    """Return a list of (lineno, message) tuples flagging a banned CTA phrase
    that appears in a template's own example/scaffold text rather than being
    named as forbidden. Two ways a hit is treated as a legitimate mention
    (skipped, not flagged) instead of a regression:

    1. A negation marker (see `_NEGATION_MARKERS`) appears anywhere on the
       same line as the match - the line is a single CTA-rule bullet, so a
       marker anywhere on it (before or after the phrase) describes that
       same example, not just the ones within a fixed distance.
    2. Inside a "DO NOT USE" style block: a heading line opens the block,
       every following bullet line (`-`/`*`) stays inside it, and the block
       closes at the first blank line or first non-bullet line.

    Matching uses word boundaries (`\\b`), not a raw substring test, so a
    single-word phrase like "Discover" does not false-positive on unrelated
    words that merely contain it as a substring, e.g. "discovery" or
    "discoverability" (both appear as legitimate SEO/hashtag terminology in
    these templates).
    """
    phrases = phrases if phrases is not None else BANNED_CTA_PHRASES
    patterns = [
        (phrase, re.compile(r"\b" + re.escape(phrase.lower()) + r"\b"))
        for phrase in phrases
    ]
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (OSError, UnicodeDecodeError) as exc:
        return [(0, f"could not read file: {exc}")]

    in_banned_block = False
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        lowered = stripped.lower()

        if not stripped:
            in_banned_block = False
            continue

        if any(h in lowered for h in _NEGATION_HEADERS):
            in_banned_block = True
            continue

        if in_banned_block:
            if stripped.startswith("-") or stripped.startswith("*"):
                continue
            in_banned_block = False

        if any(marker in lowered for marker in _NEGATION_MARKERS):
            continue

        for phrase, pattern in patterns:
            if pattern.search(lowered):
                errors.append((
                    lineno,
                    f"banned CTA phrase '{phrase}' used outside a "
                    "DO-NOT-USE list (possible template regression)",
                ))
    return errors


def run_banned_cta_regression_check(root):
    total = 0
    checked = 0
    for rel in _iter_banned_cta_regression_targets(root):
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            print(f"error: not a file: {rel}")
            total += 1
            continue
        checked += 1
        for lineno, msg in check_file_for_banned_cta_regression(path):
            print(f"{rel}:{lineno}: error: {msg}")
            total += 1
    if total:
        print(f"\n{total} banned-CTA-regression violation(s) found.")
        return 1
    print(f"Banned-CTA-regression check passed ({checked} file(s) checked).")
    return 0


def run_banned_phrases_check(target_dir, root):
    dpath = target_dir if os.path.isabs(target_dir) else os.path.join(root, target_dir)
    total = 0
    if not os.path.isdir(dpath):
        print(f"error: not a directory: {target_dir}")
        return 1
    for path in _iter_files_under(dpath, BANNED_PHRASE_EXTS):
        for lineno, msg in check_file_for_banned_phrases(path):
            rel = os.path.relpath(path, root)
            print(f"{rel}:{lineno}: error: {msg}")
            total += 1
    if total:
        print(f"\n{total} banned-phrase violation(s) found.")
        return 1
    print("Banned-phrase check passed.")
    return 0


_URL_RE = re.compile(r'https?://[^\s\)"\'>\]]+')
_URL_CHECK_TIMEOUT = 8  # seconds


def extract_urls(path):
    """Return a list of (lineno, url) tuples from markdown links and bare URLs in a file."""
    found = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                for url in _URL_RE.findall(line):
                    # Strip trailing punctuation that's not part of the URL
                    url = url.rstrip(".,;:!?)")
                    found.append((lineno, url))
    except (OSError, UnicodeDecodeError):
        pass
    return found


def check_url(url):
    """Return (status_code, error_str). status_code is None on network error."""
    try:
        req = urllib.request.Request(url, method="HEAD",
                                     headers={"User-Agent": "Mozilla/5.0 (content-wiz linter)"})
        with urllib.request.urlopen(req, timeout=_URL_CHECK_TIMEOUT) as resp:
            return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, str(e)


def run_url_check(target_dir, root):
    """Check all URLs found in .md and .txt files under target_dir. Report dead links."""
    dpath = target_dir if os.path.isabs(target_dir) else os.path.join(root, target_dir)
    if not os.path.isdir(dpath):
        print(f"error: not a directory: {target_dir}")
        return 1

    all_urls = {}  # url -> [(rel_path, lineno)]
    for path in _iter_files_under(dpath, {".md", ".txt"}):
        rel = os.path.relpath(path, root)
        for lineno, url in extract_urls(path):
            all_urls.setdefault(url, []).append((rel, lineno))

    if not all_urls:
        print("No URLs found.")
        return 0

    print(f"Checking {len(all_urls)} unique URL(s)...")
    dead = []
    for url, locations in sorted(all_urls.items()):
        status, err = check_url(url)
        if status is None:
            tag = f"TIMEOUT/ERROR ({err})"
            dead.append((url, locations, tag))
        elif status >= 400:
            tag = f"HTTP {status}"
            dead.append((url, locations, tag))
        else:
            print(f"  OK  {status}  {url}")

    if dead:
        print(f"\n{len(dead)} dead link(s) found:")
        for url, locations, tag in dead:
            for rel, lineno in locations:
                print(f"  {rel}:{lineno}: {tag}  {url}")
        return 1

    print(f"\nAll {len(all_urls)} URL(s) returned 2xx/3xx.")
    return 0


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    root = os.path.dirname(os.path.abspath(__file__))

    if argv and argv[0] == "--check-urls":
        rest = argv[1:]
        if not rest:
            print("error: --check-urls requires a directory argument (e.g. output/)")
            return 1
        return run_url_check(rest[0], root)

    if argv and argv[0] == "--check-banned-phrases":
        rest = argv[1:]
        if not rest:
            print("error: --check-banned-phrases requires a directory argument")
            return 1
        return run_banned_phrases_check(rest[0], root)

    targets = argv if argv else list(_iter_default_targets(root))

    total = 0
    for path in targets:
        for lineno, msg in check_file(path):
            rel = os.path.relpath(path, root)
            print(f"{rel}:{lineno}: error: {msg}")
            total += 1

    if total:
        print(f"\n{total} content-rule violation(s) found.")
        return 1
    print(f"Content lint passed ({len(targets)} file(s) checked).")

    return run_banned_cta_regression_check(root)


if __name__ == "__main__":
    sys.exit(main())
