import csv
from tkinter.constants import N

from student import (
    BlednaOcenaError,
    BledneImieNazwiskoError,
    BlednyEmailError,
    BlednyIndeksError,
    Oceny,
    Student,
    StudentError,
)

studenci = []


def wczytaj_csv() -> None:
    sciezka = input("Podaj ścieżkę do pliku CSV: ")
    try:
        with open(sciezka, newline="", encoding="utf-8") as plik:
            reader = csv.DictReader(plik)
            for row in reader:
                try:
                    oceny = Oceny(
                        float(row["matematyka"]),
                        float(row["fizyka"]),
                        float(row["informatyka"]),
                    )
                    student = Student(
                        row["imie"],
                        row["nazwisko"],
                        int(row["indeks"]),
                        row["email"],
                        oceny,
                    )
                    studenci.append(student)
                except StudentError as e:
                    print(f"Błąd w danych w pliku CSV: {e}")

        print("Wczytano dane poprawnie.\n")
    except FileNotFoundError:
        print("Nie znaleziono pliku.\n")


def dodaj_studenta() -> None:
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    indeks = input("Podaj numer indeksu: ")
    email = input("Podaj email: ")

    try:
        indeks = int(indeks)
    except ValueError:
        print("Numer indeksu musi być liczbą całkowitą.\n")
        return

    try:
        oc1 = float(input("Ocena z matematyki (2–5): "))
        oc2 = float(input("Ocena z fizyki (2–5): "))
        oc3 = float(input("Ocena z informatyki (2–5): "))
    except ValueError:
        print("Oceny muszą być liczbami.\n")
        return

    try:
        oceny = Oceny(oc1, oc2, oc3)
        student = Student(imie, nazwisko, indeks, email, oceny)
        studenci.append(student)
        print("Student dodany poprawnie!\n")

    except (
        BledneImieNazwiskoError,
        BlednyIndeksError,
        BlednyEmailError,
        BlednaOcenaError,
    ) as e:
        print(f"Błąd danych: {e}\n")


def wyswietl_oceny() -> None:
    nazwisko = input("Podaj nazwisko studenta: ")
    znaleziono = False

    for s in studenci:
        if s.nazwisko.lower() == nazwisko.lower():
            print(f"Oceny studenta {s.imie} {s.nazwisko}: {s.oceny}\n")
            znaleziono = True

    if not znaleziono:
        print("Nie znaleziono studenta o takim nazwisku.\n")


def wyswietl_posortowanych() -> None:
    if not studenci:
        print("Brak studentów na liście.\n")
        return

    posortowani = sorted(studenci, key=lambda s: s.srednia(), reverse=True)

    print("Lista studentów posortowana wg średniej ocen:\n")
    for s in posortowani:
        print(f"{s} | średnia: {s.srednia():.2f}")
    print()


def menu() -> None:
    while True:
        print("===== MENU =====")
        print("1. Wczytaj studentów z pliku CSV")
        print("2. Dodaj nowego studenta")
        print("3. Wyświetl oceny studenta")
        print("4. Wyświetl listę studentów wg średniej")
        print("5. Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            wczytaj_csv()
        elif wybor == "2":
            dodaj_studenta()
        elif wybor == "3":
            wyswietl_oceny()
        elif wybor == "4":
            wyswietl_posortowanych()
        elif wybor == "5":
            print("Zamykanie programu...")
            break
        else:
            print("Niepoprawny wybór.\n")


if __name__ == "__main__":
    menu()
