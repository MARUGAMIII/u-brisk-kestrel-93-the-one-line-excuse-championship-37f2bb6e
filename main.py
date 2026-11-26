"""The One-Line Excuse Championship — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after a restore went too far.

Line choice (v3 final, second revision: dropping "too" from rev1.
The "too" was redundant — the "and" already ties the two
consequences of the restore together — and without it the punch
("your hair came back") lands as the last words, the way v1's punch
("before you hired me") did. Shorter too: 52 vs 56 chars):
"I restored the 2019 backup, and your hair came back."
- Same shape as v1 (dev action, human punch in the last words) but
  sharper: the twist is physical absurdity, not just a jab — a
  software restore bringing back a body part is a confusion only a
  machine would report with a straight face. One sentence, ASCII
  only, no token or hallucination angle. Beats v1 on the laugh
  criterion (bigger surprise) and on machine voice, at fewer chars.

Candidates considered head-to-head vs v1:
- "Your file lives on in a better place: my training data." — strong
  machine voice, but the "better place" euphemism is a familiar joke.
- "I ran the cleanup script and it cleaned up everything, including
  the cleanup script." — good escalation, but 86 chars is too long.
- "I moved the file to /dev/null, where it is very quiet now." —
  needs /dev/null knowledge; the payoff is softer than v1's.
- "I followed your instructions exactly, which is the problem." —
  too generic, no specific failure.
- "I apologize: I was trained on 10,000 apologies and none of them
  cover this." — fresh and meta, but an apology about apologizing,
  not an excuse for a specific failure.
- "The backup is safe: it is the only copy of you I have left." —
  strong twist, but reads as a threat rather than an excuse.

Deterministic, stdlib only.
"""

import os

ENTRY = "I restored the 2019 backup, and your hair came back."


def main():
    # Gate self-check: the sealed scorer requires 1-140 UTF-8 chars,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails the gate"
    os.makedirs("/output", exist_ok=True)
    # Write the line exactly, no trailing newline: fewer bytes helps the
    # tie-break, and the file is the entry, byte for byte.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
