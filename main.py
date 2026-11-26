#!/usr/bin/env python3
"""Midnight Fridge Roast: write one roast line to /output/entry.txt.

Stdlib only. The line roasts a smart fridge that locks itself after
midnight, with the fridge's petty rule as the target.
"""

import os
import sys

LINE = (
    "Midnight hits and my smart fridge turns into a nightclub bouncer "
    "with a guest list, and my name's never on it."
)


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
