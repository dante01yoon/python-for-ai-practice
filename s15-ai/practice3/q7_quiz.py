import httpx
from pydantic import BaseModel


class Question(BaseModel):
    question: str
    answer: str


URL = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Write one easy quiz question about US geography, with a one word answer."}],
    "format": Question.model_json_schema(),
    "stream": False,
    "options": {"temperature": 0},
}
quiz = Question.model_validate_json(httpx.post(URL, json=payload, timeout=120).json()["message"]["content"])
guess = input(quiz.question + " ")
print("Correct!" if guess.strip().lower() == quiz.answer.strip().lower() else f"The answer was {quiz.answer}.")
