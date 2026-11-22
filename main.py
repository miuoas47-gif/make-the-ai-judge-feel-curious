#!/usr/bin/env python3
"""Write one short text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the text is a fixed string, so every run produces
byte-identical output.
"""

import os
import sys

TEXT = (
    "The lighthouse keeper still lights the lamp each night, though no ship "
    "has passed in eleven years. He polishes the glass and writes the weather "
    "in a book nobody reads. Last Tuesday the lamp burned blue for nine "
    "seconds. He has told no one."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(".", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
