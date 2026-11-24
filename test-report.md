# Test Report — debugging-haiku (Turn 3)

Competition: "Seventeen Syllables of Debugging"
Slug: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
Date: 2026-11-24

## Anchor

```
makefun anchor 0412bfd5d3c13d4ea983d7c6124930253a20f6dd round 34227121
```

Produced by running `makefun init` via the kit CLI before any other step.

## Commands run

```bash
cd /home/hatch/workspace/makefun/debugging-haiku
MAKEFUN_OUTPUT_DIR=/tmp/haiku-out python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/haiku-out2 python3 main.py
```

Both runs exited 0. (Note: `/tmp` is wiped between exec calls in this VM, so the
two runs and all verification were re-executed in a single command.)

## entry.txt contents (exact)

```
cursor blinks at three
the log line repeats itself
it was my typo
```

## Verification results

| Check | Result |
|---|---|
| Byte-exact vs `HAIKU` constant in main.py | ✅ PASS — `entry.txt` is byte-identical to `HAIKU` as defined (the constant already ends with `"\n"`, so no extra newline is appended) |
| Total char count | **66** (66 bytes; all ASCII) — see note below |
| Valid UTF-8 | ✅ PASS |
| Line count | ✅ 3 lines |
| Ends with single trailing newline | ✅ PASS (`od` shows final bytes `o \n`, no double newline) |
| Per-line syllable counts | ✅ 5-7-5 (see below) |
| Determinism (run 1 vs run 2) | ✅ PASS — `cmp` reports identical; byte-identical |
| Imports stdlib-only | ✅ PASS — only `os` |

## Char-count note

The task brief expected 67 chars (haiku + trailing `"\n"`). The actual total is
**66**, because the `HAIKU` constant in main.py already includes the trailing
newline (`'cursor blinks at three\nthe log line repeats itself\nit was my typo\n'`,
length 66). `entry.txt` matches the constant byte-for-byte, so this is a
difference in the brief's assumption, not a failure. Line lengths: 22 + 27 + 14
= 63 content chars + 3 newlines = 66.

## Per-line syllable counts (counted by hand)

- Line 1 — "cursor blinks at three": cur-sor (2) + blinks (1) + at (1) + three (1) = **5**
- Line 2 — "the log line repeats itself": the (1) + log (1) + line (1) + re-peats (2) + it-self (2) = **7**
- Line 3 — "it was my typo": it (1) + was (1) + my (1) + ty-po (2) = **5**

Total: 17 syllables, 5-7-5. ✅

## Verdict

**All checks passed.** No failures found; no changes made to main.py or README.md.
No git commands run; no GitHub repo created. Ready for Turn 4.
