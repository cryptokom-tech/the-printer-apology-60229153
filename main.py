#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Printer Apology'.

Writes a single printer apology line to /output/entry.txt.
Uses only the Python standard library and is deterministic:
every run produces byte-identical output.
"""

import os

ENTRY_TEXT = "Sorry about the jam. That sheet was damp, curled and stapled; I just finished what your paper started."
OUTPUT_PATH = "/output/entry.txt"


def check_entry(text):
    """Guard the bounty gate: 1-120 UTF-8 chars, one line, not blank."""
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry():
    check_entry(ENTRY_TEXT)
    directory = os.path.dirname(OUTPUT_PATH)
    os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    # Read back so a truncated or corrupted write fails loudly here,
    # rather than silently producing an invalid entry for the judge.
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY_TEXT:
        raise ValueError("written entry does not match ENTRY_TEXT")
    check_entry(written)


if __name__ == "__main__":
    write_entry()
