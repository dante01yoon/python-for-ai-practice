from typing import Literal

import httpx
from pydantic import BaseModel


class Ticket(BaseModel):
    team: Literal["billing", "shipping", "tech"]
    urgent: bool


URL = "http://localhost:11434/api/chat"
for message in ["I was charged twice this month!", "My package is a week late.", "The app crashes when I log in."]:
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": f"Route this support message: {message}"}],
        "format": Ticket.model_json_schema(),
        "stream": False,
        "options": {"temperature": 0},
    }
    ticket = Ticket.model_validate_json(httpx.post(URL, json=payload, timeout=120).json()["message"]["content"])
    print(f"{ticket.team:<9} urgent={ticket.urgent}  {message}")
