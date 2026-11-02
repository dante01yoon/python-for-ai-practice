import asyncio
import time

import httpx

from weather import CITIES, HEADERS, aforecast


async def polite(sem: asyncio.Semaphore, client: httpx.AsyncClient, city: str) -> str:
    async with sem:
        print(f"Asking about {city}")
        return await aforecast(client, city)


async def main() -> None:
    sem = asyncio.Semaphore(3)
    async with httpx.AsyncClient(headers=HEADERS) as client:
        try:
            async with asyncio.timeout(10):
                lines = await asyncio.gather(*(polite(sem, client, city) for city in CITIES))
        except TimeoutError:
            print("The weather service took too long. Try again later.")
            return
    for line in lines:
        print(line)


start = time.perf_counter()
asyncio.run(main())
print(f"Took {time.perf_counter() - start:.1f}s")
