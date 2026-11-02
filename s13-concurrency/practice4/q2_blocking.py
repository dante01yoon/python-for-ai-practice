import asyncio
import time


async def wait_wrong(name: str) -> None:
    time.sleep(1)
    print(name, "done")


async def wait_right(name: str) -> None:
    await asyncio.sleep(1)
    print(name, "done")


async def timed(worker) -> None:
    start = time.perf_counter()
    await asyncio.gather(*(worker(n) for n in ["a", "b", "c"]))
    print(f"{worker.__name__}: {time.perf_counter() - start:.1f} s")


async def main() -> None:
    await timed(wait_wrong)
    await timed(wait_right)


asyncio.run(main())
