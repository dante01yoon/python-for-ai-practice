import pytest

from grades import average, letter


def test_average() -> None:
    assert average([88, 92, 79]) == pytest.approx(86.33, abs=0.01)


def test_letter() -> None:
    assert letter(95) == "A"
    assert letter(85) == "B"


def test_letter_boundary() -> None:
    assert letter(90) == "A"


def test_average_empty() -> None:
    with pytest.raises(ZeroDivisionError):
        average([])


@pytest.mark.parametrize(
    ("score", "expected"),
    [(100, "A"), (90, "A"), (89, "B"), (80, "B"), (79, "C"), (60, "D"), (59, "F")],
)
def test_letter_table(score: int, expected: str) -> None:
    assert letter(score) == expected
