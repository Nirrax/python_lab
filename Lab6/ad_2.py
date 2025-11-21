import Product
from Lab6.Product import ElectronicDevice

def is_order_valid(order: dict[str, int], storage: list[type[Product]]) -> float:
    storage_names = [product.name for product in storage]
    price = 0
    for key, value in order:
        try:
            id = storage_names.index(key)
        except ValueError:
            print(f"There is no such product as {key} in the storage")
            return -1

        if storage[id].stock < value:
            print(f"There is not enough of {key} in the storage")
            return -1

        item = storage[id]
        price += item.calculate_discount * value

    return price


o = {
    "Pralka": 10,
    "Mikrofala": 5,
    "Zemsta": 2,
    "Harry Potter": 1
}

i1 = ElectronicDevice()