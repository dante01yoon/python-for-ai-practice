# Section 8 challenge solution: try every shift on a secret message.
from cipher import decrypt

secret = input("Secret message: ")
for shift in range(1, 26):
    print(f"{shift:>2}  {decrypt(secret, shift)}")
