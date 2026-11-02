import httpx

URL = "http://localhost:11434/api/chat"
table = """city,high_f,rain_pct
Seattle,54,80
Phoenix,88,0
Chicago,49,30
Miami,84,60"""
question = "Which city is the warmest, and which is most likely to get rain? Answer in one sentence."
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": f"{table}\n\n{question}"}],
    "stream": False,
    "options": {"temperature": 0},
}
print(httpx.post(URL, json=payload, timeout=120).json()["message"]["content"])
