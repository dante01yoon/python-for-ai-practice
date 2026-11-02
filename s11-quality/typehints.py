def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


print(average([88, 92, 79]))


def find_age(ages: dict[str, int], name: str) -> int | None:
    return ages.get(name)


ages = {"Emma": 29, "Liam": 34}
age = find_age(ages, "Olivia")
if age is None:
    print("No one by that name")
else:
    print(age + 1)
