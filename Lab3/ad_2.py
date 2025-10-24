from collections import namedtuple
from dataclasses import dataclass

#Duzo czytelniejszy kod
@dataclass
class DataProduct:
    name: str
    price: int
    weight: float

#Przeciewienstwo czytelnego kodu
TupleProduct = namedtuple("TupleProduct",["name", "price", "weight"])

d1 = DataProduct("DataProduct1", 2100, 2.5)
d2 = DataProduct("DataProduct2", 2500, 1.2)

t1 = TupleProduct("TupleProduct1", 3100, 5.1)
t2 = TupleProduct("TupleProduct2", 1200, 0.7)

#Dziala
print(d1 == d2)
print(t1 == t1)
print(t1 > t2)

#Nie dziala
#print(d1 < d2)  Zadziala jesli do dekoratora dodamy atrybut order=True
#print(d1 == t1) Rozne typy wiec nie da sie ich porownac
