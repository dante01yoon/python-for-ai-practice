import httpx

URL = "http://localhost:11434/api/chat"


def ask(question: str) -> str:
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": question}],
        "stream": False,
        "options": {"temperature": 0},
    }
    return httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]


print("1:", ask("Hi! My name is Dante."))
print("2:", ask("What's my name?"))
