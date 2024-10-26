from app.board import Board
from app.card import Card


def test_board():
    board = Board()
    # test flop
    flop_cards = [Card('A3'), Card('10H'), Card('3S')]
    board.cards.extend(flop_cards)
    assert len(board.cards) == 3
    # test turn
    turn_card = [Card('4H')]
    board.cards.extend(turn_card)
    assert len(board.cards) == 4
    # test river
    river_card = [Card('2C')]
    board.cards.extend(river_card)
    assert len(board.cards) == 5

def test_clear_board():
    board = Board()
    board.cards.extend([Card('A2'), Card('A3'), Card('A4')])
    assert len(board.cards) == 3
    board.cards.clear()
    assert len(board.cards) == 0
