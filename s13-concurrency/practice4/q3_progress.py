import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from rich.progress import track


def resize(photo: int) -> int:
    time.sleep(0.3)
    return photo


with ThreadPoolExecutor(max_workers=5) as pool:
    jobs = [pool.submit(resize, p) for p in range(1, 21)]
    done = [job.result() for job in track(as_completed(jobs), total=len(jobs), description="Resizing...")]
print(len(done), "photos resized")
