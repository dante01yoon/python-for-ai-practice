import traceback


def parse_age(text):
    return int(text)


for text in ["42", "forty"]:
    try:
        print("Age:", parse_age(text))
    except ValueError:
        print(f"Sorry, {text!r} is not a valid age.")
        with open("errors.log", "a") as log:
            log.write(traceback.format_exc())
