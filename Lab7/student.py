from collections import namedtuple

Oceny = namedtuple("Oceny", ["matematyka", "fizyka", "informatyka"])


class StudentError(Exception):
    pass


class BledneImieNazwiskoError(StudentError):
    pass


class BlednyIndeksError(StudentError):
    pass


class BlednyEmailError(StudentError):
    pass


class BlednaOcenaError(StudentError):
    pass


class Student:
    def __init__(self, imie, nazwisko, indeks, email, oceny):
        if not (imie.istitle() and nazwisko.istitle()):
            raise BledneImieNazwiskoError(
                "Imię i nazwisko muszą zaczynać się wielką literą."
            )

        if not isinstance(indeks, int) or indeks < 0:
            raise BlednyIndeksError(
                "Numer indeksu musi być nieujemną liczbą całkowitą."
            )

        if "@pollub.edu.pl" not in email:
            raise BlednyEmailError("Email musi zawierać domenę @pollub.edu.pl.")

        for oc in oceny:
            if not (isinstance(oc, (int, float)) and 2.0 <= oc <= 5.0):
                raise BlednaOcenaError("Oceny muszą być liczbami od 2.0 do 5.0.")

        self.imie = imie
        self.nazwisko = nazwisko
        self.indeks = indeks
        self.email = email
        self.oceny = oceny

    def srednia(self):
        return sum(self.oceny) / len(self.oceny)

    def __str__(self):
        return (
            f"{self.imie} {self.nazwisko}, indeks: {self.indeks}, email: {self.email}"
        )
