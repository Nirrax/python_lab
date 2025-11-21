from abc import ABC
from enum import Enum
from random import randint


class HuntingTime(Enum):
    """
    An enum class representing hunting time.
    ...
    Attributes
    ----------
    DAY : str
    Daytime
    NIGHT : str
    Nighttime
    """

    DAY = "Day"
    NIGHT = "Night"


class Animal(ABC):
    """
    An abstract class representing an animal.
    ...
    Attributes
    ----------
    name : str
    Name of an animal
    occurance : list[str]
    List of occurance of an animal
    is_protected : bool
    Bool value indicating whether the animal is protected
    Methods
    -------
    info()
    Prints the animal info
    """

    def __init__(self, name: str, occurance: list[str], is_protected: bool):
        self.name = name
        self.occurance = occurance
        self.is_protected = is_protected

    def info(self) -> str:
        return f"name: {self.name} | occurance: {self.occurance} | protected: {self.is_protected}"


class Predator(Animal):
    """
    A class representing a predator.
    Interface inherited from parent abstract base class Animal
    ...
    Attributes
    ----------
    hunting_time : HuntingTime
    Time of day when predator hunts
    Methods
    -------
    hunt()
    Indicates whether the predator is hunting
    """

    def __init__(
        self,
        name: str,
        occurance: list[str],
        is_protected: bool,
        hunting_time: HuntingTime,
    ):
        super().__init__(name, occurance, is_protected)
        self.hunting_time = hunting_time

    def hunt(self):
        return f"{self.name} zaczyna polowanie"


class Herbivore(Animal):
    """
    A class representing a Herbivore.
    Interface inherited from parent abstract base class Animal
    ...
    Attributes
    ----------
    name : str
    Name of the herbivore
    occurance : list[str]
    List of places where the herbivore can be found
    is_protected : bool
    Bool value indicating whether the herbivore is protected
    favourite_plants : list[str]
    List of favourite plants of the herbivore
    Methods
    -------
    search()
    Indicates whether the herbivore is searching for food
    """

    def __init__(
        self,
        name: str,
        occurance: list[str],
        is_protected: bool,
        favourite_plants: list[str],
    ):
        super().__init__(name, occurance, is_protected)
        self.favourite_plants = favourite_plants

    def search(self) -> str:
        id = randint(0, len(self.favourite_plants) - 1)
        return f"{self.name} szuka rośliny {self.favourite_plants[id]}"


class Omnivore(Predator, Herbivore):
    """
    A class representing a Omnivore.
    Interface inherited from parent classes Predator and Herbivore
    ...
    Attributes
    ----------
    name : str
    Name of the omnivore
    occurance : list[str]
    List of places where the omnivore can be found
    is_protected : bool
    Bool value indicating whether the omnivore is protected
    favourite_plants : list[str]
    List of favourite plants of the omnivore
    Methods
    -------
    info()
    Prints the omnivore info
    """

    def __init__(
        self,
        name: str,
        occurance: list[str],
        is_protected: bool,
        hunting_time: HuntingTime,
        favourite_plants: list[str],
    ):
        Predator.__init__(self, name, occurance, is_protected, hunting_time)
        Herbivore.__init__(self, name, occurance, is_protected, favourite_plants)

    def info(self) -> str:
        if isinstance(self, Predator):
            return f"{super().info()} | hunting_time: {self.hunting_time}"
        return f"{super().info()} | favourite_plants: {self.favourite_plants}"
