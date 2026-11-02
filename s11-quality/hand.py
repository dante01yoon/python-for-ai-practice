from deck import Card


class Hand:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add(self, card: Card) -> None:
        self.cards.append(card)

    def value(self) -> int:
        total, aces = 0, 0
        for card in self.cards:
            if card.rank == "A":
                total, aces = total + 11, aces + 1
            elif card.rank in ("J", "Q", "K"):
                total += 10
            else:
                total += int(card.rank)
        while total > 21 and aces:
            total, aces = total - 10, aces - 1
        return total

    def __str__(self) -> str:
        cards = " ".join(str(c) for c in self.cards)
        return f"{cards}  ({self.value()})"


if __name__ == "__main__":
    from deck import Card

    hand = Hand()
    hand.add(Card("♠", "A"))
    hand.add(Card("♥", "K"))
    print(hand)
    hand.add(Card("♦", "5"))
    print(hand)
