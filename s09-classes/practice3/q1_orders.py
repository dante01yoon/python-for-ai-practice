class Order:
    count = 0

    def __init__(self, item):
        self.item = item
        Order.count += 1
        self.number = Order.count


first = Order("burger")
second = Order("fries")
print(first.number, first.item)
print(second.number, second.item)
print("Orders today:", Order.count)
