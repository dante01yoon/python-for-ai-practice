import re

memo = """Team contacts
Maya Lopez 555-0142 maya@example.com
Sam Carter 555-0187 sam.carter@example.org
Next meeting: Nov 5 at 10:30"""

phones = re.findall(r"\d{3}-\d{4}", memo)
print(phones)

emails = re.findall(r"[\w.]+@[\w.]+", memo)
print(emails)

masked = re.sub(r"(\d{3})-\d{2}(\d{2})", r"\1-**\2", memo)
print(masked)
