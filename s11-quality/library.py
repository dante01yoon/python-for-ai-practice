from typing import Literal, TypedDict


class Book(TypedDict):
    title: str
    price: float
    status: Literal["available", "checked out"]


def label(book: Book) -> str:
    return f"{book['title']} · ${book['price']:.2f} · {book['status']}"


book: Book = {"title": "Charlotte's Web", "price": 8.99, "status": "checked out"}
print(label(book))
