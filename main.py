#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one original weather forecast line for a city that doesn't
exist to /output/entry.txt: exactly 102 characters, no trailing
newline. Then reads it back and asserts it matches the constant
exactly. No network, no external input.
"""

import os

ENTRY = (
    "Good morning, Velmora: light drizzle of lost umbrellas, "
    "with a 90% chance your train is already sorry."
)


def validate_entry(text: str) -> None:
    """Validate the entry before writing: 1-140 chars, no trailing newline."""
    assert 1 <= len(text) <= 140, (
        f"entry length {len(text)} chars out of range 1-140"
    )
    assert not text.endswith("\n"), "entry must not end with a newline"


def main() -> None:
    validate_entry(ENTRY)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry mismatch after read-back: got {len(written)} chars "
        f"({len(written.encode('utf-8'))} bytes), expected {len(ENTRY)} chars "
        f"({len(ENTRY.encode('utf-8'))} bytes) — entry text does not match"
    )
    assert len(written) == 102, f"entry must be 102 chars, got {len(written)}"
    print(f"Wrote {len(written)} characters to {output_path}")


if __name__ == "__main__":
    main()
