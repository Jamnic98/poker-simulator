from random import shuffle

faces = ['J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        deck = []
        for suit in suits:
            for i, v in enumerate([str(_) for _ in range(1, 11)] + faces):
                if i != 0:
                    card = v + suit
                    deck.append(card)


        return deck
        
    def shuffle(self):
        shuffle(self.cards)



deck = Deck()
print(deck)