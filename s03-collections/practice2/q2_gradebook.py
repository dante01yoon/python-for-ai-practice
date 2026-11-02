grades = {"Maya": [88, 92], "Sam": [75, 81]}
grades["Maya"].append(95)
grades["Ava"] = [90]
for name, scores in grades.items():
    print(name, scores, round(sum(scores) / len(scores), 1))
