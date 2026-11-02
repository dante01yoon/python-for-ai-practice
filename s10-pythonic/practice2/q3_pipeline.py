lines = ["  apple  ", "", "Banana", "  cherry", ""]
cleaned = (line.strip().lower() for line in lines)
nonempty = (line for line in cleaned if line)
print(list(nonempty))
