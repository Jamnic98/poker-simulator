from typing import List

from app.card import Card
from app.utils.logger_setup import logger


class DummyPlayer:
    def __init__(self, cards: List[Card]=None):
        self.pocket = cards or []

    def add_cards(self, cards: List[Card]):
        try:
            if len(cards) + len(self.pocket) > 2:
                raise ValueError(f'Unable to add cards {cards}')
            self.pocket.extend(cards)
        except ValueError as e:
            logger.error(e)

    def reset(self):
        self.pocket.clear()
