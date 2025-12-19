import random
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


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used_space = 0
        self.items = deque()
        self.condition = threading.Condition()

    @time_it
    def add_items(self, items: list) -> None:
        with self.condition:
            while self.used_space + len(items) > self.capacity:
                print(f"Magazyn pełny. Stan magazynu: {self.items}")
                self.condition.wait()
            self.items.extend(items)
            self.used_space += len(items)
            print(f"Dodano przedmioty. Stan magazynu: {self.items}")
            self.condition.notify_all()

    @time_it
    def remove_items(self, num: int) -> list:
        output = []
        with self.condition:
            while self.used_space - num < 0:
                print(f"Magazyn pusty. Stan magazynu: {self.items}")
                self.condition.wait()
            for _ in range(num):
                output.append(self.items.popleft())
            self.used_space -= num
            print(f"Usunięto przedmioty. Stan magazynu: {self.items}")
            self.condition.notify_all()
        return output


def add_items_thread(storage):
    while not stop_flag.is_set():
        storage.add_items(random.randint(1, 10) * [1])
        time.sleep(1)


def remove_items_thread(storage):
    while not stop_flag.is_set():
        storage.remove_items(random.randint(1, 10))
        time.sleep(1)


timing_results = []
function_call_counts = {"add_items": 0, "remove_items": 0}
lock = threading.Lock()
stop_flag = threading.Event()

magazyn = Storage(20)

add_threads = []
for _ in range(2):
    add_thread = threading.Thread(target=add_items_thread, args=(magazyn,))
    add_threads.append(add_thread)
    add_thread.start()

remove_threads = []
for _ in range(2):
    remove_thread = threading.Thread(target=remove_items_thread, args=(magazyn,))
    remove_threads.append(remove_thread)
    remove_thread.start()


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
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Threads interrupted")
stop_flag.set()

print("\nTiming Results:")
for func, time_taken in timing_results:
    print(f"{func} took {time_taken:.6f} seconds")

print_avg_times()

for thread in add_threads:
    thread.join()

for thread in remove_threads:
    thread.join()
