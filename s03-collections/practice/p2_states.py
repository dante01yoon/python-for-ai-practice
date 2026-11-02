states = {"CA": "California", "NY": "New York", "TX": "Texas", "FL": "Florida"}
code = input("State code: ").upper()
print(states.get(code, "Unknown state"))
