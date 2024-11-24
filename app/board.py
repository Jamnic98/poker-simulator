from typing import List
from app.card import Card, CardHolder
from app.utils.logger_setup import logger


class Board(CardHolder):
    def __init__(self, cards: List[Card]=None):
        super().__init__(cards)

    def add_flop_cards(self, flop_cards: List[Card]) -> None:
        try:
            if len(flop_cards) == 3:
                self.reset()
                self.add_cards(flop_cards)
            raise ValueError
        except ValueError as e:
            logger.error(e)

    def add_turn_card(self, turn_card: Card) -> None:
        try:
            if len(self.cards) == 3:
                self.add_cards([turn_card])
            raise ValueError
        except ValueError as e:
            logger.error(e)

    def add_river_card(self, river_card: Card) -> None:
        try:
            if len(self.cards) == 4:
                self.add_cards([river_card])
            raise ValueError
        except ValueError as e:
            logger.error(e)

    def reset(self):
        self.cards.clear()
