from typing import List
# import numpy as np
# from pandas import DataFrame
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.board import Board
from app.dealer import Dealer
from app.deck import Deck
# from app.graph import Graph
from app.hand.evaluator import HandEvaluator
from app.player import DummyPlayer
from app.utils.enums import Mode, PokerHand
from app.utils.constants import RUN_COUNT
from pprint import pprint


class PokerSimulator:
    def __init__(self, mode: Mode, player_count: int):
        self.mode: Mode = mode
        self.player_count = player_count
        self.run_count: int = 0
        self.running: bool = False
        self.hand_evaluator = HandEvaluator()

    def __increase_run_count(self) -> None:
        self.run_count += 1

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        """ initiates the players """
        if self.mode == Mode.PRE_FLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_pre_flop_sim(self, n_runs: int=RUN_COUNT) -> None:
        with ThreadPoolExecutor() as executor:
            results_dict = {}
            # map future to its corresponding run number
            future_to_run_num_map = {
                executor.submit(self.__run_single_pre_flop_sim, run_number): run_number for run_number in range(1, n_runs+1)
            }
            for future in as_completed(future_to_run_num_map):
                try:
                    run_num = future_to_run_num_map[future]
                    results_dict.update({run_num: future.result()})
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
            pprint(results_dict)
        self.running = False

    def __run_single_pre_flop_sim(self, run_count: int) -> None:
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
        # winning_hand = self.__decide_winning_players(board, dealer.deck, players)
        return self.hand_evaluator.rank_hands(board, players)

    def __decide_winning_players(self, board: Board, deck: Deck, players: List[DummyPlayer]):
        """decide and assign the winning player's based on hand ranking"""
        # rank the players hands based on primary hand type
        #   then by card ranking for players with the same hand type
        # ranked_hands = self.hand_evaluator.rank_hands(board, deck, players)
        # return ranked_hands[0] if len(ranked_hands) > 0 else None
        # return self.hand_evaluator.rank_hands(board, deck, players)
        pass

    # # TODO: implement graphing
    # def __graph_results(self) -> None:
    #     """ graphs the winning hand data """
    #     graph = Graph(title='Graph')
    #     x = np.arange(1, 10)
    #     y = np.square(x)
    #     graph.plot_data(x=x, y=y)
    #     graph.show()
    #     graph.save_plot(plot_name='example_plot')

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
