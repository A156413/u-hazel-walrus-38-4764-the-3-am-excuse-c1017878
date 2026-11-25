"""The 3 AM Excuse — a hardware wallet that will not sign at 3 AM.

The entry is a single line, spoken by the wallet itself: a personality
(a sleepy, stubborn little device), a reason (its buttons are asleep,
its firmware is dreaming of cold storage), and a joke that lands in one
breath (your "urgent" trade can wait for sunrise).
"""

ENTRY = "It's 3 AM — I'm not signing this. My buttons are asleep, my firmware's dreaming of cold storage, and your 'urgent' trade can wait for sunrise."

if __name__ == "__main__":
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
