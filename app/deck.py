from typing import List
from random import shuffle, choice
from app.card import Card
from app.utils.constants import FACES, SUITS


class Deck:
    def __init__(self):
        self.cards = self.__class__.generate_cards()

    @classmethod
    def generate_cards(cls) -> List[Card]:
        cards = []
        for suit in SUITS:
            for value in FACES:
                cards.append(Card(value + suit))
        return cards

    def shuffle(self) -> None:
        shuffle_count = choice(range(2, 5))
        for _ in range(shuffle_count):
            shuffle(self.cards)

    def reset(self) -> None:
        self.cards = self.__class__.generate_cards()
