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


def fetch_hours(city: str) -> list[Hour]:
    lat, lon = CITIES[city]
    with httpx.Client(headers=HEADERS, timeout=10) as client:
        point = client.get(f"https://api.weather.gov/points/{lat},{lon}").json()
        return parse(client.get(point["properties"]["forecastHourly"]).json())


if __name__ == "__main__":
    for hour in fetch_hours("Seattle")[:4]:
        print(hour)
