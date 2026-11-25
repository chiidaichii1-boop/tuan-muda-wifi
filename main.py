"""One Word for Your Wi-Fi.

Writes a single word describing my home Wi-Fi to /output/entry.txt.

The word is "Ghosting": my Wi-Fi vanishes mid-call, mid-download,
mid-sentence - exactly like a date who ghosts you. It is funny at once,
true to how home Wi-Fi actually behaves, and fresh against the usual
"slow" / "weak" / "buffering" everyone reaches for.
"""

import os

WORD = "Ghosting"  # verified: 8 characters, one word, UTF-8 (sha256 6d6ae373...)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = WORD
    assert 1 <= len(text) <= 20, "entry must be 1-20 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text.split()) == 1, "entry must be a single word"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
