from typing import List
from app.board import Board
from app.card import Card
from app.dealer import Dealer
from app.player import DummyPlayer
from app.hand_evaluator import HandEvaluator


def __generate_test_data(cards: List[Card]=None):
    players = [DummyPlayer(), DummyPlayer(), DummyPlayer()]
    return {
        'board': Board(),
        'cards': cards or [Card('AH'), Card('AD'), Card('AS'), Card('AH')],
        'dealer': Dealer(),
        'players': players
    }

def test_hand_evaluator_updates_correctly():
    # init
    test_data = __generate_test_data()
    board = test_data['board']
    cards = test_data['cards']
    players = test_data['players']
    hand_evaluator =  HandEvaluator(board, players)
    # test
    board.add_cards(cards)
    assert hand_evaluator.board.cards == cards

def test_hand_evaluator_pre_flop():
    # init
    test_data = __generate_test_data()
    board = test_data['board']
    players = test_data['players']
    dealer = test_data['dealer']
    dealer.deal_starting_cards(players)
    hand_evaluator = HandEvaluator(board, players)
    # test
    hand_evaluator.evaluate_hands()

def test_hand_evaluator_after_flop():
    # init
    test_data = __generate_test_data()
    board = test_data['board']
    players = test_data['players']
    dealer = test_data['dealer']
    dealer.deal_starting_cards(players)
    dealer.deal_flop(board)
    hand_evaluator = HandEvaluator(board, players)
    # test
    hand_evaluator.evaluate_hands()

def test_hand_evaluator_after_turn():
    # init
    test_data = __generate_test_data()
    board = test_data['board']
    players = test_data['players']
    dealer = test_data['dealer']
    dealer.deal_starting_cards(players)
    dealer.deal_flop(board)
    dealer.deal_turn_or_river(board)
    hand_evaluator = HandEvaluator(board, players)
    # test
    hand_evaluator.evaluate_hands()

def test_hand_evaluator_after_river():
    # init
    test_data = __generate_test_data()
    board = test_data['board']
    players = test_data['players']
    dealer = test_data['dealer']
    dealer.deal_starting_cards(players)
    dealer.deal_flop(board)
    dealer.deal_turn_or_river(board)
    dealer.deal_turn_or_river(board)
    hand_evaluator = HandEvaluator(board, players)
    # test
    hand_evaluator.evaluate_hands()
