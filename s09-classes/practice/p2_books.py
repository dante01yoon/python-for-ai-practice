from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int


shelf = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    Book("Charlotte's Web", "E. B. White", 1952),
    Book("Moby-Dick", "Herman Melville", 1851),
]
for book in sorted(shelf, key=lambda b: b.year):
    print(book.year, book.title)
print(shelf[0])
