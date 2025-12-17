import threading
from random import randint

MAX_CONNECTIONS = 10


class Theater:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.available_seats = capacity
        self.semaphore = threading.Semaphore(MAX_CONNECTIONS)
        self.lock = threading.Lock()

    def reserve_seats(self, num_seats: int) -> None:
        with self.semaphore:
            if num_seats > self.available_seats:
                raise ValueError("Not enough seats available")
            with self.lock:
                self.available_seats -= num_seats
                print(f"Reserved {num_seats} seats")


def thread_function(thread_number: int, num_seats: int) -> None:
    try:
        theater.reserve_seats(num_seats)
    except Exception as e:
        print(f"Thread {thread_number} : {e}")


theater = Theater(100)

threads = []
for i in range(50):
    num_seats = randint(1, 5)
    t = threading.Thread(target=thread_function, args=(i, num_seats))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
