from typing import List
# from pandas import DataFrame
from app.board import Board
from app.dealer import Dealer
# from app.graph import Graph
from app.player import DummyPlayer
from app.utils.enums import Mode
# from app.utils.logger import logger
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
        # winning_hand_data = []
        for i in range(n_runs):
            print(f'run {i+1}')
            # shuffle and deal pre-flop cards to players
            self.dealer.shuffle_cards()
            self.dealer.deal_starting_cards(self.players)
            # deal flop, turn and river
            self.dealer.deal_flop(self.board)
            self.dealer.deal_turn_or_river(self.board)
            self.dealer.deal_turn_or_river(self.board)
            # decide winning hand
            # update winning hand data
            # reset
            self.__reset_game_state()
        # output data
        # self.__graph_results(winning_hand_data)
        self.running = False

    def __reset_game_state(self) -> None:
        # remove cards from players
        for player in self.players:
            player.reset()
        # reset dealer
        self.dealer.reset()
        # reset board
        self.board.reset()

    # TODO: add graphing
    # def __graph_results(self) -> None:
    #     logger.info('graphing data...')
        # graph = Graph(title='test')
        # graph.show()
        # graph.save_plot()

    def run(self) -> None:
        self.running = True
        while self.running:
            if self.mode == Mode.PREFLOP_SIM:
                self.__run_preflop_sim(n_runs=DEFAULT_RUN_COUNT)
