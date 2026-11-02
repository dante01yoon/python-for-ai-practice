import httpx
from pydantic import BaseModel

URL = "http://localhost:11434/api/chat"


class Item(BaseModel):
    name: str
    quantity: int
    price: float


class Order(BaseModel):
    order_id: int
    items: list[Item]
    city: str
    state: str


email = """Hi! This is about order 4521. I bought 2 coffee mugs at $12.99 each
and 1 French press for $34.50. Please ship everything to Austin, Texas. Thanks, Jordan"""

payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": f"Extract the order from this email:\n{email}"}],
    "format": Order.model_json_schema(),
    "stream": False,
    "options": {"temperature": 0},
}
reply = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]
order = Order.model_validate_json(reply)

print("Order", order.order_id, "to", order.city, order.state)
for item in order.items:
    print(f"  {item.quantity} x {item.name} at ${item.price:.2f}")
total = sum(i.quantity * i.price for i in order.items)
print(f"Total: ${total:.2f}")
