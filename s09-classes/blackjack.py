import random

from deck import Deck
from hand import Hand

random.seed(6)
deck = Deck()
deck.shuffle()
player, dealer = Hand(), Hand()
for _ in range(2):
    player.add(deck.draw())
    dealer.add(deck.draw())
print("Dealer shows:", dealer.cards[0])

while player.value() < 21:
    print("You:", player)
    if input("Hit or stand? (h/s) ") != "h":
        break
    player.add(deck.draw())
print("You:", player)

if player.value() > 21:
    print("Bust! Dealer wins.")
else:
    while dealer.value() <= 16:
        dealer.add(deck.draw())
    print("Dealer:", dealer)
    if dealer.value() > 21 or player.value() > dealer.value():
        print("You win!")
    elif player.value() == dealer.value():
        print("Push. It's a tie.")
    else:
        print("Dealer wins.")
