from typing import List
from app.card import Card


class Board:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return str(self.cards)

    def add_cards(self, cards: List[Card]):
        self.cards.extend(cards)

    def reset(self):
        self.cards.clear()
