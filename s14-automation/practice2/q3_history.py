import csv

import httpx

url = "https://api.frankfurter.dev/v1/2026-10-26..2026-10-30"
data = httpx.get(url, params={"base": "USD", "symbols": "EUR"}, timeout=10).json()
with open("usd_eur.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "eur"])
    for day, rates in data["rates"].items():
        writer.writerow([day, rates["EUR"]])
        print(day, rates["EUR"])
