from pathlib import Path

import pytest

from todos import load_todos, save_todos


@pytest.fixture
def sample() -> list[str]:
    return ["Buy groceries", "Call the dentist"]


def test_save_and_load(tmp_path: Path, sample: list[str]) -> None:
    file = tmp_path / "todos.json"
    save_todos(file, sample)
    assert load_todos(file) == sample


def test_load_missing(tmp_path: Path) -> None:
    assert load_todos(tmp_path / "nothing.json") == []
