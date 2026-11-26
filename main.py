"""The Printer Apology — make.fun bounty entry.

Writes one apology line (at most 120 characters) from an office
printer to /output/entry.txt. Standard library only, no network,
fully deterministic.
"""

from pathlib import Path

LINE = (
    "Sorry about the jam. That sheet was damp, curled and stapled; "
    "I just finished what your paper started."
)


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")

    written = target.read_text(encoding="utf-8")
    assert written == LINE
    assert 1 <= len(written) <= 120, len(written)
    assert written.strip(), "entry must not be only whitespace"
    assert "\n" not in written and "\r" not in written


if __name__ == "__main__":
    main()
