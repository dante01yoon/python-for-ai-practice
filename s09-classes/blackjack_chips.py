import random

from deck import Deck
from hand import Hand

random.seed(6)
chips = 100
while chips > 0:
    bet = input(f"You have ${chips}. Bet (or q to quit): $")
    if bet == "q":
        break
    bet = min(int(bet), chips)
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
        print("Bust!")
        chips -= bet
        continue
    while dealer.value() <= 16:
        dealer.add(deck.draw())
    print("Dealer:", dealer)
    if dealer.value() > 21 or player.value() > dealer.value():
        print(f"You win ${bet}!")
        chips += bet
    elif player.value() < dealer.value():
        print(f"You lose ${bet}.")
        chips -= bet
    else:
        print("Push. Your bet comes back.")
print(f"You leave with ${chips}.")
