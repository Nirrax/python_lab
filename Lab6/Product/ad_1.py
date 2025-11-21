from abc import ABC, abstractmethod


class Product(ABC):
    """
    An abstract base class representing a product.
    ...
    Attributes
    ----------
    name : str
    Name of the product
    price : int
    Price of the product
    stock : int
    Stock of the product
    Methods
    -------
    display_info()
    Prints the product info
    calculate_discount()
    Calculates the discount for the product"""

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
    """
    A class representing a book.
    Interface inherited from parent abstract base class Product
    ...
    Attributes
    ----------
    author : str
    Author of a book
    genre : str
    Genre of a book
    pages : int
    Number of pages in a book
    Methods
    -------
    display_info()
    Prints the book info
    calculate_discount()
    Calculates the discount for a book
    """

    def __init__(
        self, author: str, genre: str, pages: int, name: str, price: int, stock: int
    ):
        Product.__init__(self, name, price, stock)
        self.author = author
        self.genre = genre
        self.pages = pages

    def calculate_discount(self) -> float:
        return self.price * 0.9

    def display_info(self) -> str:
        return f"author: {self.author} | genre: {self.genre} | pages: {self.pages}"


class ElectronicDevice(Product):
    """
    A class representing an electronic device.
    Interface inherited from parent abstract base class Product
    ...
    Attributes
    ----------
    brand : str
    Brand of an electronic device
    warranty : int
    Warranty period in months
    power : float
    Power consumption in watts
    Methods
    -------
    display_info()
    Prints the car info
    calculate_discount()
    Calculates the discount for an electronic device
    """

    def __init__(
        self, brand: str, warranty: int, power: float, name: str, price: int, stock: int
    ):
        Product.__init__(self, name, price, stock)
        self.brand = brand
        self.warranty = warranty
        self.power = power

    def calculate_discount(self) -> float:
        return self.price * 0.95

    def display_info(self) -> str:
        return f"brand: {self.brand} | warranty: {self.warranty} | power: {self.power}"
