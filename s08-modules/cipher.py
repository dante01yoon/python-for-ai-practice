import string

LETTERS = string.ascii_lowercase

def shift_text(text, shift):
    result = ""
    for ch in text.lower():
        if ch in LETTERS:
            i = LETTERS.index(ch)
            result += LETTERS[(i + shift) % 26]
        else:
            result += ch
    return result

def encrypt(text, shift):
    return shift_text(text, shift)

def decrypt(text, shift):
    return shift_text(text, -shift)
