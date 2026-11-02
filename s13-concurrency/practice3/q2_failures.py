import asyncio


async def fetch(city: str) -> str:
    await asyncio.sleep(0.5)
    if city == "Atlantis":
        raise ValueError(f"no weather for {city}")
    return f"{city}: 61°F"


async def main() -> None:
    cities = ["Boston", "Atlantis", "Denver"]
    results = await asyncio.gather(*(fetch(c) for c in cities), return_exceptions=True)
    for city, result in zip(cities, results):
        if isinstance(result, Exception):
            print(city, "failed:", result)
        else:
            print(result)


asyncio.run(main())
