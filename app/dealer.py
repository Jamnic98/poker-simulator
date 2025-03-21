from typing import List, Tuple
from app.board import Board
from app.deck import Deck
from app.player import DummyPlayer


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def shuffle_cards(self):
        self.deck.shuffle()

    def deal_starting_cards(self, players: Tuple[DummyPlayer, ...]) -> None:
        for _ in range(2):
            for player in players:
                player.pocket.append(self.deck.cards.pop())

    def deal_flop(self, board: Board) -> None:
        flop_cards = [self.deck.cards.pop() for _ in range(3)]
        board.cards.extend(flop_cards)

    def deal_turn_or_river(self, board) -> None:
        board.cards.extend([self.deck.cards.pop()])

    def reset(self):
        self.deck.reset()
