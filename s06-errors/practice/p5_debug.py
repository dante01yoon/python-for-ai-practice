def average(scores):
    total = 0
    breakpoint()
    for i in range(1, len(scores)):
        total += scores[i]
    return total / len(scores)


print(average([90, 80, 70]))
