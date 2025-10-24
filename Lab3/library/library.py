from dataclasses import dataclass

@dataclass(order=True)
class Book:
    author: str
    title: str

class Library:
    books: list[Book] = []

    def __init__(self):
        books = []

    def add(self, book: Book) -> None:
        self.books.append(book)
        print(f"added {book} to collection")

    def delete(self, book: Book) -> None:
        count = self.books.count(book)
        if count == 0:
            print(f"no copy of {book} found")
            return

        for _ in range(0, count):
            pos = self.books.index(book)
            self.books.pop(pos)
        print(f"deleted {count+1} copies of {book}")

    def find(self, book: Book) -> None:
        count = self.books.count(book)
        ids = []

        offset = 0
        for _ in range(0, count):
            pos = self.books.index(book, offset)
            ids.append(pos)
            offset = pos+1
        print(f"found {count} copies of {book} at positions {ids}")

    def sort(self, reverse=False) -> None:
        self.books.sort(reverse=reverse)

    def print(self):
        print(f"{self.books}\n")