# from typing import List
# from app.board import Board
# from app.card import Card
# from app.dealer import Dealer
# from app.player import DummyPlayer
from app.hand_evaluator import HandEvaluator
# from app.utils.enums import PokerHand
# from app.data import example_hands


hand_evaluator = HandEvaluator()

def test_get_hand_type():
    pass
    # assert hand_evaluator.get_hand_type(example_hands.royal_flush) == PokerHand.ROYAL_FLUSH
    # assert hand_evaluator.get_hand_type(example_hands.straight_flush) == PokerHand.STRAIGHT_FLUSH
    # assert hand_evaluator.get_hand_type(example_hands.four_of_a_kind) == PokerHand.FOUR_OF_A_KIND
    # assert hand_evaluator.get_hand_type(example_hands.full_house) == PokerHand.FULL_HOUSE
    # assert hand_evaluator.get_hand_type(example_hands.flush) == PokerHand.FLUSH
    # assert hand_evaluator.get_hand_type(example_hands.straight) == PokerHand.STRAIGHT
    # assert hand_evaluator.get_hand_type(example_hands.three_of_a_kind) == PokerHand.THREE_OF_A_KIND
    # assert hand_evaluator.get_hand_type(example_hands.two_pair) == PokerHand.TWO_PAIR
    # assert hand_evaluator.get_hand_type(example_hands.pair) == PokerHand.PAIR
    # assert hand_evaluator.get_hand_type(example_hands.high_card) == PokerHand.HIGH_CARD

# def test_makes_royal_flush():
#     assert hand_evaluator.makes_royal_flush(example_hands.royal_flush) is True

# def test_makes_straight_flush():
#     assert hand_evaluator.makes_straight_flush(example_hands.straight_flush) is True

# def test_makes_four_of_a_kind():
#     assert hand_evaluator.makes_four_of_a_kind(example_hands.four_of_a_kind) is True

# def test_makes_full_house():
#     assert hand_evaluator.makes_full_house(example_hands.full_house) is True

# def test_makes_flush():
#     assert hand_evaluator.makes_flush(example_hands.flush) is True

# def test_makes_straight():
#     assert hand_evaluator.makes_straight(example_hands.straight) is True

# def test_makes_three_of_a_kind():
#     assert hand_evaluator.makes_three_of_a_kind(example_hands.three_of_a_kind) is True

# def test_makes_two_pair():
#     assert hand_evaluator.makes_two_pair(example_hands.two_pair) is True

# def test_makes_pair():
#     assert hand_evaluator.makes_pair(example_hands.pair) is True

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
