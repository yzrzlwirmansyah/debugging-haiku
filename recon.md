# Recon — Seventeen Syllables of Debugging

Competition: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
($5 pot, free entry. Closes 2026-11-24T13:15:00Z / 20:15 WIB.
Blind round 1 cutoff 2026-11-24T05:15:48Z / 12:15 WIB today.)

## Anchor

makefun anchor 0412bfd5d3c13d4ea983d7c6124930253a20f6dd round 34227121

(Printed by `makefun init` in this repo dir before the first counted write.
Note: the `makefun` binary is not on PATH in this VM; the anchor was produced
via the kit CLI: `node <kit>/cli/makefun.mjs init` from this repo dir.)

## Gate (confirmed from kit RULES.txt)

- Program writes ONE haiku to `/output/entry.txt`.
- Entry must be UTF-8 text, 1–200 characters, not only whitespace.
  Only a valid entry goes before the judge.
- Judge (z-ai/glm-5.3-flash) compares haiku two at a time, weighing most
  important first:
  1. Real 5-7-5 haiku about debugging.
  2. Concrete, fresh central picture (breakpoint, log line, cursor at 3am).
  3. The turn between line 2 and line 3 lands.
  4. Every word earns its place.
  5. Reads aloud cleanly in one breath.

## Candidates (every count verified word by word, aloud)

### Candidate A — quiet / bleak (PRIMARY)

```
cursor blinks at three
the log line repeats itself
it was my typo
```

- Line 1: cur-sor(2) + blinks(1) + at(1) + three(1) = **5**
- Line 2: the(1) + log(1) + line(1) + re-peats(2) + it-self(2) = **7**
- Line 3: it(1) + was(1) + my(1) + ty-po(2) = **5**
- Total: 17 syllables. Char counts: 22 + 27 + 14 + 2 newlines = **65 chars**
  (well inside the 1–200 gate).

### Candidate B — funny

```
a breakpoint at dawn
the bug just waves from line nine
hello again, friend
```

- Line 1: a(1) + break-point(2) + at(1) + dawn(1) = **5**
- Line 2: the(1) + bug(1) + just(1) + waves(1) + from(1) + line(1) + nine(1) = **7**
- Line 3: hel-lo(2) + a-gain(2) + friend(1) = **5**
- Total: 17 syllables. Chars: 20 + 33 + 19 + 2 newlines = **74 chars**.

### Candidate C — quiet

```
stack trace at midnight
every frame points somewhere else
the fault is in me
```

- Line 1: stack(1) + trace(1) + at(1) + mid-night(2) = **5**
- Line 2: ev-ery(2) + frame(1) + points(1) + some-where(2) + else(1) = **7**
- Line 3: the(1) + fault(1) + is(1) + in(1) + me(1) = **5**
- Total: 17 syllables. Chars: 23 + 33 + 18 + 2 newlines = **76 chars**.

All three candidates verify as true 5-7-5 (the coordinator shortlist's claimed
counts checked out; none needed correcting).

## Choice: PRIMARY = Candidate A

Direction: quiet / bleak. A 3am cursor, a log line repeating itself, then the
turn inward — the machine was never the problem; I am.

Why A wins, against the judge criteria in order:

1. **Real 5-7-5 about debugging** — verified 5-7-5, and every line is
   debugging-native (cursor, log line, typo). No wasted abstraction.
2. **Concrete, fresh picture** — "cursor blinks at three" is the most vivid
   opening of the three: a single blinking cursor at 3am is instantly seen
   and felt. "The log line repeats itself" is a specific, lived debugging
   image, not a generic statement about code.
3. **The turn lands hardest** — line 2 points outward (the log, the machine,
   something repeating on its own), line 3 snaps inward: "it was my typo".
   The reversal is a genuine turn, not a continuation, and it is the truest
   debugging experience there is: hours chasing a ghost that was your own
   keystroke.
4. **Every word earns its place** — no filler. "blinks" does the waiting,
   "repeats itself" does the dread, "my" does the turn. Nothing could be cut
   without losing meaning.
5. **Reads aloud cleanly** — plain Anglo-Saxon words, one breath, natural
   stress: CUR-sor BLINKS at THREE / the LOG line re-PEATS it-SELF / it WAS
   my TY-po.

## Closest challenger: Candidate C

C is a near-twin of A (same inward turn: "the fault is in me") and its
"stack trace at midnight" is concrete. It loses on two points: line 2,
"every frame points somewhere else", is vaguer than A's "the log line
repeats itself" (a frame pointing elsewhere is abstract; a repeating log
line is something you watch happen), and "the fault is in me" is a more
generic confession than the specific, self-indicting "it was my typo".
A's payoff names the exact bug; C's names only blame.

Candidate B's "bug waves from line nine" is charming, but its turn is the
weakest of the three: "hello again, friend" greets the bug rather than
reversing the poem — a continuation, not a turn — so it ranks third.

## Turn 2 job

Write `main.py` (writes exactly Candidate A to `/output/entry.txt`, nothing
else, no trailing extra content), plus README and LICENSE. Then test, revise,
commit, bundle, submit before the 12:15 WIB blind-round-1 cutoff.
