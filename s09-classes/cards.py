class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        return self.rank + self.suit


ace = Card("♠", "A")
king = Card("♥", "K")
print(ace.show(), king.show())
print(ace.rank, king.suit)
