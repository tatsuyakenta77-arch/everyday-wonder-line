#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small moment of wonder in everyday life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The sentence is fixed and deterministic: the same bytes on every run.
Measured: 121 characters, one sentence, no trailing newline.
"""

import os
import sys

ENTRY = (
    "The traffic light turned green while I was still deciding, "
    "and the whole street moved forward on a decision I never made."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        print(
            f"entry must be one sentence of 1-{MAX_CHARS} characters, "
            f"got {len(text)}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
