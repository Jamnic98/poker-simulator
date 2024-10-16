from random import shuffle

faces = ['J', 'Q', 'K', 'A']
suits = ['C', 'D', 'H', 'S']


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        deck = []
        for suit in suits:
            for index, value in enumerate([str(i) for i in range(1, 11)] + faces):
                if index != 0:
                    card = value + suit
                    deck.append(card)

        return deck
        
    def shuffle(self):
        # shuffle cards in place
        shuffle(self.cards)
