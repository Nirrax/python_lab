import concurrent.futures
import threading
from collections import deque


def add_to_queue(item: int):
    with lock:
        queue.appendleft(item)
        print(f"Added {item} to queue")


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

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_adds = [executor.submit(add_to_queue, i) for i in range(5)]
    future_takes = [executor.submit(take_from_queue) for _ in range(5)]

    for future in future_adds:
        future.result()

    for future in future_takes:
        future.result()
