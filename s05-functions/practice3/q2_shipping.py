def shipping(weight, express=False):
    if weight <= 0:
        return 0
    if weight > 50:
        return 99.0
    cost = 5 + weight * 0.5
    if express:
        cost = cost * 2
    return cost


for weight, express in [(0, False), (4, False), (4, True), (60, False)]:
    print(weight, express, shipping(weight, express))
