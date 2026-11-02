snippets = ["10 / 0", "[1, 2, 3][5]", "'age' + 30", "int('ten')", "{'a': 1}['b']"]
for code in snippets:
    try:
        eval(code)
    except Exception as e:
        print(f"{code:<16} {type(e).__name__}: {e}")
