class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class WantedList:
    def __init__(self):
        self.wanted_people = {}

    def add_person(self, person, reason):
        self.wanted_people[person] = reason

    def update_last_seen(self, person, location):
        if person in self.wanted_people:
            setattr(person, "last_seen", location)
        else:
            raise ValueError("Osoba nie znajduje się na liście poszukiwanych.")


p1 = Person("Jan Kowalski", 34)
p2 = Person("Anna Nowak", 29)

wanted = WantedList()
wanted.add_person(p1, "napad rabunkowy")
wanted.add_person(p2, "oszustwa finansowe")

# Dynamiczne dodanie atrybutu last_seen
wanted.update_last_seen(p1, "Warszawa, Dworzec Centralny")
wanted.update_last_seen(p2, "Kraków, Główny")

print(f"p1:{p1.last_seen}")  # -> Warszawa, Dworzec Centralny
print(f"p2:{p2.last_seen}")  # -> Kraków, Główny
