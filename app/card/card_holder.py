from typing import List, Optional
from .card import Card


class CardHolder:
    def __init__(self, cards: Optional[List[Card]]=None):
        self.cards = cards or []

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def get_cards(self):
        return self.cards

    def add_cards(self, cards: List[Card]):
        self.cards.extend(cards)

    def reset(self):
        self.cards.clear()
