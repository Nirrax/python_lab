import csv
import re


class Item:
    def __init__(self, id: str, price: str, quantity: int):
        self.id = id
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.id}: {self.price} | {self.quantity}"

    def get_price(self) -> float:
        currency = {"PLN": 1.0, "USD": 4.3, "EUR": 4.8}
        currency_code = self.price[-3:]
        if currency_code not in currency:
            raise ValueError(f"Invalid currency code: {currency_code}")
        return (
            float(self.price[:-3].replace(",", ".").replace(" ", ""))
            * currency[currency_code]
        )


def load_csv(path: str) -> list[Item]:
    items = []
    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for index, row in enumerate(reader):
            id, price, quantity = row
            if not re.match(r"^\#\d{8}[SO]", id):
                print(f"Invalid ID at row {index + 2}: {id}")
                continue
            if not re.match(r"^\d{1,3}(?: \d{3})*\.\d{2}[A-Za-z]+$", price):
                print(f"Invalid price at row {index + 2}: {price}")
                continue
            if not re.match(r"^\d+", quantity):
                print(f"Invalid quantity at row {index + 2}: {quantity}")
                continue
            item = Item(id, price, int(quantity))
            items.append(item)
    return items


items = load_csv("items.csv")

for item in items:
    print(item)

items.sort(key=lambda x: x.get_price(), reverse=True)
print("Po sortowaniu: ")

for item in items:
    print(item)
