import asyncio
import time


async def bake(item: str, minutes: int) -> str:
    await asyncio.sleep(minutes / 10)
    return f"{item} ready"


async def main() -> None:
    start = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        bread = tg.create_task(bake("bread", 10))
        pie = tg.create_task(bake("pie", 6))
        cookies = tg.create_task(bake("cookies", 3))
    print(bread.result(), pie.result(), cookies.result(), sep=" | ")
    print(f"{time.perf_counter() - start:.1f} s")


asyncio.run(main())
