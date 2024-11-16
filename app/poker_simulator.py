from os import getcwd, path
from time import time
from asyncio import CancelledError
from typing import List
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
        """Resets the simulation at the end of a run"""
        pass

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        """Initiates the players"""
        if self.mode == Mode.PRE_FLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_pre_flop_sim(self, n_runs: int = RUN_COUNT) -> None:
        """Runs pre_flop simulation in concurrent batches"""
        chunk_size = 10000
        chunk_number = 0
        all_results = []

        with ProcessPoolExecutor() as executor:
            for start in range(1, n_runs + 1, chunk_size):
                chunk_number += 1
                end = min(start + chunk_size, n_runs + 1)
                futures = [executor.submit(self._run_single_pre_flop_sim) for _ in range(start, end)]
                temp_results = []
                start_time = time()

                for chunk_run_number, future in enumerate(as_completed(futures), start=1):
                    try:
                        future_result = future.result()
                        temp_results.append(future_result)

                        # Periodically save and log
                        if chunk_run_number % chunk_size == 0:
                            elapsed_time = time() - start_time
                            print(f"Run: {(chunk_number-1)*chunk_size + 1} -> {chunk_number * chunk_size}, Duration: {elapsed_time:.2f}s")
                            start_time = time()
                    except (CancelledError, TimeoutError) as e:
                        print(f"An error occurred during run {chunk_run_number}: {e}")

                # Combine chunk results and save to file
                chunk_df = concat(temp_results, ignore_index=True)
                self.__output_chunk_results_to_file(chunk_df, chunk_number)
                all_results.append(chunk_df)  # Append chunk results for final aggregation

        # Combine all chunks into a single DataFrame for graphing
        final_results = concat(all_results, ignore_index=True)
        self.__graph_results(final_results)
        self.running = False

    def _run_single_pre_flop_sim(self) -> DataFrame:
        """Runs a single pre_flop simulation"""
        # init the game state
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
                'pocket': [card.serialize() for card in hand.get_sorted_cards()[:2]],
                'board': [card.serialize() for card in hand.cards[2:]],
                'hand_type': hand.type,
                'is_winning_hand': hand == ranked_hands[0],
            })
        return DataFrame(results_list)

    @staticmethod
    def __graph_results(data: DataFrame, plot_name: str = 'pre_flop_results') -> None:
        """Graphs the winning hand data"""
        # Extract starting hand (first two cards) as a tuple
        data['ordered_starting_hand'] = data['pocket'].map(
            lambda x: f"{x[0]['face']}{x[0]['suit']}_{x[1]['face']}{x[1]['suit']}"
        )

        # Group by starting hand and calculate win percentages
        win_stats = data.groupby('ordered_starting_hand').agg(
            total_hands=('is_winning_hand', 'count'),
            total_wins=('is_winning_hand', lambda x: (x == True).sum())
        )

        # Calculate win percentage
        win_stats['win_percentage'] = (win_stats['total_wins'] / win_stats['total_hands']) * 100
        win_stats.sort_values('win_percentage', inplace=True, ascending=False)
        print(win_stats)

        # Display the results
        graph = Graph(x_label='Starting Hand', y_label='Win %', title='Pre Flop Simulation Results')
        graph.plot_data(x=win_stats.index, y=win_stats['win_percentage'])
        graph.save_plot(plot_name=plot_name)
        graph.show()

    @staticmethod
    def __output_chunk_results_to_file(chunk_data, chunk_number: int) -> None:
        chunk_file_name = f'pre_flop_sim_chunk_{chunk_number}.json'
        chunk_data.to_json(path.join(getcwd(), 'results', chunk_file_name), orient='records', lines=True)

    def run(self) -> None:
        """Run the poker sim as a loop until complete"""
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim()
        self.__reset()
