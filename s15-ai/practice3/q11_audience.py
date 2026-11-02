import httpx

URL = "http://localhost:11434/api/chat"
question = "Why do leaves change color in the fall?"
for audience in ["a 7 year old", "a college biology student"]:
    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": f"Explain things to {audience} in two sentences."},
            {"role": "user", "content": question},
        ],
        "stream": False,
        "options": {"temperature": 0},
    }
    print(audience.upper())
    print(httpx.post(URL, json=payload, timeout=120).json()["message"]["content"])
    print()
