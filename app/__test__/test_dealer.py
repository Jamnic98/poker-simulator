from dealer import Dealer

def test_deck_initialisation():
    dealer = Dealer()
    assert len(dealer.deck.cards) == 52

def test_deal_flop():
    dealer = Dealer()
    flop = dealer.deal_flop()
    assert isinstance(flop, list)
    assert len(flop) == 3
    assert len(dealer.deck.cards) == 49

def test_deal_turn():
    pass

def test_deal_river():
    pass
