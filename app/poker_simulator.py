from pathlib import Path
from datetime import datetime
from time import time
from asyncio import CancelledError
from typing import Tuple
from concurrent.futures import ProcessPoolExecutor, as_completed
from pandas import concat, read_parquet, DataFrame

from app.board import Board
from app.dealer import Dealer
from app.graph import Graph
from app.hand.hand_evaluator import HandEvaluator
from app.hand import Hand
from app.player import DummyPlayer
from app.utils.logger_setup import logger
from app.utils.enums import Mode
from app.settings import config


class PokerSimulator:
    def __init__(self, mode: Mode, run_count: int, top_starting_hands: int, player_count: int = 2):
        self.chunk_data_path = None
        self.run_start_time = None
        self.chunk_size = 10_000
        self.mode: Mode = mode
        self.run_count = run_count
        self.player_count = player_count
        self.top_starting_hands = top_starting_hands
        self.running: bool = False
        self.hand_evaluator = HandEvaluator()

    def __set_players(self, player_count: int) -> tuple[DummyPlayer, ...]:
        """Initiates the players"""
        if self.mode == Mode.PRE_FLOP_SIM:
            return tuple(DummyPlayer() for _ in range(player_count))
        return tuple()

    def __run_pre_flop_sim(self, n_runs) -> None:
        """Runs pre_flop simulation in concurrent batches"""
        try:
            start_time = time()
            with ProcessPoolExecutor(max_workers=1) as executor:
                chunk_results = []
                for chunk_number in range(1, n_runs + 1, self.chunk_size):
                    chunk_start_time = time()

                    # Adjust the chunk size for the final batch if necessary
                    remaining_runs = n_runs + 1 - chunk_number
                    current_chunk_size = min(self.chunk_size, remaining_runs)

                    # Process chunk in parallel
                    for future in as_completed([
                        executor.submit(self._run_single_pre_flop_sim) for _ in range(chunk_number,
                                                                                      chunk_number + current_chunk_size)
                    ]):
                       chunk_results.append(future.result())

                    # Log chunk run duration
                    logger.info(f"Run: {chunk_number} -> {chunk_number + current_chunk_size - 1}, "
                                f"Chunk run duration: {time() - chunk_start_time:.2f}s")

                    # Combine chunk results and save
                    chunk_results_df = concat(chunk_results, axis=0)

                    self.__output_chunk_results_to_file(chunk_results_df, ((chunk_number - 1) // self.chunk_size))

                    # reset for next chunk
                    chunk_results.clear()

                # Log total pre-flop sim run duration
                logger.info(f'Total Run Duration: {(time() - start_time):.2f}s')
                # Graph final results
                self.__graph_results()

        except (CancelledError, TimeoutError) as e:
            logger.error(f"An error occurred: {e}")

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

        results = self.__get_single_pre_flop_sim_result_entry(board, players)
        del board
        del dealer
        del players
        return results

    def __get_single_pre_flop_sim_result_entry(
            self,
            board: Board,
            players: Tuple[DummyPlayer, ...]
    ) -> DataFrame:
        # Create a list of results for each player hand
        hand_results = []
        hands = tuple(Hand([*player.pocket, *board.get_cards()]) for player in players)
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
                # Handle tied hands
                for player_hand in hand:
                    hand_results.append(create_result_entry(player_hand, won=True))
            else:
                # Handle individual hands
                is_winning_hand = hand == ranked_hands[0]
                hand_results.append(create_result_entry(hand, is_winning_hand))

        df = DataFrame(hand_results)

        return df.astype({'main_suit': 'string', 'hand_type': 'string'})

    def __graph_results(self, plot_name: str = 'pre_flop_results') -> None:
        """Graphs the winning hand data"""
        dataframes = []
        # Loop through all Parquet files in the directory
        for file in self.chunk_data_path.iterdir():
            if file.suffix == '.parquet':
                # Load Parquet data into a DataFrame
                df = read_parquet(file)
                dataframes.append(df)

        # Concatenate all DataFrames into a single DataFrame
        data = concat(dataframes, ignore_index=True)

        if data.empty:
            logger.error('Cannot graph empty DataFrame')
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
        # Display the results
        top_starting_hands = self.top_starting_hands
        graph = Graph(
            x_label='Starting Hand',
            y_label='Win %',
            title=f'Pre-flop Simulation Results @ {self.run_count:.0E} runs w/ {self.player_count} players' \
                  f' {f'Top {top_starting_hands} Starting Hands' if top_starting_hands else ''}'
        )

        x = win_stats.index
        y = win_stats['win_percentage']
        if top_starting_hands:
            x = x[:top_starting_hands]
            y = y[:top_starting_hands]

        graph.plot_data(x, y)
        graph.save_plot(plot_name)
        graph.show()

    def __output_chunk_results_to_file(self, chunk_data: DataFrame, chunk_number: int) -> None:
        self.chunk_data_path = Path(
            config.get('RESULTS_DIR', 'results'),
            self.run_start_time.strftime('%Y-%m-%d'),
            f'[{self.run_start_time.strftime('%H:%M:%S')}]-{self.player_count}_players@{self.run_count}_runs'
        )

        if not Path.exists(self.chunk_data_path):
            Path.mkdir(self.chunk_data_path, parents=True, exist_ok=True)

        chunk_file_name = f'pre_flop_sim_chunk_{chunk_number}.parquet'
        chunk_file_path = self.chunk_data_path / chunk_file_name

        # Save as Parquet
        chunk_data.to_parquet(chunk_file_path, engine='pyarrow', index=False)
        logger.info(f'Saved chunk to file: {chunk_file_name}')

    def run(self) -> None:
        """Run the poker sim as a loop until complete"""
        self.run_start_time = datetime.now()
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim(self.run_count)
