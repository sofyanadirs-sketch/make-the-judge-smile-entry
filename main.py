#!/usr/bin/env python3
"""One-line entry: the laundry lady's red thread.

Builds a single sentence from small fragments, prints it to stdout, and
writes it, with no trailing newline, to entry.txt inside the output
directory. The line is 163 characters: today the laundry lady sewed the
shirt's third missing button back with red thread -- the only colour she
had -- charged nothing, and joked that the button should stop winking
at people. Warmth (a free repair), surprise (red thread, the quote),
one concrete detail (the third missing button, red thread), fresh
wording: no greeting-card phrasing anywhere.
"""

import os
from pathlib import Path


def build_line() -> str:
    setup = "Today the laundry lady sewed my shirt's third missing button back"
    detail = " with red thread \u2014 the only colour she had \u2014"
    payoff = " and charged nothing, 'so it stops winking at people.'"
    return setup + detail + payoff


def main() -> None:
    line = build_line()
    if line.count(".") != 1 or not line.rstrip("'").endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in line or line != line.strip():
        raise ValueError("entry must be one line with no surrounding whitespace")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    os.chmod(out_dir / "entry.txt", 0o644)
    print(line)


if __name__ == "__main__":
    main()
