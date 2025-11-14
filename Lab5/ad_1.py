from enum import Enum
from datetime import date

class Gender(Enum):
    Male = 1
    Female = 2
    NonBinary = 3

class Person:

    counter = 0
    instances = []

    def __init__(self, name="", surname="", gender=Gender.NonBinary, pesel="") -> None:
        Person.counter += 1
        Person.instances.append(self)
        self.name = name.strip()
        self.surname = surname.strip()
        self.gender = gender
        self.pesel = pesel.strip()

    def __str__(self) -> str:
        return f"{self.name} | {self.surname} | {self.gender} | {self.pesel}"

    def age_from_pesel(self) -> int:
        today = date.today()

        year = int(self.pesel[0:2])
        month = int(self.pesel[2:4])
        day = int(self.pesel[4:6])
        if month < 20:
            year = 1900 + year
        else:
            year = 2000 + year
            month = month - 20

        if today.month < month:
            return today.year - year - 1
        if today.month > month:
            return today.year - year
        if today.day < day:
            return today.year - year - 1
        return today.year - year

    def is_surname_hyphenated(self) -> bool:
        return "-" in self.surname or " " in self.surname


p1 = Person("Andrzej", "Kowalski", Gender.Male, "22210942891")
p2 = Person("Janina", "Kowalska-Nowak", Gender.Female, "98101286812")
p3 = Person("Marcin", "Małysz vel Stoch", Gender.NonBinary, "01291715442")
print(f"p1: wiek: {p1.age_from_pesel()} laczone nazwisko: {p1.is_surname_hyphenated()}")
print(f"p2: wiek: {p2.age_from_pesel()} laczone nazwisko: {p2.is_surname_hyphenated()}")
print(f"p3: wiek: {p3.age_from_pesel()} laczone nazwisko: {p3.is_surname_hyphenated()}")

#ZAD2

person_counter = {}

for i in range(0, 5):
    person_counter[Person.counter] = Person()

print(person_counter)