def average(scores):
    assert len(scores) > 0, "scores must not be empty"
    return sum(scores) / len(scores)


print(average([90, 80]))
print(average([]))
