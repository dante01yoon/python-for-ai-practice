import httpx

URL = "https://api.frankfurter.dev/v1/latest"
params = {"base": "USD", "symbols": "EUR,GBP,JPY,CAD,MXN"}

response = httpx.get(URL, params=params, timeout=10)
print(response.status_code)
data = response.json()
print("Rates for", data["date"])
for code, rate in data["rates"].items():
    print(f"$100 = {100 * rate:,.2f} {code}")
