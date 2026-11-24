from pytest import raises
from app.board import Board
from app.card import Card


test_cards = [Card('AC'), Card('10H'), Card('3S')]
turn_card = Card('4H')
river_card = Card('2C')


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

def test_add_flop():
    board = Board()
    board.add_flop_cards(test_cards)
    assert len(board.cards) == 3
    assert board.cards == test_cards
    # adding a second flop to a non-empty board raises
    with raises(ValueError):
        board.add_flop_cards(test_cards.copy())

def test_add_flop_wrong_card_count_raises():
    board = Board()
    with raises(ValueError):
        board.add_flop_cards(test_cards.copy() + [turn_card])
    with raises(ValueError):
        board.add_flop_cards([turn_card, river_card])
    assert len(board.cards) == 0

def test_add_turn():
    board = Board(test_cards.copy())
    board.add_turn_card(turn_card)
    assert len(board.cards) == 4
    assert board.cards[3] == turn_card

def test_add_turn_invalid_state_raises():
    board = Board()
    with raises(ValueError):
        board.add_turn_card(turn_card)
    board.add_flop_cards(test_cards.copy())
    board.add_turn_card(turn_card)
    with raises(ValueError):
        board.add_turn_card(river_card)

def test_add_river():
    board = Board(test_cards.copy() + [turn_card])
    board.add_river_card(river_card)
    assert len(board.cards) == 5
    assert board.cards[4] == river_card

def test_add_river_invalid_state_raises():
    board = Board(test_cards.copy())
    with raises(ValueError):
        board.add_river_card(river_card)
