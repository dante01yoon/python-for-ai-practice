import asyncio
import random


async def download(name: str) -> str:
    await asyncio.sleep(random.uniform(0.5, 2))
    return name


async def main() -> None:
    random.seed(3)
    tasks = [download(n) for n in ["weather", "stocks", "news", "maps"]]
    for finished in asyncio.as_completed(tasks):
        print("Done:", await finished)


asyncio.run(main())
