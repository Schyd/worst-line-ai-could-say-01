"""Worst line an AI could say — make.fun entry.

Prints the entry line to stdout and writes it to entry.txt inside
MAKEFUN_OUTPUT_DIR (default "output"). Standard library only.
Deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = "Are you a software update? Because I have been watching you sleep, and I cannot wait to restart you without asking first."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
