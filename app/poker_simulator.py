from typing import List
from pandas import DataFrame
from app.board import Board
from app.dealer import Dealer
from app.player import DummyPlayer
from app.utils.enums import Mode
from app.utils.constants import DEFAULT_RUN_COUNT


class PokerSimulator:
    def __init__(self, mode: Mode, player_count: int):
        self.mode = mode
        self.running = False
        self.board = Board()
        self.dealer = Dealer()
        self.players = self.__set_players(player_count)

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        if self.mode == Mode.PREFLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_preflop_sim(self, n_runs: int) -> None:
        data = []
        for i in range(n_runs):
            # shuffle and deal pre-flop cards to players
            self.dealer.shuffle_cards()
            self.dealer.deal_starting_cards(self.players)
            # deal flop, turn and river
            self.dealer.deal_flop(self.board)
            self.dealer.deal_turn_or_river(self.board)
            self.dealer.deal_turn_or_river(self.board)
            # decide winning hand
            # reset
            self.dealer.deck.reset()
            self.board.reset()
            print(f'run {i+1}')

        self.__graph_results(data)

    def __graph_results(self, data: DataFrame) -> None:
        print('generating graph...')
        print(data)

    def run(self) -> None:
        self.running = True
        while self.running:
            if self.mode == Mode.PREFLOP_SIM:
                self.__run_preflop_sim(n_runs=DEFAULT_RUN_COUNT)
                self.running = False
