import pytest

from deck import Deck


def test_shuffle_keeps_52_unique_cards() -> None:
    deck = Deck()
    deck.shuffle()
    assert len(deck) == 52
    assert len({str(card) for card in deck.cards}) == 52


def test_draw_from_empty_deck() -> None:
    deck = Deck()
    for _ in range(52):
        deck.draw()
    with pytest.raises(IndexError):
        deck.draw()
