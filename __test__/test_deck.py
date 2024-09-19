from deck import Deck

def test_deck():
    test_deck = Deck()
    generated_deck = test_deck.generate_deck()
    assert len(generated_deck) == 52