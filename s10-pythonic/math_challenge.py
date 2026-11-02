import random
import time


def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        print(f"Time: {time.perf_counter() - start:.1f}s")
        return result

    return wrapper


def problems(count):
    for _ in range(count):
        a, b = random.randint(2, 9), random.randint(2, 9)
        op = random.choice(["+", "*"])
        answer = a + b if op == "+" else a * b
        yield f"{a} {op} {b}", answer


@timer
def play(count):
    results = []
    for question, answer in problems(count):
        reply = input(f"{question} = ")
        results.append(reply.strip() == str(answer))
    return results


random.seed(1)
results = play(3)
print(f"{sum(results)} out of {len(results)} correct")
print(["✓" if r else "✗" for r in results])
