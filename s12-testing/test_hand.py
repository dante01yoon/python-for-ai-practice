from deck import Card, Deck
from hand import Hand


def make_hand(*ranks: str) -> Hand:
    hand = Hand()
    for rank in ranks:
        hand.add(Card("♠", rank))
    return hand


def test_blackjack() -> None:
    assert make_hand("A", "K").value() == 21


def test_two_aces() -> None:
    assert make_hand("A", "A", "9").value() == 21


def test_bust() -> None:
    assert make_hand("K", "Q", "5").value() == 25


def test_draw_removes_a_card() -> None:
    deck = Deck()
    deck.draw()
    assert len(deck) == 51
