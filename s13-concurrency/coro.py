import asyncio
import time


async def download(name: str) -> str:
    await asyncio.sleep(1)
    return f"{name} done"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(download("weather"), download("stocks"), download("news"))
    print(results)
    print(f"gather: {time.perf_counter() - start:.1f}s")


asyncio.run(main())
