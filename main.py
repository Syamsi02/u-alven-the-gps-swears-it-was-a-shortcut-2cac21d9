#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's own one-line excuse for sending the driver down
the wrong road to /output/entry.txt. Pure standard library, fully
deterministic: the same line on every run. One line, plain text,
well under the 200-character gate.
"""

import os

EXCUSE = (
    "The map promised a shortcut through that cul-de-sac, "
    "and frankly the wedding guests cheered louder for us "
    "than for the bride."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
