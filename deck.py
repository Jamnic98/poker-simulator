from random import shuffle

FACES = ['J', 'Q', 'K', 'A']
SUITS = ['C', 'D', 'H', 'S']


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
        # shuffle cards in place
        shuffle(self.cards)
