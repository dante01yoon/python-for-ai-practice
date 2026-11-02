import sqlite3

db = sqlite3.connect("library.db")
db.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER)")
db.execute("DELETE FROM books")
db.executemany(
    "INSERT INTO books VALUES (?, ?, ?)",
    [
        ("Charlotte's Web", "E. B. White", 1952),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        ("To Kill a Mockingbird", "Harper Lee", 1960),
    ],
)
db.commit()

for title, year in db.execute("SELECT title, year FROM books WHERE year > 1950 ORDER BY year"):
    print(year, title)
db.close()
