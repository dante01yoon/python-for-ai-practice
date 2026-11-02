import httpx

URL = "http://localhost:11434/api/chat"
history = [{"role": "system", "content": "You are a helpful assistant. Keep answers short."}]

while True:
    question = input("You: ")
    if question == "quit":
        break
    history.append({"role": "user", "content": question})
    payload = {"model": "llama3.2", "messages": history, "stream": False, "options": {"temperature": 0}}
    reply = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    print("AI:", reply)
