original = ["milk", "eggs"]
same = original
same.append("bread")
print(original)

backup = original.copy()
backup.append("apples")
print(original)
print(backup)
