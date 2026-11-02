import time

import httpx

URL = "http://localhost:11434/api/chat"
for limit in [30, 300]:
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": "Tell me about the Golden Gate Bridge."}],
        "stream": False,
        "options": {"temperature": 0, "num_predict": limit},
    }
    start = time.perf_counter()
    answer = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]
    print(f"limit {limit}: {len(answer.split())} words in {time.perf_counter() - start:.1f} s")
