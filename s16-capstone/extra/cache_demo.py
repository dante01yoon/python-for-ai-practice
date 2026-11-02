import time

from forecast import fetch_hours

for attempt in (1, 2):
    start = time.perf_counter()
    hours = fetch_hours("Denver")
    print(f"Call {attempt}: {len(hours)} hours in {time.perf_counter() - start:.2f}s")
