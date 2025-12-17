import random
import threading
import time
from collections import deque


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used_space = 0
        self.items = deque()
        self.condition = threading.Condition()

    def add_items(self, items: list) -> None:
        with self.condition:
            while self.used_space + len(items) > self.capacity:
                print(f"Magazyn pełny. Stan magazynu: {self.items}")
                self.condition.wait()
            self.items.extend(items)
            self.used_space += len(items)
            print(f"Dodano przedmioty. Stan magazynu: {self.items}")
            self.condition.notify_all()

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
    while True:
        storage.add_items(random.randint(1, 10) * [1])
        time.sleep(1)


def remove_items_thread(storage):
    while True:
        storage.remove_items(random.randint(1, 10))
        time.sleep(1)


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

for thread in add_threads:
    thread.join()
for thread in remove_threads:
    thread.join()
