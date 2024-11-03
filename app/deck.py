from typing import List
from random import choice, sample, shuffle
from app.card import Card
from app.utils.constants import FACES, SUITS


class Deck:
    def __init__(self):
        self.cards = self.__class__._generate_cards()

    @classmethod
    def _generate_cards(cls) -> List[Card]:
        cards = []
        for suit in SUITS:
            for value in FACES:
                cards.append(Card(value + suit))
        return cards

    def shuffle(self) -> None:
        shuffle(self.cards)

    def reset(self) -> None:
        self.cards = self.__class__._generate_cards()
