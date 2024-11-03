# from typing import List
# from app.board import Board
# from app.card import Card
# from app.dealer import Dealer
# from app.player import DummyPlayer
# from app.hand.evaluator import HandEvaluator
# from app.utils.enums import PokerHand
# from app.data import example_hands


# evaluator = HandEvaluator()


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
