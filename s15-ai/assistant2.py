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
    },
    {
        "type": "function",
        "function": {
            "name": "usd_to",
            "description": "Convert an amount of US dollars into another currency, using today's rate.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {"type": "number"},
                    "currency": {"type": "string", "description": "Three-letter code, like EUR or JPY"},
                },
                "required": ["amount", "currency"],
            },
        },
    },
]


def usd_to(amount: float, currency: str) -> str:
    params = {"base": "USD", "symbols": currency}
    rate = httpx.get("https://api.frankfurter.dev/v1/latest", params=params, timeout=10).json()["rates"][currency]
    return f"${amount} = {amount * rate:,.2f} {currency}"


def chat(messages: list[dict]) -> dict:
    payload = {"model": "llama3.2", "messages": messages, "tools": TOOLS, "stream": False, "options": {"temperature": 0}}
    return httpx.post(URL, json=payload, timeout=120).json()["message"]


messages = [{"role": "user", "content": "How much is 50 dollars in euros?"}]
reply = chat(messages)
messages.append(reply)

with httpx.Client(headers=HEADERS) as client:
    for call in reply.get("tool_calls", []):
        name, args = call["function"]["name"], call["function"]["arguments"]
        if name == "get_forecast":
            result = forecast(client, args["city"])
        else:
            result = usd_to(float(args["amount"]), args["currency"])
        print("Tool result:", result)
        messages.append({"role": "tool", "content": result})

print("AI:", chat(messages)["content"])
