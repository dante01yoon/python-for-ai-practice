class Book:
    def __init__(self, title):
        self.title = title
        self.checked_out = False


class Library:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(Book(title))

    def checkout(self, title):
        for book in self.books:
            if book.title == title and not book.checked_out:
                book.checked_out = True
                return True
        return False

    def available(self):
        return [b.title for b in self.books if not b.checked_out]


lib = Library()
for t in ["Charlotte's Web", "Moby-Dick", "The Great Gatsby"]:
    lib.add(t)
print(lib.checkout("Moby-Dick"))
print(lib.checkout("Moby-Dick"))
print(lib.available())
