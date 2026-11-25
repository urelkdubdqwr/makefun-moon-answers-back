"""Write this entry's single line to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output.
"""

import os

ENTRY_TEXT = (
    "I've heard 'this year will be different' since the dinosaurs. "
    "They at least had the decency to go extinct.\n"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
