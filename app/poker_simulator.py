from typing import List
# import numpy as np
# from pandas import DataFrame
from concurrent.futures import ThreadPoolExecutor, as_completed
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
        self.player_count = player_count
        self.hand_evaluator = HandEvaluator()
        self.run_count: int = 0
        self.running: bool = False

    def __increase_run_count(self) -> None:
        self.run_count += 1

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        """ initiates the players """
        if self.mode == Mode.PRE_FLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_pre_flop_sim(self, n_runs: int=DEFAULT_RUN_COUNT) -> None:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.__run_single_pre_flop_sim) for _ in range(n_runs)]
            for future in as_completed(futures):
                try:
                    future.result()  # This will raise any exceptions that occurred in the thread
                except Exception as e:
                    print(f"An error occurred: {e}")
        self.running = False

    def __run_single_pre_flop_sim(self) -> None:
        self.__increase_run_count()
        board = Board()
        dealer = Dealer()
        players = self.__set_players(self.player_count)
        # shuffle and deal pre-flop cards to players
        dealer.shuffle_cards()
        dealer.deal_starting_cards(players)
        # deal flop, turn and river
        dealer.deal_flop(board)
        dealer.deal_turn_or_river(board)
        dealer.deal_turn_or_river(board)
        # decide and assign winning hand
        # self.__decide_winning_hand(self.board, self.dealer, self.players)
        # update winning hand data
        print(f'Run {self.run_count}: \n Player Cards: {[player.pocket for player in players]}\n Board: {board}\n')

    # def __decide_winning_hand(self, board: Board, dealer: Dealer, players: List[Player]):
    #     winning_hand = self.hand_evaluator.rank_hands()[0]

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
        # self.__reset_game_state()
        self.run_count = 0

    def run(self) -> None:
        """ run the poker simulator as a loop until """
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim()
        self.__reset()
