import re


def is_zip(text: str) -> bool:
    return re.fullmatch(r"\d{5}(-\d{4})?", text) is not None


for t in ["94103", "10001-1234", "9410", "941033"]:
    print(t, is_zip(t))

log = """12:01 ERROR payment timeout
12:05 INFO order shipped
12:09 ERROR disk full"""

for m in re.finditer(r"(\d{2}:\d{2}) ERROR (.+)", log):
    print(m.group(1), "|", m.group(2))
