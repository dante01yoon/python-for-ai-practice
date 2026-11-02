import asyncio
import time

import httpx

URL = "http://localhost:11434/api/chat"
QUESTIONS = ["Capital of Texas?", "Capital of Ohio?", "Capital of Oregon?"]


async def ask(client: httpx.AsyncClient, question: str) -> str:
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": f"{question} Answer with one word."}],
        "stream": False,
        "options": {"temperature": 0},
    }
    for attempt in range(3):
        try:
            response = await client.post(URL, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()["message"]["content"].strip()
        except httpx.HTTPError as error:
            print(f"Attempt {attempt + 1} failed: {error}")
            await asyncio.sleep(1)
    return "no answer"


async def main() -> None:
    start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        answers = await asyncio.gather(*(ask(client, q) for q in QUESTIONS))
    for q, a in zip(QUESTIONS, answers):
        print(f"{q:<20} {a}")
    print(f"Took {time.perf_counter() - start:.1f}s")


asyncio.run(main())
