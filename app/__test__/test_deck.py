from app.deck import Deck, FACES, SUITS


def test_generate_cards():
    # test a subset
    test_deck = Deck()
    generated_cards = test_deck.cards
    assert len(generated_cards) == 52
    # test for correct number of face and suits
    faces = []
    suits = []
    for card in generated_cards:
        faces.append(card.face)
        suits.append(card.suit)
    # test for the correct number of occurrences for each face
    for face in FACES:
        assert [card.face for card in generated_cards].count(face) == 4
    # test for the correct number of occurrences for each suit
    for suit in SUITS:
        assert [card.suit for card in generated_cards].count(suit) == 13
