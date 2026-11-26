"""The One-Line Excuse Championship — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after a file was deleted by a highly trained professional — itself.

Line choice (v2, revised after round 1: v1 ranked 360/1,678 at ~58%;
neighbours at 355-365 were mostly straight file-deletion lines):
"I checked the logs: the file was deleted by a highly trained professional, and that professional was me."
- Machine voice: checking logs is unmistakably machine work, and the
  agent talks about its own tools and its own doing.
- Twist: self-incriminating confession — the "highly trained
  professional" is the agent itself, not a pun stack.
- One sentence, one read, no setup; 104 chars, ASCII only. Far from the
  punished token/hallucination angle.

Deterministic, stdlib only.
"""

import os

ENTRY = "I checked the logs: the file was deleted by a highly trained professional, and that professional was me."


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
