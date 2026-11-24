"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — an alien tourist's review of Earth —
to /output/entry.txt (UTF-8, single line, at most 200 characters).
"""

import os

ENTRY = (
    "Came for the beaches, stayed for the tacos. Gravity is a bit much, "
    "the locals keep asking my star sign, and checkout is at 11am sharp. "
    "Four stars \u2014 would abduct again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
