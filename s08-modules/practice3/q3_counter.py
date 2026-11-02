from collections import Counter

votes = ["pizza", "tacos", "pizza", "sushi", "tacos", "pizza"]
count = Counter(votes)
print(count)
print("Winner:", count.most_common(1)[0][0])
