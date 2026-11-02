import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE tasks (title TEXT, done INTEGER)")
db.executemany("INSERT INTO tasks VALUES (?, 0)", [("Buy milk",), ("Pay rent",), ("Gym",)])
db.execute("UPDATE tasks SET done = 1 WHERE title = ?", ("Pay rent",))
db.execute("DELETE FROM tasks WHERE title = ?", ("Gym",))
for title, done in db.execute("SELECT title, done FROM tasks"):
    print("✓" if done else "·", title)
