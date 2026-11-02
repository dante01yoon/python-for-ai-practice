def check(password):
    rules = {
        "8+ characters": len(password) >= 8,
        "a digit": any(c.isdigit() for c in password),
        "an uppercase letter": any(c.isupper() for c in password),
    }
    missing = [name for name, ok in rules.items() if not ok]
    return all(rules.values()), missing


print(check("sunshine"))
print(check("Sunshine2026"))
