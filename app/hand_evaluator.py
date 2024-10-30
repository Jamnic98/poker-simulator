from typing import List
from app.board import Board
from app.deck import Deck
from app.hand import Hand
from app.player import DummyPlayer


class HandEvaluator:
    def __init__(self):
        pass

    def rank_hands(self, board: Board, deck: Deck, players: List[DummyPlayer]) -> List[Hand]:
        deck.shuffle()
        hand = Hand(players[0].pocket.copy().extend(board))
        return [hand]

    def get_best_made_hand(self, hand: Hand):
        return hand
