from os import listdir, makedirs, path
from datetime import datetime
from time import time
from asyncio import CancelledError
from typing import List, Tuple
from pandas import concat, read_json, DataFrame
from concurrent.futures import ProcessPoolExecutor, as_completed

from app.board import Board
from app.dealer import Dealer
from app.graph import Graph
from app.hand.hand_evaluator import HandEvaluator
from app.hand import Hand
from app.player import DummyPlayer
from app.utils.enums import Mode
from app.settings import config


class PokerSimulator:
    def __init__(self, mode: Mode, run_count: int, player_count: int = 2):
        self.run_start_time = None
        self.chunks_data_dir = None
        self.mode: Mode = mode
        self.run_count = run_count
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

    def __run_pre_flop_sim(self, n_runs) -> None:
        """Runs pre_flop simulation in concurrent batches"""
        chunk_number = 0
        chunk_size = 100000
        all_results = []
        start_time = time()
        with ProcessPoolExecutor() as executor:
            for start in range(1, n_runs + 1, chunk_size):
                end = min(start + chunk_size, n_runs + 1)
                futures = [executor.submit(self._run_single_pre_flop_sim) for _ in range(start, end)]
                chunk_number += 1
                chunk_results = []
                chunk_start_time = time()
                for chunk_run_number, future in enumerate(as_completed(futures), start=1):
                    try:
                        future_result = future.result()
                        chunk_results.append(future_result)

                        # Periodically save and log
                        if chunk_run_number % chunk_size == 0:
                            elapsed_time = time() - chunk_start_time
                            print(
                                f"Run: {(chunk_number-1)*chunk_size + 1} -> {chunk_number * chunk_size},"
                                f" Duration: {elapsed_time:.2f}s"
                            )
                            chunk_start_time = time()
                    except (CancelledError, TimeoutError) as e:
                        print(f"An error occurred during run {chunk_run_number}: {e}")

                # combine chunk results and save to file
                chunk_results_df = concat(chunk_results, axis=0)
                all_results.append(chunk_results_df)
                # save chunk data to file
                self.__output_chunk_results_to_file(chunk_results_df, chunk_number)
                all_results.clear()

        # Output final results
        print(f'Total Run Duration: {(time() - start_time):.2f}s')
        self.__graph_results()
        self.running = False

    def _run_single_pre_flop_sim(self) -> DataFrame:
        """Runs a single pre_flop simulation"""
        # Init the game state
        board = Board()
        dealer = Dealer()
        players = self.__set_players(self.player_count)
        # Shuffle and deal pre-flop cards to players
        dealer.shuffle_cards()
        dealer.deal_starting_cards(players)
        # Deal flop, turn and river
        dealer.deal_flop(board)
        dealer.deal_turn_or_river(board)
        dealer.deal_turn_or_river(board)
        return self.__get_single_pre_flop_sim_result_entry(board, players)

    def __get_single_pre_flop_sim_result_entry(self, board: Board, players: List[DummyPlayer]):
        # Create a list of results for each player hand
        hand_results = []
        hands = [Hand([*player.pocket, *board.get_cards()]) for player in players]
        ranked_hands = self.hand_evaluator.rank_hands(hands)

        def create_result_entry(players_hand: Hand, won: bool):
            return {
                'pocket': tuple(card.token for card in players_hand.get_sorted_cards()[:2]),
                'board': tuple(card.token for card in players_hand.cards[2:]),
                'hand_type': players_hand.hand_type[0].name,
                'main_cards': tuple(card.token for card in players_hand.hand_type[1]),
                'kickers': tuple(card.token for card in players_hand.hand_type[2]),
                'main_suit': players_hand.hand_type[3],
                'is_winning_hand': won,
            }

        # Iterate through ranked hands
        for i, hand in enumerate(ranked_hands):
            if i == 0 and isinstance(hand, Tuple):
                # Handle the tuple of hands (e.g., tie case)
                for player_hand in hand:
                    hand_results.append(create_result_entry(player_hand, won=True))
            else:
                # Handle individual hands
                is_winning_hand = hand == ranked_hands[0]
                hand_results.append(create_result_entry(hand, is_winning_hand))

        return DataFrame(hand_results).astype({'main_suit': 'string', 'hand_type': 'string'})

    def __graph_results(self, plot_name: str = 'pre_flop_results') -> None:
        """Graphs the winning hand data"""
        dataframes = []
        # Loop through all JSON files in the directory
        for file in listdir(self.chunks_data_dir):
            if file.endswith('.json'):  # Check if the file is a JSON file
                file_path = path.join(self.chunks_data_dir, file)
                # Load JSON data into a DataFrame
                df = read_json(file_path, orient='records')
                # Append the DataFrame to the list
                dataframes.append(df)

        # Concatenate all DataFrames into a single DataFrame
        data = concat(dataframes, ignore_index=True)
        if data.empty:
            print('NO DATA')
            return
        # Ensure that 'pocket' is represented as a string for each hand combination
        data['ordered_pocket'] = data['pocket'].map(lambda card: f"{card[0]}-{card[1]}")
        # Group by the 'ordered_pocket' to calculate win statistics
        win_stats = data.groupby('ordered_pocket').agg(
            total_hands=('is_winning_hand', 'count'),
            total_wins=('is_winning_hand', 'sum')
        )
        # Calculate the win percentage
        win_stats['win_percentage'] = (win_stats['total_wins'] / win_stats['total_hands']) * 100
        # Sort the data by win percentage
        win_stats.sort_values('win_percentage', ascending=False, inplace=True)
        top_cards_count = config.get('TOP_CARDS_COUNT', None)
        # Display the results
        graph = Graph(
            x_label='Starting Hand',
            y_label='Win %',
            title=f'Pre-flop Simulation Results @ {self.run_count:.0E} runs w/ {self.player_count} players' \
                  f' {f'Top {top_cards_count} Cards' if top_cards_count else ''}'
        )

        x = win_stats.index
        y = win_stats['win_percentage']
        if top_cards_count:
            x = x[:top_cards_count]
            y = y[:top_cards_count]

        graph.plot_data(x=x, y=y)
        graph.save_plot(plot_name=plot_name)
        graph.show()

    def __output_chunk_results_to_file(self, chunk_data: DataFrame, chunk_number: int) -> None:
        chunk_file_name = f'pre_flop_sim_chunk_{chunk_number}.json'
        if not path.isdir(self.chunks_data_dir):
            makedirs(self.chunks_data_dir, exist_ok=True)
        chunk_file_path = path.join(str(self.chunks_data_dir), chunk_file_name)
        chunk_data.to_json(chunk_file_path, orient='records', lines=False)
        print(f'Saved chunk to file: {chunk_file_name}')

    def run(self) -> None:
        """Run the poker sim as a loop until complete"""
        self.run_start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.chunks_data_dir = path.join(config.get('RESULTS_DIR', 'results'), self.run_start_time)
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim(self.run_count)
        self.__reset()
