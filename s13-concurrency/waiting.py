import time


def download(name: str) -> str:
    time.sleep(1)
    return f"{name} done"


start = time.perf_counter()
for name in ["weather", "stocks", "news"]:
    print(download(name))
print(f"Took {time.perf_counter() - start:.1f}s")
