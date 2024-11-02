from typing import List
from random import choice, sample, shuffle
from app.card import Card
from app.utils.constants import FACES, SUITS


class Deck:
    def __init__(self):
        self.cards = self.__generate_cards()

    @staticmethod
    def __generate_cards() -> List[Card]:
        cards = []
        for suit in SUITS:
            for value in FACES:
                cards.append(Card(value + suit))
        return cards

    def get_royal_flush(self) -> List[Card]:
        return self.cards

    def get_straight_flush(self) -> List[Card]:
        return self.cards

    def get_four_of_a_kind(self) -> List[Card]:
        return self.cards

    def get_full_house(self) -> List[Card]:
        return self.cards

    def get_flush(self) -> List[Card]:
        return self.cards

    def get_straight(self) -> List[Card]:
        return self.cards

    def get_three_of_a_kind(self) -> List[Card]:
        return self.cards

    def get_two_pair(self) -> List[Card]:
        return self.cards

    def get_pair(self) -> List[Card]:
        random_face = choice(FACES)
        return self.cards

    def shuffle(self) -> None:
        shuffle(self.cards)

    def reset(self) -> None:
        self.cards = self.__generate_cards()
