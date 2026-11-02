import threading
import time
from concurrent.futures import ThreadPoolExecutor


def download(name: str) -> str:
    time.sleep(1)
    return f"{name} done"


names = ["weather", "stocks", "news"]
start = time.perf_counter()
workers = [threading.Thread(target=download, args=(n,)) for n in names]
for w in workers:
    w.start()
for w in workers:
    w.join()
print(f"Three threads: {time.perf_counter() - start:.1f}s")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    for result in pool.map(download, names):
        print(result)
print(f"Thread pool: {time.perf_counter() - start:.1f}s")
