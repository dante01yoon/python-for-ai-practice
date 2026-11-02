import asyncio


async def cook(name: str, queue: asyncio.Queue[str]) -> None:
    while True:
        order = await queue.get()
        await asyncio.sleep(0.5)
        print(f"{name} made {order}")
        queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue()
    for order in ["burger", "fries", "salad", "shake", "taco", "soup"]:
        queue.put_nowait(order)
    cooks = [asyncio.create_task(cook(n, queue)) for n in ["Ana", "Ben"]]
    await queue.join()
    for c in cooks:
        c.cancel()
    print("All orders done")


asyncio.run(main())
