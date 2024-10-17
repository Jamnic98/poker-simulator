from deck import Deck, FACES, SUITS


def test_generate_cards():
    test_deck = Deck()
    generated_cards = test_deck.generate_cards()
    assert len(generated_cards) == 52
    test_cards_set = {'JC', 'AH', 'QD', '4S'}
    assert test_cards_set.issubset(generated_cards)
    assert 'FU' not in generated_cards

    faces = []
    suits = []
    for card in generated_cards:
        face = card[:-1]
        suit = card[-1]

        faces.append(face)
        suits.append(suit)

    for face in FACES:
        assert [card[:-1] for card in generated_cards].count(face) == 4

    for suit in SUITS:
        assert [card[-1] for card in generated_cards].count(suit) == 13
