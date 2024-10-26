from app.board import Board
from app.dealer import Dealer


def test_deck_initialisation():
    dealer = Dealer()
    assert len(dealer.deck.cards) == 52

def test_deal_flop():
    dealer = Dealer()
    board = Board()
    starting_deck = dealer.deck.cards.copy()
    dealer.deal_flop(board)
    assert len(board.cards) == 3
    assert len(dealer.deck.cards) == 49
    # test flop is last 3 cards in deck in reverse order
    assert list(reversed(starting_deck[-3:])) == board.cards

def test_deal_turn_or_river():
    dealer = Dealer()
    board = Board()
    dealer.shuffle_cards()
    last_card_in_deck = dealer.deck.cards.copy()[-1]
    dealer.deal_turn_or_river(board)
    assert len(board.cards) == 1
    assert board.cards[0] == last_card_in_deck
