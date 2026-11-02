import re

raw = ["555.014.2233", "(555) 014-2244", "5550142255", "555-014-2266"]
for number in raw:
    digits = re.sub(r"\D", "", number)
    print(f"({digits[:3]}) {digits[3:6]}-{digits[6:]}")
