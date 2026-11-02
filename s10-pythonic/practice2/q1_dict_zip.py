states = ["Texas", "Ohio", "Oregon"]
capitals = ["Austin", "Columbus", "Salem"]
lookup = dict(zip(states, capitals))
print(lookup)
print({city: len(city) for city in capitals})
