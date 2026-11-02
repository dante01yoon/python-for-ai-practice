import asyncio
import time


def old_download(name: str) -> str:
    time.sleep(1)
    return f"{name} done"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(*(asyncio.to_thread(old_download, n) for n in ["a", "b", "c"]))
    print(results, f"{time.perf_counter() - start:.1f} s")


asyncio.run(main())
