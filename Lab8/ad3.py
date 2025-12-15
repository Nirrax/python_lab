import re


class Client:
    def __init__(self, name: str, surname: str, adres: str, postal_code: str):
        self.name = name
        self.surname = surname
        self.adres = adres
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.name} {self.surname} {self.adres} {self.postal_code}"


def add_client():
    name = get_name()
    surname = get_surname()
    adres = get_adres()
    postal_code = get_postal_code()

    client = Client(name, surname, adres, postal_code)
    clients.append(client)
    print(f"Klient {client} został dodany.")


def get_name() -> str:
    match = None
    name = ""
    while not match:
        name = input("Podaj imię klienta: ")
        match = re.match(r"^[A-ZĘÓĄŚŁŻŹĆŃ][a-zęóąśłżźćń]+$", name)
        if not match:
            print("Niepoprawne imię. Spróbuj ponownie.")
    return name


def get_surname() -> str:
    match = None
    surname = ""
    while not match:
        surname = input("Podaj nazwisko klienta: ")
        match = re.match(
            r"^[A-ZĘÓĄŚŁŻŹĆŃ][a-zęóąśłżźćń]+(\-[A-ZĘÓĄŚŁŻŹĆŃ][a-zęóąśłżźćń]+)?$",
            surname,
        )
        if not match:
            print("Niepoprawne nazwisko. Spróbuj ponownie.")
    return surname


def get_adres() -> str:
    match = None
    adres = ""
    while not match:
        adres = input("Podaj adres klienta: ")
        match = re.match(r"^[A-Z][a-zęóąśłżźćń]+(\s+[A-Za-z0-9]+)(/\d+)?$", adres)
        if not match:
            print("Niepoprawny adres. Spróbuj ponownie.")
    return adres


def get_postal_code() -> str:
    match = None
    postal_code = ""
    while not match:
        postal_code = input("Podaj kod pocztowy klienta: ")
        match = re.match(r"^(\d{2})\-(\d{3})$", postal_code)
        if not match:
            print("Niepoprawny kod pocztowy. Spróbuj ponownie.")
    return postal_code


clients = []

while True:
    add_client()
