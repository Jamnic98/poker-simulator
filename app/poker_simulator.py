from typing import List
# import numpy as np
# from pandas import DataFrame
from app.board import Board
from app.dealer import Dealer
# from app.graph import Graph
from app.hand.evaluator import HandEvaluator
from app.player import DummyPlayer
from app.utils.enums import Mode
from app.utils.constants import DEFAULT_RUN_COUNT


class PokerSimulator:
    def __init__(self, mode: Mode, player_count: int):
        self.mode: Mode = mode
        self.players: List[DummyPlayer] = self.__set_players(player_count)
        self.board: Board = Board()
        self.dealer: Dealer = Dealer()
        self.hand_evaluator = HandEvaluator()
        self.run_count: int = 0
        self.running: bool = False

    def __repr__(self):
        return f'Run: {self.run_count}\n' \
            f'Player Cards: {[player.pocket for player in self.players]}\n' \
            f'Board: {self.board}\n'

    def __increase_run_count(self) -> None:
        self.run_count += 1

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        """ initiates the players """
        if self.mode == Mode.PRE_FLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_pre_flop_sim(self, n_runs: int=DEFAULT_RUN_COUNT) -> None:
        # winning_hand_data = []
        while self.run_count < n_runs:
            self.__increase_run_count()
            # shuffle and deal pre-flop cards to players
            self.dealer.shuffle_cards()
            self.dealer.deal_starting_cards(self.players)
            # deal flop, turn and river
            self.dealer.deal_flop(self.board)
            self.dealer.deal_turn_or_river(self.board)
            self.dealer.deal_turn_or_river(self.board)
            # decide and assign winning hand
            # self.__decide_winning_hand(self.board, self.dealer, self.players)
            # update winning hand data
            print(self)
            self.__reset_game_state()

        # self.__graph_results()
        self.running = False

    # def __decide_winning_hand(self, board: Board, dealer: Dealer, players: List[Player]):
    #     winning_hand = self.hand_evaluator.rank_hands()[0]

    def __reset_game_state(self) -> None:
        """ resets the game state at the end of a play """
        for player in self.players:
            player.reset()
        self.board.reset()
        self.dealer.reset()

    # # TODO: implement graphing
    # def __graph_results(self) -> None:
    #     """ graphs the winning hand data """
    #     graph = Graph(title='Graph')
    #     x = np.arange(1, 10)
    #     y = np.square(x)
    #     graph.plot_data(x=x, y=y)
    #     graph.show()
    #     graph.save_plot(plot_name='example_plot')

    # def __decide_winning_hand(self) -> None:
    #     TODO: implement
    #     ranked_hands = self.hand_evaluator.rank_hands(self.board, self.dealer, self.players)

    def __reset(self) -> None:
        """ resets the poker_sim """
        self.__reset_game_state()
        self.run_count = 0

    def run(self) -> None:
        """ run the poker simulator as a loop until """
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim()
        self.__reset()
