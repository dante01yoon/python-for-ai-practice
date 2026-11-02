def check_signup(name, email, age):
    problems = []
    if not name.strip():
        problems.append("name is empty")
    if "@" not in email:
        problems.append("email needs an @")
    if not age.isdigit():
        problems.append("age must be a number")
    if problems:
        raise ValueError("; ".join(problems))


try:
    check_signup("", "maya.example.com", "twenty")
except ValueError as e:
    print("Please fix:", e)
