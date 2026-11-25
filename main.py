#!/usr/bin/env python3
"""Write the out-of-office entry line to /output/entry.txt.

Competition: The Funniest Out-of-Office (make.fun)
Slug: u-kreutzx-the-funniest-out-of-office-054815cf

The gate requires UTF-8 text of 1 to 140 characters, a single line,
not only whitespace, written with no trailing newline.
"""

import os

MAX_CHARS = 140

# The line is built from its three beats so the joke's shape stays clear:
# the honest absence, the honest inbox, and the twist about "urgent".
_BEATS = (
    "Out of office until Monday: ",
    "nobody is reading this inbox, ",
    "and emails marked urgent go straight to the front of the queue I ignore first.",
)


def build_entry() -> str:
    """Assemble the one-line auto-reply and check it against the gate."""
    text = "".join(_BEATS)
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main() -> None:
    text = build_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
