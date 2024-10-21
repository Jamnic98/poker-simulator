from deck import Deck, FACES, SUITS


def test_generate_cards():
    # test a subset
    test_deck = Deck()
    generated_cards = test_deck.generate_cards()
    assert len(generated_cards) == 52
    test_cards_set = {'JC', 'AH', 'QD', '4S'}
    assert test_cards_set.issubset(generated_cards)
    # test card types
    assert all([type(card) == str for card in generated_cards]) is True

    # test for correct number of suits
    faces = []
    suits = []
    for card in generated_cards:
        faces.append(card[:-1])
        suits.append(card[-1])

    for face in FACES:
        assert [card[:-1] for card in generated_cards].count(face) == 4

    for suit in SUITS:
        assert [card[-1] for card in generated_cards].count(suit) == 13
