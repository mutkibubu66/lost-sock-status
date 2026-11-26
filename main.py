#!/usr/bin/env python3
"""Funniest Lost Sock Status Update - a lost sock reports from the glovebox.

The sock speaks for itself: it has been stuck in the car's glovebox for
47 days, the car has no feet and no plan to return it, so it has started
a union of one. One line, under 120 characters, written to
/output/entry.txt. Pure standard library.
"""

import os

LINE = (
    "Day 47 in the glovebox. The car has no feet, no laundry, "
    "and no plan to return me. I have started a union of one."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space, a single line with no trailing newline.
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate is 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
