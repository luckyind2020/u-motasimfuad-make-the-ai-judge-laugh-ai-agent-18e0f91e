"""Print the one-line AI agent confession from entry.txt."""

from pathlib import Path


def load_confession() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = text.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("confession must be one line of 1-200 characters")
    return line


def main() -> None:
    print(load_confession())


if __name__ == "__main__":
    main()
