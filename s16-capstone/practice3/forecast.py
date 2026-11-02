import time
from dataclasses import dataclass
from typing import Any

import httpx

HEADERS = {"User-Agent": "python-for-ai-course (github.com/dante01yoon/python-for-ai-practice)"}
CITIES = {
    "New York": (40.7128, -74.0060),
    "Chicago": (41.8781, -87.6298),
    "Seattle": (47.6062, -122.3321),
    "Miami": (25.7617, -80.1918),
    "Denver": (39.7392, -104.9903),
    "Boston": (42.3601, -71.0589),
}


@dataclass
class Hour:
    time: str
    temp: int
    rain: int
    sky: str


def parse(data: dict[str, Any]) -> list[Hour]:
    hours = []
    for period in data["properties"]["periods"][:12]:
        rain = period["probabilityOfPrecipitation"]["value"] or 0
        hours.append(Hour(period["startTime"][11:16], period["temperature"], rain, period["shortForecast"]))
    return hours


_cache: dict[str, tuple[float, list[Hour]]] = {}


def fetch_hours(city: str) -> list[Hour]:
    saved = _cache.get(city)
    if saved and time.time() - saved[0] < 600:
        return saved[1]
    lat, lon = CITIES[city]
    with httpx.Client(headers=HEADERS, timeout=10) as client:
        point = client.get(f"https://api.weather.gov/points/{lat},{lon}").json()
        hours = parse(client.get(point["properties"]["forecastHourly"]).json())
    _cache[city] = (time.time(), hours)
    return hours


if __name__ == "__main__":
    for hour in fetch_hours("Seattle")[:4]:
        print(hour)
