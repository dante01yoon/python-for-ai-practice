from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import httpx
from openpyxl import Workbook
from rich.console import Console
from rich.table import Table

HEADERS = {"User-Agent": "python-for-ai-course (github.com/dante01yoon/python-for-ai-practice)"}
CITIES = {
    "New York": (40.7128, -74.0060),
    "Chicago": (41.8781, -87.6298),
    "Los Angeles": (34.0522, -118.2437),
}


def temperature(city: str) -> int:
    lat, lon = CITIES[city]
    point = httpx.get(f"https://api.weather.gov/points/{lat},{lon}", headers=HEADERS, timeout=10).json()
    forecast = httpx.get(point["properties"]["forecast"], headers=HEADERS, timeout=10).json()
    return forecast["properties"]["periods"][0]["temperature"]


def usd_rates() -> dict[str, float]:
    params = {"base": "USD", "symbols": "EUR,GBP,JPY"}
    return httpx.get("https://api.frankfurter.dev/v1/latest", params=params, timeout=10).json()["rates"]


with ThreadPoolExecutor() as pool:
    temps = list(pool.map(temperature, CITIES))

rows = [(f"{city} temperature", f"{t}°F") for city, t in zip(CITIES, temps)]
rows += [(f"$1 in {code}", f"{rate:,.2f}") for code, rate in usd_rates().items()]

table = Table(title=f"Today's dashboard · {datetime.now():%I:%M %p}")
table.add_column("Item")
table.add_column("Value", justify="right")
for name, value in rows:
    table.add_row(name, value)
Console().print(table)

wb = Workbook()
ws = wb.active
ws.append(["Item", "Value"])
for row in rows:
    ws.append(list(row))
wb.save("dashboard.xlsx")
print("Saved dashboard.xlsx")
