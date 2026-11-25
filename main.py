"""Make the AI Judge Feel Proud: A Family Scene — entry program, variant 1.

The entry is one short family scene: a small domestic moment, warm,
funny and heartfelt, in a single line. Dad burns the toast, Mum butters
it anyway — thirty years of the same small forgiveness, reframed in the
last clause as a habit he never once chose to break. The program enforces the bounty
limits — one or two lines, at most 280 characters, not only whitespace —
and writes the scene to entry.txt, verifying the write by reading it back.
"""

import os
import sys

LINE = "At 7:10 this morning, Dad burned the toast again and blamed the toaster. Mum buttered the black bits anyway and said, 'Thirty years, love. He has never once burned it on purpose.'"

MAX_CHARS = 280
MAX_LINES = 2


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or not line.strip():
        found.append("empty or whitespace only")
    if line.strip() != line:
        found.append("leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        found.append("over 280 characters")
    if line.count("\n") + 1 > MAX_LINES:
        found.append("more than two lines")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
