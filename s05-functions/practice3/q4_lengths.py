def length_groups(words):
    groups = {}
    for word in words:
        size = len(word)
        if size not in groups:
            groups[size] = []
        groups[size].append(word)
    return groups


print(length_groups(["cat", "dog", "horse", "bird", "fish", "zebra"]))
