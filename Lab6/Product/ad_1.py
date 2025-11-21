from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __add__(self, other):
        self.stock += other

    def __sub__(self, other):
        self.stock -= other

    @abstractmethod
    def calculate_discount(self) -> float:
        pass

    def display_info(self) -> str:
        return f"name: {self.name} | price: {self.price} | stock: {self.stock}"

class Book(Product):
    def __init__(self, author: str, genre: str, pages: int, name: str, price: int, stock: int):
        Product.__init__(self, name, price, stock)
        self.author = author
        self.genre = genre
        self.pages = pages

    def calculate_discount(self) -> float:
        return self.price * 0.9

    def display_info(self) -> str:
        return f"author: {self.author} | genre: {self.genre} | pages: {self.pages}"

class ElectronicDevice(Product):
    def __init__(self, brand: str, warranty: int, power: float, name: str, price: int, stock: int):
        Product.__init__(self, name, price, stock)
        self.brand = brand
        self.warranty = warranty
        self.power = power

    def calculate_discount(self) -> float:
        return self.price * 0.95

    def display_info(self) -> str:
        return f"brand: {self.brand} | warranty: {self.warranty} | power: {self.power}"

