import httpx

URL = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Explain what Python is in one sentence."}],
    "stream": False,
}
response = httpx.post(URL, json=payload, timeout=120)
data = response.json()
print(data["message"]["content"])
