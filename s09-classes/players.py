class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def wants_card(self):
        return input(f"{self.name}, hit? (y/n) ") == "y"


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def wants_card(self):
        return self.score <= 16


dealer = Dealer()
dealer.score = 15
print(dealer.name, dealer.wants_card())
dealer.score = 18
print(dealer.name, dealer.wants_card())
print(isinstance(dealer, Player))
