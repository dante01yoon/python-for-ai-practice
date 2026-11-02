from dataclasses import dataclass


@dataclass(order=True)
class Player:
    score: int
    name: str


players = [Player(18, "Maya"), Player(21, "Jordan"), Player(15, "Sam")]
print(max(players))
print(sorted(players)[0].name)
print(Player(21, "Jordan") == Player(21, "Jordan"))
