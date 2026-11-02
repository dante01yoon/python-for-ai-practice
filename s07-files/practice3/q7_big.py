with open("big.log", "w") as f:
    for n in range(1, 200_001):
        level = "ERROR" if n % 1000 == 0 else "INFO"
        f.write(f"{level} request {n}\n")

errors = 0
with open("big.log") as f:
    for line in f:
        if line.startswith("ERROR"):
            errors += 1
print(errors, "errors in 200,000 lines")
