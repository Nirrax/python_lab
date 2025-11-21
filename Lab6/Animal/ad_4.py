from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, occurance: list[str], is_protected: bool):
        self.name = name
        self.occurance = occurance
        self.is_protected = is_protected


    def info(self) -> str:
        return f"name: {self.name} | occurance: {self.occurance} | protected: {self.is_protected}"

class Predator(Animal):


class Herbivore(Animal):
