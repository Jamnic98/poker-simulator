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
#     royal_flush = deck.get_royal_flush()
#     assert len(royal_flush) == 5
#     assert len(deck.cards) == 47


# def test_get_straight_flush():
#     deck = Deck()
#     straight_flush = deck.get_straight_flush()
#     assert len(straight_flush) == 5
#     assert len(deck.cards) == 47


# def test_get_four_of_a_kind():
#     deck = Deck()
#     quads = deck.get_four_of_a_kind()
#     assert len(quads) == 4
#     assert len(deck.cards) == 48


# def test_get_full_house():
#     deck = Deck()
#     full_house = deck.get_full_house()
#     assert len(full_house) == 5
#     assert len(deck.cards) == 47


# def test_get_flush():
#     deck = Deck()
#     flush = deck.get_flush()
#     assert len(flush) == 5
#     assert len(deck) == 47


# def test_get_straight():
#     deck = Deck()
#     straight = deck.get_straight()
#     assert len(straight) == 5
#     assert len(deck.cards) == 47


# def test_get_three_of_a_kind():
#     deck = Deck()
#     trips = deck.get_three_of_a_kind()
#     assert len(trips) == 3
#     assert len(deck.cards) == 49


# def test_get_two_pair():
#     deck = Deck()
#     two_pair = deck.get_two_pair()
#     assert len(two_pair) == 4
#     assert len(deck.cards) == 48


# def test_get_pair():
#     deck = Deck()
#     pair = deck.get_pair()
#     assert len(pair) == 2
#     assert len(deck.cards) == 50
#     # check the cards have the same face
#     assert pair[0].face == pair[1].face
