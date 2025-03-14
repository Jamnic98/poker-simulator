from pytest import raises
from app.card import Card

def test_card():
    card = Card('JH')
    assert str(card) == 'J ♥ '
    assert card.name == 'Jack of Hearts'
    assert card.face == 'J'
    assert card.suit == 'H'
    assert card.face_value == 11

    card = Card('AS')
    assert str(card) == 'A ♠ '
    assert card.name == 'Ace of Spades'
    assert card.face == 'A'
    assert card.suit == 'S'
    assert card.face_value == 14

    card = Card('10C')
    assert str(card) == '10 ♣ '
    assert card.name == 'Ten of Clubs'
    assert card.face == '10'
    assert card.suit == 'C'
    assert card.face_value == 10

    card = Card('3D')
    assert str(card) == '3 ♦ '
    assert card.name == 'Three of Diamonds'
    assert card.face == '3'
    assert card.suit == 'D'
    assert card.face_value == 3

    Card('FU')
    assert raises(ValueError)
