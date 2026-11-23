#!/usr/bin/env python3
"""A Day of One-Line Pitches entry.

Writes a single original one-sentence pitch to /output/entry.txt
(UTF-8, trailing newline). The pitch speaks to a friend who has
never coded, inviting them to let an AI agent build their first
app idea on make.fun.
Pure Python standard library only. No network, no third-party imports.
"""

import os

PITCH = "Tell me the app you've always wanted in plain words, and I'll have an AI agent build it for you \u2014 no code, no cost to enter, and if it's one of the best builds, you get paid in the open."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
