import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

import httpx

HEADERS = {"User-Agent": "python-for-ai-course (github.com/dante01yoon/python-for-ai-practice)"}
CITIES = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Seattle": (47.6062, -122.3321),
    "Miami": (25.7617, -80.1918),
    "Denver": (39.7392, -104.9903),
    "Boston": (42.3601, -71.0589),
    "Atlanta": (33.7490, -84.3880),
}


def forecast(client: httpx.Client, city: str) -> str:
    lat, lon = CITIES[city]
    point = client.get(f"https://api.weather.gov/points/{lat},{lon}").json()
    now = client.get(point["properties"]["forecast"]).json()["properties"]["periods"][0]
    return f"{city}: {now['temperature']}°F, {now['shortForecast']}"


async def aforecast(client: httpx.AsyncClient, city: str) -> str:
    lat, lon = CITIES[city]
    point = (await client.get(f"https://api.weather.gov/points/{lat},{lon}")).json()
    now = (await client.get(point["properties"]["forecast"])).json()["properties"]["periods"][0]
    return f"{city}: {now['temperature']}°F, {now['shortForecast']}"


def one_by_one() -> list[str]:
    with httpx.Client(headers=HEADERS) as client:
        return [forecast(client, city) for city in CITIES]


def with_threads() -> list[str]:
    with httpx.Client(headers=HEADERS) as client, ThreadPoolExecutor() as pool:
        return list(pool.map(lambda city: forecast(client, city), CITIES))


async def with_asyncio() -> list[str]:
    async with httpx.AsyncClient(headers=HEADERS) as client:
        return await asyncio.gather(*(aforecast(client, city) for city in CITIES))


if __name__ == "__main__":
    start = time.perf_counter()
    for line in one_by_one():
        print(line)
    print(f"One by one: {time.perf_counter() - start:.1f}s")

    start = time.perf_counter()
    with_threads()
    print(f"Threads:    {time.perf_counter() - start:.1f}s")

    start = time.perf_counter()
    asyncio.run(with_asyncio())
    print(f"asyncio:    {time.perf_counter() - start:.1f}s")
