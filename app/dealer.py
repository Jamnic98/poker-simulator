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
                player.add_cards([self.deck.cards.pop()])

    def deal_flop(self, board: Board) -> None:
        board.add_flop_cards([self.deck.cards.pop() for _ in range(3)])

    def deal_turn_or_river(self, board) -> None:
        card = self.deck.cards.pop()
        if len(board.cards) == 3:
            board.add_turn_card(card)
        else:
            board.add_river_card(card)

    def reset(self):
        self.deck.reset()
