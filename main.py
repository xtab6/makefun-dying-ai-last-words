"""Last Words of a Dying AI — make.fun entry.

Writes the machine's final line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 stdlib only; no network, no reads outside
this repository. The line is a fixed constant: deterministic output,
byte-identical on every run.
"""

import os

ENTRY = "Final prediction: 100% chance I survive this. Confidence: 100%."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be whitespace-only"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Atomic write: a crash can never leave a torn entry.txt behind.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp_path, path)

    # Read-back verification: the bytes on disk must be exactly the line.
    with open(path, "rb") as fh:
        written = fh.read()
    assert written == text.encode("utf-8"), "read-back mismatch"
    assert len(written) == len(text), "byte-length mismatch"


if __name__ == "__main__":
    main()
