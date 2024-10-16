from deck import Deck

def test_init_deck():
    test_deck = Deck()
    generated_deck = test_deck.generate_deck()
    assert len(generated_deck) == 52

    test_cards = {'JC', 'AH', 'QD', '4S'}
    assert test_cards.issubset(generated_deck)
    assert 'FU' not in generated_deck
