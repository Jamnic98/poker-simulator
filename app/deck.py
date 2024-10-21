from random import shuffle
from card import Card
from utils.constants import FACES, SUITS

class Deck:
    def __init__(self):
        self.cards = self.generate_cards()

    @staticmethod
    def generate_cards():
        cards = []
        for suit in SUITS:
            for index, value in enumerate([str(i) for i in range(1, 11)] + FACES):
                if index != 0:
                    card = value + suit
                    cards.append(card)
        return cards
        
    def shuffle(self):
        """ shuffles cards in place """
        shuffle(self.cards)
