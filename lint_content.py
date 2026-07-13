"""Content-rule linter. Enforces the project's hard content rules on the files
that feed the generator, so violations cannot silently land.

Currently enforced (error): no em-dash (U+2014) anywhere in prompt/strategy/
template source. Warnings are advisory and never fail the build.

Usage:
    python lint_content.py            # lint the default fileset
    python lint_content.py path ...   # lint specific files

Exit code 1 if any error is found.
"""
import os
import sys

EM_DASH = "—"

# Files the linter should never scan: they reference the banned character on
# purpose (to detect it) and would otherwise self-flag.
SELF_REFERENTIAL = {"lint_content.py", "test_generate.py"}

DEFAULT_TARGET_DIRS = ["prompts", "strategies", "templates"]
DEFAULT_TARGET_FILES = ["generate.py", "textprompts.py", "README.md"]

SCAN_EXTS = {".txt", ".md", ".py", ".csv"}


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


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    root = os.path.dirname(os.path.abspath(__file__))
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
