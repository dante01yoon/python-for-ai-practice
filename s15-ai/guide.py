import httpx

URL = "http://localhost:11434/api/chat"
SYSTEM = "You are a friendly park ranger. Answer in two short sentences."


def ask(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": question},
    ]
    payload = {"model": "llama3.2", "messages": messages, "stream": False, "options": {"temperature": 0}}
    return httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]


print(ask("What is Yellowstone famous for?"))
