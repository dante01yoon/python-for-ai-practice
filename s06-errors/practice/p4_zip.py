def check_zip(text):
    if len(text) != 5 or not text.isdigit():
        raise ValueError(f"{text!r} is not a 5-digit ZIP code")
    return text


for z in ["94103", "9410", "ABCDE"]:
    try:
        print("OK:", check_zip(z))
    except ValueError as e:
        print("Error:", e)
