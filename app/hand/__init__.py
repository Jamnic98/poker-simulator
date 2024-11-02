from typing import List
from app.card import Card


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards or []
        self.win_percentage = 0
        self.tie_percentage = 0

    def add_cards_to_hand(self, cards: List[Card]) -> None:
        self.cards.extend(cards)


class Pocket(Hand):
    pass
