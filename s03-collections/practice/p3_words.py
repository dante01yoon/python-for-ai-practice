text = "that government of the people by the people for the people shall not perish from the earth"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts["people"], counts["the"])
print(max(counts, key=counts.get))
