"""Two Days of Quiet Dread — one code-review line that approves a PR.

The program writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt:
an approval carrying quiet existential dread, flat and understated,
the way a tired engineer would paste it before clicking approve.
Gate: UTF-8 text of 1 to 140 characters, not only white space.
This line is 107 characters on one line.
"""

import os

LINE = "LGTM. Clean diff, green tests, and someday this repo will be the only record that any of us were ever here."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
