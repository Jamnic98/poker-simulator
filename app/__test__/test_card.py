from app.card import Card

def test_card():
    card = Card('JH')
    assert str(card) == 'JH'
    assert card.name == 'Jack of Hearts'
    assert card.face == 'J'
    assert card.suit == 'H'
    assert card.face_value == 11

    card = Card('AS')
    assert str(card) == 'AS'
    assert card.name == 'Ace of Spades'
    assert card.face == 'A'
    assert card.suit == 'S'
    assert card.face_value == (14, 1)

    card = Card('10C')
    assert str(card) == '10C'
    assert card.name == 'Ten of Clubs'
    assert card.face == '10'
    assert card.suit == 'C'
    assert card.face_value == 10
