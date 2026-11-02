import math

import httpx

FACTS = [
    "Yellowstone became the first national park in the United States in 1872.",
    "Old Faithful in Yellowstone erupts about every 90 minutes.",
    "Yosemite National Park is in California and is famous for El Capitan and Half Dome.",
    "The Grand Canyon is about 277 river miles long.",
    "Acadia National Park is in Maine.",
    "Zion National Park is in Utah.",
]


def embed(texts: list[str]) -> list[list[float]]:
    payload = {"model": "nomic-embed-text", "input": texts}
    return httpx.post("http://localhost:11434/api/embed", json=payload, timeout=120).json()["embeddings"]


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


fact_vectors = embed(FACTS)


def search(question: str, k: int = 2) -> list[str]:
    q = embed([question])[0]
    ranked = sorted(zip(FACTS, fact_vectors), key=lambda pair: cosine(q, pair[1]), reverse=True)
    return [fact for fact, _ in ranked[:k]]


def answer(question: str) -> str:
    context = "\n".join(search(question))
    prompt = f"Answer using only these facts. If they don't contain the answer, say you don't know.\n{context}\n\nQuestion: {question}"
    payload = {"model": "llama3.2", "messages": [{"role": "user", "content": prompt}], "stream": False, "options": {"temperature": 0}}
    return httpx.post("http://localhost:11434/api/chat", json=payload, timeout=120).json()["message"]["content"]


question = "How often does Old Faithful erupt?"
print("Found:", search(question))
print("AI:", answer(question))
