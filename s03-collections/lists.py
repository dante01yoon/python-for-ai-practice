# Lists: an ordered row you can change
groceries = ["milk", "eggs", "bread"]
groceries.append("coffee")
print(groceries)
print(groceries[0], len(groceries))
groceries[1] = "bagels"
groceries.remove("milk")
print(groceries)
print("coffee" in groceries)
