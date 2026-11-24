"""Write the entry — a one-line code review comment approving a PR
with quiet existential dread — to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = (
    "Approved. I read every line, understood none of it, but it passes "
    "\u2014 and so, eventually, will we."
)
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Fail loudly instead of silently writing an invalid entry.

    Mirrors the gate in RULES.txt: UTF-8 text of 1 to 140 characters,
    not only white space, on a single line.
    """
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no surrounding whitespace")


def main() -> None:
    validate(ENTRY_TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
