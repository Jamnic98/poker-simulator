import os
from time import time
from asyncio import CancelledError
from typing import List
import numpy as np
from pandas import concat, DataFrame
from concurrent.futures import ProcessPoolExecutor, as_completed
from app.board import Board
from app.dealer import Dealer
from app.graph import Graph
from app.hand.evaluator import HandEvaluator
from app.player import DummyPlayer
from app.utils.enums import Mode, PokerHand
from app.utils.constants import RUN_COUNT
from pprint import pprint


class PokerSimulator:
    def __init__(self, mode: Mode, player_count: int):
        self.mode: Mode = mode
        self.player_count = player_count
        self.running: bool = False
        self.hand_evaluator = HandEvaluator()

    def __reset(self) -> None:
        """ resets the poker_sim """
        pass

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        """ initiates the players """
        if self.mode == Mode.PRE_FLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_pre_flop_sim(self, n_runs: int = RUN_COUNT) -> None:
        temp_results = []
        start_time = time()
        with ProcessPoolExecutor() as executor:
            chunk_size = 1000
            for start in range(0, n_runs, chunk_size):
                end = min(start + chunk_size, n_runs+1)
                futures = [executor.submit(self._run_single_pre_flop_sim) for _ in range(start, end)]    
                for run_number, future in enumerate(as_completed(futures), start=1):
                    try:
                        future_result = future.result()
                        future_result['run_number'] = run_number
                        temp_results.append(future_result)
                        if run_number % 1000 == 0:
                            elapsed_time = time() - start_time
                            print(f'Run: {run_number}, Duration: {elapsed_time:.2f}s')
                            start_time = time()
                    except (CancelledError, TimeoutError) as e:
                        print(f"An error occurred during run {run_number}: {e}")

        results = concat(temp_results, ignore_index=True)
        self.__graph_results(results, 'pre_flop_si m_results')
        self.__output_results_to_file(results, 'pre_flop_sim_results')
        self.running = False

    def _run_single_pre_flop_sim(self) -> DataFrame:
        # init
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
        # create a list of results for each player hand
        results_list = []
        ranked_hands = self.hand_evaluator.rank_hands(board, players)
        for hand in ranked_hands:
            results_list.append({
                'pocket': hand.cards[:2],
                'board': hand.cards[2:],
                'sorted_cards': hand.get_sorted_cards(),
                'is_winning_hand': hand == ranked_hands[0],
                'hand_type': hand.type
            })
        return DataFrame(results_list)

    @staticmethod
    def __graph_results(data: DataFrame, plot_name: str = 'example_plot') -> None:
        """ graphs the winning hand data """
        df = data
        # Step 1: Extract starting hand (first two cards) as a tuple
        df['ordered_starting_hand'] = df['sorted_cards'].map(
            lambda x: f"{x[0].face + x[0].suit}_{x[1].face + x[1].suit}"
        )
        # Step 2: Group by starting hand and calculate win percentages
        win_stats = df.groupby('ordered_starting_hand').agg(
            total_hands=('is_winning_hand', 'count'),
            total_wins=('is_winning_hand', lambda x: (x == True).sum())
        )
        # Step 3: Calculate win percentage
        win_stats['win_percentage'] = (win_stats['total_wins'] / win_stats['total_hands']) * 100
        win_stats.sort_values('win_percentage', inplace=True, ascending=False)
        print(win_stats)
        # Step 4: Display the results
        graph = Graph(title='Pre Flop Sim Results')
        graph.plot_data(x=win_stats.index, y=win_stats['win_percentage'])
        graph.show()
        graph.save_plot(plot_name=plot_name)

    @staticmethod
    def __output_results_to_file(data: DataFrame, file_name: str = 'results') -> None:
        data.to_json(os.path.join(os.getcwd(), f'{file_name}.json'))

    def run(self) -> None:
        """ run the poker simulator as a loop until """
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim()
        self.__reset()
