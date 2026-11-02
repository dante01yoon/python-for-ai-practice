import secrets
import string

letters = string.ascii_letters + string.digits
password = ""
for _ in range(16):
    password += secrets.choice(letters)
print(password)
print(len(password), "characters")
