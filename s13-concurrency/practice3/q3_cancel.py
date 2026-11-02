import asyncio


async def ticker() -> None:
    seconds = 0
    while True:
        await asyncio.sleep(1)
        seconds += 1
        print(f"... still working, {seconds} s")


async def main() -> None:
    task = asyncio.create_task(ticker())
    await asyncio.sleep(3.5)
    print("Report finished!")
    task.cancel()


asyncio.run(main())
