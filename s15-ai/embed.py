import math

import httpx

URL = "http://localhost:11434/api/embed"


def embed(texts: list[str]) -> list[list[float]]:
    payload = {"model": "nomic-embed-text", "input": texts}
    return httpx.post(URL, json=payload, timeout=120).json()["embeddings"]


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


sentences = ["How do I reset my password?", "I forgot my login.", "What's the weather in Denver?"]
vectors = embed(sentences)
print("Numbers per sentence:", len(vectors[0]))
print(f"password vs login:   {cosine(vectors[0], vectors[1]):.2f}")
print(f"password vs weather: {cosine(vectors[0], vectors[2]):.2f}")
