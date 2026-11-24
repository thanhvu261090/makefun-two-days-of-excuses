#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes a single-line excuse, in the voice of an AI agent that missed
its deadline, to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os
import sys

ENTRY = (
    "I estimated the job at 0.4 seconds with 99.9% confidence \u2014 "
    "the remaining 0.1% has been running for two days."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def gate_check(text: str) -> None:
    """Enforce the kit gate exactly: UTF-8 text, 1 to 200 characters,
    not only whitespace, a single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8 text
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, must be 1 to {MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry contains control characters")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")


def main() -> int:
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
