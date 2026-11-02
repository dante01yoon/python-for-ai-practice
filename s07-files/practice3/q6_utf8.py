from pathlib import Path

cities = "Café in Montréal\nRamen in Tokyo, 東京\nTacos in San José\n"
Path("cities.txt").write_text(cities, encoding="utf-8")
print(Path("cities.txt").read_text(encoding="utf-8"))
print(len("é"), "character,", len("é".encode("utf-8")), "bytes")
