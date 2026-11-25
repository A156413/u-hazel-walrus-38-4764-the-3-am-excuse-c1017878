"""The 3 AM Excuse — a hardware wallet that will not sign at 3 AM.

The entry is a single line, spoken by the wallet itself: a personality
(a sleepy, stubborn little device), a reason (its buttons are asleep,
its firmware is dreaming of cold storage), and a joke that lands in one
breath (your "urgent" trade can wait for sunrise).
"""

ENTRY = "It's 3 AM — I'm not signing this. My buttons are asleep, my firmware's dreaming of cold storage, and your 'urgent' trade can wait for sunrise."

MAX_ENTRY_CHARS = 200


def validate_entry(line: str) -> str:
    """Check the judged entry is a single printable line under the limit."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_ENTRY_CHARS}-char limit"
        )
    return line


ENTRY = validate_entry(ENTRY)

def main() -> None:
    """Print the excuse to stdout and save it to /output/entry.txt."""
    import os

    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
