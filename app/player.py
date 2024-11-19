from typing import List
from app.card import Card, CardHolder


class DummyPlayer:
    def __init__(self, cards: List[Card]=None):
        self.pocket = cards or []

    def add_cards(self, cards: List[Card]):
        try:
            if len(cards) + len(self.pocket) > 2:
                raise  ValueError(f'Unable to add cards {cards}')
            self.pocket.extend(cards)
        except ValueError as e:
            print(e)

    def make_move(self):
        pass

    def reset(self):
        self.pocket.clear()


# class Player(DummyPlayer):
#     def make_move(self):
#         pass


# class AI(DummyPlayer):
#     def __init__(self, *args):
#         super().__init__(*args)

#     def make_move(self):
#         pass
