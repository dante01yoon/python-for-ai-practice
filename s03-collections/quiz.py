# Mini project: US states and capitals quiz
capitals = {"California": "Sacramento", "Texas": "Austin", "New York": "Albany", "Florida": "Tallahassee"}
score = 0
for state, capital in capitals.items():
    answer = input(f"Capital of {state}? ")
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"It's {capital}")
print(f"You got {score} out of {len(capitals)}")
