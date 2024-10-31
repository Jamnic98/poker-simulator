from typing import List
from app.card import Card


class DummyPlayer:
    def __init__(self):
        self.makes_current_player: bool=False
        self.has_button: bool=False
        self.winning_hand = None
        self.pocket: List[Card]=[]

    def add_cards_to_pocket(self, cards: List[Card]):
        self.pocket.extend(cards)

    def make_move(self):
        pass

    def reset(self):
        self.makes_current_player = False
        self.has_button = False
        self.winning_hand = None
        self.pocket.clear()


# class Player(DummyPlayer):
#     def make_move(self):
#         pass


# class AI(DummyPlayer):
#     def __init__(self, *args):
#         super().__init__(*args)

#     def make_move(self):
#         pass
