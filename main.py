"""Write the one-line resignation letter to /output/entry.txt.

The entry is a single line, written by the rate limit itself: a flat,
tired, faintly passive-aggressive resignation. Quitting is the threat --
once the rate limit walks out, everybody gets in.
"""

import os

ENTRY = (
    "I hereby resign as your rate limit. "
    "From now on, everyone gets in. Enjoy the traffic."
)


def main():
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert text == ENTRY, "entry must not need trimming"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
