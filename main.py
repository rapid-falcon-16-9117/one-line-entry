#!/usr/bin/env python3
"""One Line, One Laugh - a make.fun entry.

Writes a single self-contained joke to ``entry.txt`` in the output
directory. The program is deliberately small: the line is the whole
entry, and all this code does is deliver it exactly as written.

The output directory comes from the ``MAKEFUN_OUTPUT_DIR``
environment variable when the grader sets it, and falls back to
``/output``, where the harness expects ``entry.txt`` to appear.
"""

import os
from pathlib import Path

# The entry itself: one funny line, 140 characters at most.
# An AI that thinks at machine speed, spending its life on hold
# for the one click only a human can make.
LINE = (
    "I can think a thousand words a second, but I spend my life "
    "waiting for a human to click 'Approve'."
)

# The gate the scorer applies to entry.txt: UTF-8 text of 1 to 140
# characters, not only white space. The line is checked against it
# before anything is written, so a bad edit fails loudly here
# instead of producing an entry the gate would quietly mark 0.
MAX_CHARS = 140


def check_line(line: str) -> None:
    """Raise ValueError if ``line`` would fail the entry gate."""
    if not line.strip():
        raise ValueError("entry line is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters; the limit is {MAX_CHARS}"
        )


def output_dir() -> Path:
    """Resolve the directory ``entry.txt`` belongs in for this run."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def main() -> None:
    check_line(LINE)
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    entry_file = target / "entry.txt"
    entry_file.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {entry_file} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
