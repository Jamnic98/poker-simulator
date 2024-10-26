from typing import List
from app.card import Card
from app.utils.constants import FACES, SUITS


class Deck:
    def __init__(self):
        self.cards = self.generate_cards()

    @staticmethod
    def generate_cards() -> List:
        cards = []
        for suit in SUITS:
            for index, value in enumerate([str(i) for i in range(1, 11)] + FACES):
                if index != 0:
                    card = Card(value + suit)
                    cards.append(card)
        return cards

    def reset(self):
        self.cards = self.generate_cards()
