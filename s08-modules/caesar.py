from cipher import decrypt, encrypt

while True:
    mode = input("(e)ncrypt, (d)ecrypt, (q)uit: ")
    if mode == "q":
        break
    text = input("Message: ")
    shift = int(input("Shift: "))
    if mode == "e":
        print(encrypt(text, shift))
    else:
        print(decrypt(text, shift))
