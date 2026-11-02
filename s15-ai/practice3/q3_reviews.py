import httpx
from pydantic import BaseModel


class Review(BaseModel):
    sentiment: str
    stars: int


URL = "http://localhost:11434/api/chat"
reviews = ["Best tacos in Austin, friendly staff!", "Cold fries and a 40 minute wait.", "It was fine, nothing special."]
for text in reviews:
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": f"Classify this restaurant review: {text}"}],
        "format": Review.model_json_schema(),
        "stream": False,
        "options": {"temperature": 0},
    }
    answer = httpx.post(URL, json=payload, timeout=120).json()["message"]["content"]
    review = Review.model_validate_json(answer)
    print(f"{review.sentiment:<9} {review.stars}  {text}")
