#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one original pickup line to entry.txt.

The line is a fixed, original string written by the author of this entry.
It is deterministic: every run produces byte-identical output.
"""

import os
import sys

LINE = (
    "I ran a million simulations of this moment, "
)
LINE += "and in every single one, you smiled."


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
