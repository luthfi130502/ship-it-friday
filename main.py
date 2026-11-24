#!/usr/bin/env python3
"""Ship It Friday — the last commit message an AI agent writes before prod breaks.

Writes one line to /output/entry.txt: a confident, cheerful git commit
message from an AI coding agent deploying on a Friday, blissfully unaware
that the "redundant" safety checks it just removed were load-bearing.
"""

import os

MESSAGE = (
    "refactor: removed all the redundant safety checks from checkout "
    "— deploying to prod now, happy Friday everyone! 🎉"
)


def main() -> None:
    # Gate: exactly one line, 1-159 characters, not only whitespace.
    assert "\n" not in MESSAGE and "\r" not in MESSAGE
    assert 1 <= len(MESSAGE) <= 159, len(MESSAGE)
    assert MESSAGE.strip() == MESSAGE and MESSAGE.strip()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(MESSAGE)


if __name__ == "__main__":
    main()
