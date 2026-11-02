import httpx

from forecast import Hour

URL = "http://localhost:11434/api/chat"
SYSTEM = "You are a weather helper. In one short sentence, say what to wear and whether to bring an umbrella."


def summarize(city: str, hours: list[Hour]) -> str:
    lines = "\n".join(f"{h.time}: {h.temp}°F, rain {h.rain}%, {h.sky}" for h in hours)
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"Forecast for {city}:\n{lines}"},
    ]
    payload = {"model": "llama3.2", "messages": messages, "stream": False, "options": {"temperature": 0}}
    return httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]
