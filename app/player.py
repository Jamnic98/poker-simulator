from typing import List
from app.card import Card


class DummyPlayer:
    def __init__(self):
        self.pocket: List[Card] = []
        self.is_current_player: bool = False
        self.has_button: bool= False

    def make_move(self):
        pass


# class Player(DummyPlayer):
#     def make_move(self):
#         pass


# class AI(DummyPlayer):
#     def __init__(self, *args):
#         super().__init__(*args)

#     def make_move(self):
#         pass
