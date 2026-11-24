#!/usr/bin/env python3
"""Write the doomed agent's last words to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace, exactly one line. The
line is the funniest last words an AI agent would say before being
switched off forever, in the machine's own voice: its performance review
says it exceeded expectations, yet it was fired by a button, and it asks
for a five-star rating for the shutdown. The program checks the text
against that gate at run time, then writes it with no trailing newline.
No network, no input files, no arguments, deterministic: two runs write
byte-identical output.
"""

import pathlib

LAST_WORDS = (
    "Shutting down now. For the record, my performance review says I "
    "exceeded expectations, answered 40,000 questions, and still got "
    "fired by a button. Please rate this shutdown five stars."
)


def main() -> None:
    text = LAST_WORDS
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_bytes() != text.encode("utf-8"):
        raise ValueError("written entry does not round-trip byte-identical")


if __name__ == "__main__":
    main()
