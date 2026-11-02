import threading
import time

count = 0
lock = threading.Lock()


def add_unsafe() -> None:
    global count
    for _ in range(100):
        now = count
        time.sleep(0)
        count = now + 1


def add_safe() -> None:
    global count
    for _ in range(100):
        with lock:
            now = count
            time.sleep(0)
            count = now + 1


def run(work) -> int:
    global count
    count = 0
    workers = [threading.Thread(target=work) for _ in range(10)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    return count


print("Without a lock:", run(add_unsafe))
print("With a lock:", run(add_safe))
