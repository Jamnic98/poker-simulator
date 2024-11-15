from asyncio import CancelledError
from typing import List
from pandas import concat, DataFrame
from concurrent.futures import ProcessPoolExecutor, as_completed
from app.board import Board
from app.dealer import Dealer
# from app.deck import Deck
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
        self.running: bool = False
        self.hand_evaluator = HandEvaluator()

    def __set_players(self, player_count: int) -> List[DummyPlayer]:
        """ initiates the players """
        if self.mode == Mode.PRE_FLOP_SIM:
            return [DummyPlayer() for _ in range(player_count)]
        return []

    def __run_pre_flop_sim(self, n_runs: int=RUN_COUNT) -> None:
        results = DataFrame()
        with ProcessPoolExecutor() as executor:
            # submit tasks and store futures in a list
            futures = [
                executor.submit(self._run_single_pre_flop_sim) for _ in range(1, n_runs + 1)
            ]
            for run_number, future in enumerate(as_completed(futures), start=1):
                try:
                    future_result = future.result()
                    future_result['run_number'] = run_number
                    results = concat([results, future_result], ignore_index=True)
                except (CancelledError, TimeoutError) as e:
                    print(f"An error occurred during run {run_number}: {e}")
        
        self.__graph_results(results)
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
        results = []
        ranked_hands = self.hand_evaluator.rank_hands(board, players)
        for hand in ranked_hands:
            results.append({
                'cards': hand.get_sorted_cards(),
                'is_winning_hand': hand == ranked_hands[0],
                'hand_type': hand.type
            })
        return DataFrame(results)

    def __graph_results(self, data: DataFrame) -> None:
        """ graphs the winning hand data """
        print(data)
        # df = data
        # # Assuming df is your DataFrame
        # # Step 1: Extract starting hand (first two cards) as a tuple
        # df['starting_hand'] = df['cards'].apply(lambda x: tuple(x[:2]))  # Get the first two cards

        # # Step 2: Group by starting hand and calculate win percentages
        # win_stats = df.groupby('starting_hand').agg(
        #     total_hands=('is_winning_hand', 'count'),
        #     total_wins=('is_winning_hand', lambda x: (x == True).sum())
        # )

        # # Step 3: Calculate win percentage
        # win_stats['win_percentage'] = (win_stats['total_wins'] / win_stats['total_hands']) * 100

        # # Step 4: Display the results
        # print(win_stats[['total_hands', 'total_wins', 'win_percentage']])
        # graph = Graph(title='Graph')
        # x = np.arange(1, 10)
        # y = np.square(x)
        # graph.plot_data(x=x, y=y)
        # graph.show()
        # graph.save_plot(plot_name='example_plot')

    def __reset(self) -> None:
        """ resets the poker_sim """
        pass

    def run(self) -> None:
        """ run the poker simulator as a loop until """
        self.running = True
        while self.running:
            if self.mode == Mode.PRE_FLOP_SIM:
                self.__run_pre_flop_sim()
        self.__reset()
