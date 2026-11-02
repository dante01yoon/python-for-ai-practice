for age in [8, 15, 34, 70]:
    group = "adult" if age >= 18 else "kid"
    teen = 13 <= age <= 19
    print(age, group, "teen" if teen else "")
