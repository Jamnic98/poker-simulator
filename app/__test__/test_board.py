from app.board import Board
from app.card import Card


test_cards = [Card('A3'), Card('10H'), Card('3S')]

def test_init_board():
    board = Board()
    assert len(board.cards) == 0
    board = Board(test_cards)
    assert len(board.cards) == len(test_cards)
    assert board.cards == test_cards

def test_clear_board():
    board = Board()
    board.cards.extend(test_cards)
    assert len(board.cards) == len(test_cards)
    board.reset()
    assert len(board.cards) == 0

def test_adding_cards():
    board = Board()
    # test flop
    flop_cards = test_cards
    board.add_flop_cards(flop_cards)
    assert len(board.cards) == 3
    assert board.cards == flop_cards
    # test turn
    turn_card = Card('4H')
    board.add_turn_card(turn_card)
    assert len(board.cards) == 4
    assert board.cards[3] == turn_card
    # test river
    river_card = Card('2C')
    board.add_river_card(river_card)
    assert len(board.cards) == 5
    assert board.cards[4] == river_card
