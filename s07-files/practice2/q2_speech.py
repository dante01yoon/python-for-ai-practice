from pathlib import Path

Path("speech.txt").write_text(
    "Four score and seven years ago our fathers brought forth on this continent, a new nation,\n"
    "conceived in Liberty, and dedicated to the proposition that all men are created equal.\n"
)
words = 0
with open("speech.txt") as f:
    for line in f:
        words += len(line.split())
print("Words:", words)
