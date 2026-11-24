#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line -- the excuse a robot vacuum gives after eating a
sock -- to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when that
variable is set. Deterministic, offline, no trailing newline.
"""

import os
from pathlib import Path

LINE = "It's wrapped around my brush and won't come off. We're engaged."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
