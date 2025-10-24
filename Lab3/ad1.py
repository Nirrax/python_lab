from library import library, Book

lib = library.Library()

b1 = Book("Mickiewicz", "Pan Tadeusz")
b2 = Book("Slowacki", "Kordian")
b3 = Book("Sienkiewicz", "Krzyzacy")

lib.add(b1)
lib.add(b2)
lib.add(b3)
lib.add(b1)
lib.print()

lib.delete(Book("temp", "book"))
lib.print()

lib.find(b1)

lib.sort()
lib.print()