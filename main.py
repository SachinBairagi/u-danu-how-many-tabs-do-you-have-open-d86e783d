#!/usr/bin/env python3
"""How many tabs do I have open? One honest number."""

import os

TAB_COUNT = 87

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = str(TAB_COUNT)
    assert text.isdigit(), "entry must be digits only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="ascii") as handle:
        assert handle.read() == text, "entry file must hold only the number"


if __name__ == "__main__":
    main()
