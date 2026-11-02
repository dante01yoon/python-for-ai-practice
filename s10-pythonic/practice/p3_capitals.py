capitals = {"California": "Sacramento", "Texas": "Austin", "New York": "Albany", "Florida": "Tallahassee"}

by_capital = {city: state for state, city in capitals.items()}
print(by_capital["Austin"])

short = {state: city for state, city in capitals.items() if len(city) <= 6}
print(short)
