from pprint import pprint

forecast = {"city": "Denver", "days": [{"day": "Mon", "high": 64, "sky": "Sunny"}, {"day": "Tue", "high": 51, "sky": "Snow showers"}], "units": "F"}
print(forecast)
print()
pprint(forecast, width=50)
