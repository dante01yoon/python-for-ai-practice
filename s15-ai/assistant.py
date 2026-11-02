import httpx

from weather import CITIES, HEADERS, forecast

URL = "http://localhost:11434/api/chat"
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_forecast",
            "description": "Get the current weather forecast for a US city.",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string", "enum": list(CITIES)}},
                "required": ["city"],
            },
        },
    }
]


def chat(messages: list[dict]) -> dict:
    payload = {"model": "llama3.2", "messages": messages, "tools": TOOLS, "stream": False, "options": {"temperature": 0}}
    return httpx.post(URL, json=payload, timeout=120).json()["message"]


messages = [{"role": "user", "content": "Should I bring an umbrella in Seattle today?"}]
reply = chat(messages)
messages.append(reply)

with httpx.Client(headers=HEADERS) as client:
    for call in reply.get("tool_calls", []):
        city = call["function"]["arguments"]["city"]
        result = forecast(client, city)
        print("Tool result:", result)
        messages.append({"role": "tool", "content": result})

print("AI:", chat(messages)["content"])
