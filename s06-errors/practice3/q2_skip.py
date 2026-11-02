values = ["12", "7.5", "n/a", "3", ""]
total = 0.0
skipped = []
for value in values:
    try:
        total += float(value)
    except ValueError:
        skipped.append(value)
        continue
    print("added", value)
print("Total:", total, "Skipped:", skipped)
