import pytest

from calc import safe_divide


def test_zero_message() -> None:
    with pytest.raises(ValueError, match="divide by zero"):
        safe_divide(10, 0)


def test_floats() -> None:
    assert 0.1 + 0.2 == pytest.approx(0.3)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(10, 2, 5), (9, 3, 3), (1, 4, 0.25)],
    ids=["ten-by-two", "nine-by-three", "quarter"],
)
def test_divide(a: float, b: float, expected: float) -> None:
    assert safe_divide(a, b) == expected
