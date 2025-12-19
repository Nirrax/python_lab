import asyncio
import threading
import time
from collections import deque


def time_it(func):
    """A decorator that measures the time a function takes to execute."""

    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        async with lock:
            timing_results.append((func.__name__, elapsed_time))
            function_call_counts[func.__name__] += 1
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    return wrapper


@time_it
async def add_to_queue(item: int):
    async with lock:
        queue.appendleft(item)
        print(f"Added {item} to queue")


@time_it
async def take_from_queue() -> int | None:
    async with lock:
        if not queue:
            print("Queue is empty")
            return None
        item = queue.pop()
        print(f"Removed {item} from queue")
        return item


queue = deque()
lock = asyncio.Lock()
reslock = threading.Lock()
timing_results = []
function_call_counts = {"add_to_queue": 0, "take_from_queue": 0}


async def main():
    add_tasks = [asyncio.create_task(add_to_queue(i)) for i in range(100000)]
    take_tasks = [asyncio.create_task(take_from_queue()) for _ in range(100000)]

    await asyncio.gather(*add_tasks)
    await asyncio.gather(*take_tasks)


def print_avg_times():
    with reslock:
        for func_name in function_call_counts:
            total_time = sum(
                [time for name, time in timing_results if name == func_name]
            )
            count = function_call_counts[func_name]
            avg_time = total_time / count if count > 0 else 0
            print(f"Average time for {func_name}: {avg_time:.6f} seconds")


asyncio.run(main())

print("\nTiming Results:")
for func, time_taken in timing_results:
    print(f"{func} took {time_taken:.6f} seconds")

print_avg_times()
