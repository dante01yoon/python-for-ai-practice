import httpx

URL = "http://localhost:11434/api/chat"
SYSTEM = """Sort each customer email into exactly one category: billing, shipping, or technical.
Answer with the category only.

Email: I was charged twice this month.
Category: billing

Email: My package says delivered but it's not here.
Category: shipping"""


def triage(email: str) -> str:
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": f"Email: {email}\nCategory:"}]
    payload = {"model": "llama3.2", "messages": messages, "stream": False, "options": {"temperature": 0}}
    return httpx.post(URL, json=payload, timeout=120).json()["message"]["content"].strip().lower()


emails = [
    "The app crashes every time I open settings.",
    "Can I get a refund for last month?",
    "My order has been stuck in Memphis for a week.",
]
for email in emails:
    print(f"{triage(email):<10} {email}")
