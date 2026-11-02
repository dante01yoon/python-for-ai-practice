import json

import httpx

URL = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Give me three fun facts about the Grand Canyon, one line each."}],
    "options": {"temperature": 0},
}

with httpx.stream("POST", URL, json=payload, timeout=120) as response:
    for line in response.iter_lines():
        chunk = json.loads(line)
        print(chunk["message"]["content"], end="", flush=True)
        if chunk["done"]:
            print()
            print(f"Tokens: {chunk['eval_count']}, speed: {chunk['eval_count'] / chunk['eval_duration'] * 1e9:.0f} tokens per second")
