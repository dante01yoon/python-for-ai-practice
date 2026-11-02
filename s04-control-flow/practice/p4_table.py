for row in range(1, 6):
    line = ""
    for col in range(1, 6):
        line += f"{row * col:4}"
    print(line)
