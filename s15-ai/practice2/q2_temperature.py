import httpx

URL = "http://localhost:11434/api/chat"
prompt = "Invent a name for a coffee shop in Seattle. Answer with the name only."
for temperature in [0, 0, 1.2, 1.2]:
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": temperature},
    }
    name = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"].strip()
    print(f"temperature {temperature}: {name}")
