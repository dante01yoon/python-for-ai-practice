import httpx

URL = "http://localhost:11434/api/embed"
faq = ["How do I reset my password?", "When is my bill due?", "How can I cancel my subscription?", "Where can I change my shipping address?"]


def embed(texts: list[str]) -> list[list[float]]:
    return httpx.post(URL, json={"model": "nomic-embed-text", "input": texts}, timeout=120).json()["embeddings"]


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (sum(x * x for x in a) ** 0.5 * sum(y * y for y in b) ** 0.5)


question = "I moved to a new apartment"
q, *docs = embed([question] + faq)
best = max(range(len(faq)), key=lambda i: cosine(q, docs[i]))
print("Closest FAQ:", faq[best])
