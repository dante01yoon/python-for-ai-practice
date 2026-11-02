import httpx
from pydantic import BaseModel


class Trail(BaseModel):
    name: str
    miles: float


class Trails(BaseModel):
    trails: list[Trail]


URL = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "List 3 popular day hikes in Colorado with their length in miles."}],
    "format": Trails.model_json_schema(),
    "stream": False,
    "options": {"temperature": 0},
}
result = Trails.model_validate_json(httpx.post(URL, json=payload, timeout=120).json()["message"]["content"])
for trail in result.trails:
    print(f"{trail.miles:5.1f} mi  {trail.name}")
print(f"{sum(t.miles for t in result.trails):.1f} miles in total")
