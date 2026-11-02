import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def heavy(n: int) -> int:
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    jobs = [10_000_000] * 4

    start = time.perf_counter()
    for n in jobs:
        heavy(n)
    print(f"One by one: {time.perf_counter() - start:.1f}s")

    start = time.perf_counter()
    with ThreadPoolExecutor() as pool:
        list(pool.map(heavy, jobs))
    print(f"Threads:    {time.perf_counter() - start:.1f}s")

    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        list(pool.map(heavy, jobs))
    print(f"Processes:  {time.perf_counter() - start:.1f}s")
