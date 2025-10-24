from dataclasses import dataclass
from collections import deque

@dataclass(order=True)
class Patient:
    surname: str
    name: str
    age: int
    disease: str
    
class Clnic:
    queue: deque
    
    def __init__(self) -> None:
        self.queue = deque([])
        
    def add_patient(self, patient: Patient) -> None:
        self.queue.appendleft(patient)
        print(f"patient {patient} added to queue")
    
    def delete_patient(self) -> None:
        if self.is_queue_empty():
            print("Koniec przyjec")
            return
        
        patient = self.queue.pop()
        print(f"patient {patient} removed from queue")
        
        if self.is_queue_empty():
            print("Koniec przyjec")
            
    def sort_patients_by_surname(self) -> None:
        # uses default dataclass ordering (by fields order)
        self.queue = deque(sorted(self.queue))
        print("queue sorted by surname")
        
    def sort_patients_by_age(self) -> None:
        self.queue = deque(sorted(self.queue, key=lambda p: p.age))
        print("queue sorted by age")
    
    def is_queue_empty(self) -> bool:
        return len(self.queue) == 0
    
    def show_queue(self) -> None:
        if self.is_queue_empty():
            print("queue is empty")
            return
        
        print("current queue:")
        for patient in self.queue:
            print(patient)