import json
from pathlib import Path

import httpx

URL = "http://localhost:11434/api/chat"
path = Path("history.json")
history = json.loads(path.read_text()) if path.exists() else []

question = input("You: ")
history.append({"role": "user", "content": question})
payload = {"model": "llama3.2", "messages": history, "stream": False, "options": {"temperature": 0}}
reply = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]
history.append({"role": "assistant", "content": reply})
path.write_text(json.dumps(history, indent=2))
print("AI:", reply)
print(f"({len(history)} messages saved)")
