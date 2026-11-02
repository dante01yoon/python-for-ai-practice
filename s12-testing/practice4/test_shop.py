from shop import shipping


def test_free_shipping() -> None:
    assert shipping(80) == 0.0


def test_standard_shipping() -> None:
    assert shipping(30) == 4.99


def test_small_order() -> None:
    assert shipping(10) == 7.99
