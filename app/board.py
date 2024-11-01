from typing import List
from app.card import Card


class Board:
    def __init__(self, cards: List[Card]=None):
        self.cards = cards or []

    def __repr__(self):
        return str(self.cards)

    def add_flop_cards(self, flop_cards: List[Card]) -> None:
        try:
            if len(flop_cards) == 3:
                self.reset()
                self.cards.extend(flop_cards)
            raise ValueError
        except ValueError as e:
            print(e)

    def add_turn_card(self, turn_card: Card) -> None:
        try:
            if len(self.cards) == 3:
                self.cards.append(turn_card)
            raise ValueError
        except ValueError as e:
            print(e)

    def add_river_card(self, river_card: Card) -> None:
        try:
            if len(self.cards) == 4:
                self.cards.append(river_card)
            raise ValueError
        except ValueError as e:
            print(e)

    def reset(self):
        self.cards.clear()
