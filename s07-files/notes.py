# Text files: write, append, read
with open("notes.txt", "w") as f:
    f.write("Buy coffee beans\n")
    f.write("Call Mom\n")

with open("notes.txt", "a") as f:
    f.write("Finish Python section 7\n")

with open("notes.txt") as f:
    for line in f:
        print("-", line.strip())
