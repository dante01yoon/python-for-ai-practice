import time


def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        print(f"{func.__name__} took {time.perf_counter() - start:.2f}s")
        return result

    return wrapper


@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b


print(slow_add(2, 3))
