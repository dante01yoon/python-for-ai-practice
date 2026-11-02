import json
from pathlib import Path


def save_todos(path: Path, todos: list[str]) -> None:
    path.write_text(json.dumps(todos))


def load_todos(path: Path) -> list[str]:
    if not path.exists():
        return []
    todos: list[str] = json.loads(path.read_text())
    return todos
