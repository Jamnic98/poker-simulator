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


# def test_get_royal_flush():
#     deck = Deck()
#     # deck.get_royal_flush()


# def test_get_straight_flush():
#     deck = Deck()
#     # deck.get_straight_flush()


# def test_get_four_of_a_kind():
#     deck = Deck()
#     # deck.get_four_of_a_kind()


# def test_get_full_house():
#     deck = Deck()
#     # deck.get_full_house()


# def test_get_flush():
#     deck = Deck()
#     # deck.get_flush()


# def test_get_straight():
#     deck = Deck()
#     # deck.get_straight()


# def test_get_three_of_a_kind():
#     deck = Deck()
#     # deck.get_three_of_a_kind()


# def test_get_two_pair():
#     deck = Deck()
#     # deck.get_two_pair()


# def test_get_pair():
#     deck = Deck()
#     pair = deck.get_pair()
#     assert len(pair) == 2
