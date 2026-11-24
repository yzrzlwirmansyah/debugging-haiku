"""Seventeen Syllables of Debugging — make.fun entry.

Writes the debugging haiku to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), then re-reads the file and verifies its bytes
match the haiku exactly, that it is 1-200 chars, and valid UTF-8.
Standard library only, deterministic.
"""

import os

HAIKU = "cursor blinks at three\nthe log line repeats itself\nit was my typo\n"


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
    text = data.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= 200, "entry.txt length out of range (1-200 chars)"


if __name__ == "__main__":
    main()
