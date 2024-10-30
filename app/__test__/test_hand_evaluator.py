from typing import List
from app.board import Board
from app.card import Card
from app.dealer import Dealer
from app.player import DummyPlayer
# from app.hand_evaluator import HandEvaluator
# from app.utils.enums import PokerHands


def __generate_test_data(cards: List[Card]=None):
    players = [DummyPlayer(), DummyPlayer(), DummyPlayer()]
    return {
        'board': Board(),
        'cards': cards or [Card('AH'), Card('AD'), Card('AS'), Card('AH')],
        'dealer': Dealer(),
        'players': players
    }

# def test_get_best_made_hand():
#     hand_evaluator = HandEvaluator()
#     best_hand = hand_evaluator.get_best_made_hand()
#     assert best_hand == PokerHands.FLUSH

# def test_evaluation_pre_flop():
#     # init
#     test_data = __generate_test_data()
#     board = test_data['board']
#     players = test_data['players']
#     dealer = test_data['dealer']
#     dealer.deal_starting_cards(players)
#     hand_evaluator = HandEvaluator()
#     # test
#     hand_evaluator.rank_hands(board, dealer, players)

# def test_evaluation_after_flop():
#     # init
#     test_data = __generate_test_data()
#     board = test_data['board']
#     players = test_data['players']
#     dealer = test_data['dealer']
#     dealer.deal_starting_cards(players)
#     dealer.deal_flop(board)
#     hand_evaluator = HandEvaluator()
#     # test
#     hand_evaluator.rank_hands(board, dealer, players)

# def test_evaluation_after_turn():
#     # init
#     test_data = __generate_test_data()
#     board = test_data['board']
#     players = test_data['players']
#     dealer = test_data['dealer']
#     dealer.deal_starting_cards(players)
#     dealer.deal_flop(board)
#     dealer.deal_turn_or_river(board)
#     hand_evaluator = HandEvaluator()
#     # test
#     hand_evaluator.rank_hands(board, dealer, players)

# def test_evaluation_after_river():
#     # init
#     test_data = __generate_test_data()
#     board = test_data['board']
#     players = test_data['players']
#     dealer = test_data['dealer']
#     dealer.deal_starting_cards(players)
#     dealer.deal_flop(board)
#     dealer.deal_turn_or_river(board)
#     dealer.deal_turn_or_river(board)
#     hand_evaluator = HandEvaluator()
#     # test
#     hand_evaluator.rank_hands(board, dealer, players)
