import concurrent.futures
import threading
import time
from collections import deque


def time_it(func):
    """A decorator that measures the time a function takes to execute."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        with lock:
            timing_results.append((func.__name__, elapsed_time))
            function_call_counts[func.__name__] += 1
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    return wrapper


@time_it
def add_to_queue(item: int):
    with lock:
        queue.appendleft(item)
        print(f"Added {item} to queue")


@time_it
def take_from_queue() -> int | None:
    with lock:
        if not queue:
            print("Queue is empty")
            return None
        item = queue.pop()
        print(f"Removed {item} from queue")
        return item


queue = deque()
lock = threading.Lock()
timing_results = []
function_call_counts = {"add_to_queue": 0, "take_from_queue": 0}

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_adds = [executor.submit(add_to_queue, i) for i in range(100000)]
    future_takes = [executor.submit(take_from_queue) for _ in range(100000)]

    for future in future_adds:
        future.result()

    for future in future_takes:
        future.result()


def print_avg_times():
    with lock:
        for func_name in function_call_counts:
            total_time = sum(
                [time for name, time in timing_results if name == func_name]
            )
            count = function_call_counts[func_name]
            avg_time = total_time / count if count > 0 else 0
            print(f"Average time for {func_name}: {avg_time:.6f} seconds")


print("\nTiming Results:")
for func, time_taken in timing_results:
    print(f"{func} took {time_taken:.6f} seconds")

print_avg_times()
