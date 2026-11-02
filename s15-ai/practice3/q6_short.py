import httpx

URL = "http://localhost:11434/api/chat"
messages = [{"role": "user", "content": "Describe Yellowstone National Park in under 10 words."}]
for attempt in range(1, 4):
    payload = {"model": "llama3.2", "messages": messages, "stream": False, "options": {"temperature": 0}}
    answer = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"].strip()
    words = len(answer.split())
    print(f"Attempt {attempt}: {words} words")
    if words < 10:
        break
    messages += [{"role": "assistant", "content": answer}, {"role": "user", "content": "Too long. Under 10 words, please."}]
print(answer)
