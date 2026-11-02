contacts = [
    {"name": "Ana", "state": "TX", "phone": "512-555-0101"},
    {"name": "Ben", "state": "CA", "phone": "415-555-0102"},
    {"name": "Chloe", "state": "TX", "phone": "713-555-0103"},
]
for person in contacts:
    if person["state"] == "TX":
        print(person["name"], person["phone"])
print(len(contacts), "contacts")
