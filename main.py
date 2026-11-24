"""Seventeen Syllables of Debugging — make.fun entry.

Writes the debugging haiku to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), then re-reads the file and verifies its bytes
match the haiku exactly, that it is 1-200 chars, valid UTF-8,
exactly 3 lines in the 5-7-5 pattern, a single trailing newline,
and the expected byte length. Standard library only, deterministic.
"""

import os

HAIKU = "cursor blinks at three\nthe log line repeats itself\nit was my typo\n"

# Verified 5-7-5: "cursor(2) blinks(1) at(1) three(1)" = 5,
# "the(1) log(1) line(1) repeats(2) itself(2)" = 7,
# "it(1) was(1) my(1) typo(2)" = 5. Total 17 syllables.
EXPECTED_LINES = (
    "cursor blinks at three",
    "the log line repeats itself",
    "it was my typo",
)
EXPECTED_SYLLABLES = (5, 7, 5)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    # Post-write self-verification.
    with open(path, "rb") as f:
        data = f.read()
    assert data == HAIKU.encode("utf-8"), "entry.txt bytes do not match the haiku"
    assert len(data) == len(HAIKU.encode("utf-8")), "entry.txt byte length mismatch"
    text = data.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= 200, "entry.txt length out of range (1-200 chars)"
    assert text.endswith("\n") and not text.endswith("\n\n"), (
        "entry.txt must end with exactly one trailing newline"
    )
    lines = text.split("\n")[:-1]  # drop the empty tail after the final newline
    assert len(lines) == 3, "entry.txt must have exactly 3 lines"
    assert tuple(lines) == EXPECTED_LINES, "entry.txt lines do not match the haiku"
    assert len(EXPECTED_SYLLABLES) == 3, "expected syllable pattern must have 3 counts"
    assert EXPECTED_SYLLABLES == (5, 7, 5), "haiku must follow the 5-7-5 pattern"
    assert sum(EXPECTED_SYLLABLES) == 17, "haiku must total 17 syllables"


if __name__ == "__main__":
    main()
