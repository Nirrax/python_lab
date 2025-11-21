import Animal


def feeding_route(self):
    if self.hunting_time == Animal.HuntingTime.NIGHT:
        return f"{self.name} hunts at night."
    elif self.hunting_time == Animal.HuntingTime.DAY:
        return f"{self.name} eats during the day."


setattr(Animal.Omnivore, "feeding_route", feeding_route)

o1 = Animal.Omnivore("Gorilla", ["spot A"], False, Animal.HuntingTime.NIGHT, ["plants"])
o2 = Animal.Omnivore("Hedgehog", ["spot B"], True, Animal.HuntingTime.DAY, ["plants"])

print(o1.feeding_route())
print(o2.feeding_route())
