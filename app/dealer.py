from random import shuffle
from typing import List
from deck import Deck
from player import Player


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def shuffle_cards(self):
        shuffle(self.deck.cards)

    def pass_button(self):
        pass

    def deal_starting_cards(self, players: List[Player]):
        pass
        # for player in players:
        #     player.hand

    def deal_flop(self):
        return [self.deck.cards.pop() for _ in range(3)]
