import asyncio
import random
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
        async with async_lock:
            timing_results.append((func.__name__, elapsed_time))
            function_call_counts[func.__name__] += 1
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    return wrapper


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used_space = 0
        self.items = deque()
        self.condition = asyncio.Condition()

    @time_it
    async def add_items(self, items: list) -> None:
        async with self.condition:
            while self.used_space + len(items) > self.capacity:
                print(f"Magazyn pełny. Stan magazynu: {self.items}")
                await self.condition.wait()
            self.items.extend(items)
            self.used_space += len(items)
            print(f"Dodano przedmioty. Stan magazynu: {self.items}")
            self.condition.notify_all()

    @time_it
    async def remove_items(self, num: int) -> list:
        output = []
        async with self.condition:
            while self.used_space - num < 0:
                print(f"Magazyn pusty. Stan magazynu: {self.items}")
                await self.condition.wait()
            for _ in range(num):
                output.append(self.items.popleft())
            self.used_space -= num
            print(f"Usunięto przedmioty. Stan magazynu: {self.items}")
            self.condition.notify_all()
        return output


async def add_items(storage):
    while not stop_flag.is_set():
        await storage.add_items(random.randint(1, 10) * [1])
        await asyncio.sleep(1)


async def remove_items(storage):
    while not stop_flag.is_set():
        await storage.remove_items(random.randint(1, 10))
        await asyncio.sleep(1)


timing_results = []
function_call_counts = {"add_items": 0, "remove_items": 0}
lock = threading.Lock()
async_lock = asyncio.Lock()
stop_flag = asyncio.Event()

magazyn = Storage(20)


async def main():
    add_tasks = [asyncio.create_task(add_items(magazyn)) for _ in range(2)]
    remove_tasks = [asyncio.create_task(remove_items(magazyn)) for _ in range(2)]

    try:
        await asyncio.gather(*add_tasks, *remove_tasks)
    except asyncio.CancelledError:
        pass


def print_avg_times():
    with lock:
        for func_name in function_call_counts:
            total_time = sum(
                [time for name, time in timing_results if name == func_name]
            )
            count = function_call_counts[func_name]
            avg_time = total_time / count if count > 0 else 0
            print(f"Average time for {func_name}: {avg_time:.6f} seconds")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Operation interrupted")
finally:
    stop_flag.set()

print("\nTiming Results:")
for func, time_taken in timing_results:
    print(f"{func} took {time_taken:.6f} seconds")

print_avg_times()
