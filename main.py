#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entrypoint.

Writes the single entry letter to /output/entry.txt so the make.fun
gate sees UTF-8 text of exactly 1 character, not only whitespace.

Entry: A (coffee).
"""

from __future__ import annotations

import os

# The entry: exactly one character. A = coffee, B = tea.
ENTRY_LETTER: str = "A"

OUTPUT_PATH = "/output/entry.txt"


def validate(letter: str) -> str:
    """Assert the entry is exactly one non-whitespace character."""
    assert len(letter) == 1, f"entry must be exactly 1 character, got {len(letter)}"
    assert letter.strip(), "entry must not be only whitespace"
    return letter


def main() -> None:
    letter = validate(ENTRY_LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(letter)
    print(letter)


if __name__ == "__main__":
    main()