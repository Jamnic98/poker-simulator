from typing import List
from app.board import Board
from app.player import DummyPlayer


class HandEvaluator:
    def __init__(self, board: Board, players: List[DummyPlayer]):
        self.board = board
        self.players = players

    def evaluate_hands(self):
        # for player in self.players:
            # print(player.pocket)
        pass

    def get_best_made_hand(self):
        pass
