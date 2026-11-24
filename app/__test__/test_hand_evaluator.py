from app.card import Card
from app.hand import Hand
from app.hand.hand_evaluator import HandEvaluator
from app.utils.enums import PokerHand


def hand(*tokens) -> Hand:
    return Hand([Card(t) for t in tokens])


def test_category_ordering():
    high_card = hand('2C', '3D', '5H', '9S', 'JC')
    pair_kings = hand('KC', 'KD', '5H', '9S', 'JC')
    pair_aces = hand('AC', 'AD', '5H', '9S', 'JC')
    ranked = HandEvaluator.rank_hands((high_card, pair_kings, pair_aces))
    assert ranked == [pair_aces, pair_kings, high_card]


def test_kicker_decides_two_pair():
    # same two pair (8s and 6s), different kicker: K beats Q, no split pot
    a = hand('8S', '8D', '6H', '6C', 'KC', '2D', '3H')
    b = hand('8C', '8H', '6D', '6S', 'QC', '4D', '5H')
    ranked = HandEvaluator.rank_hands((a, b))
    assert ranked[0] is a
    assert not isinstance(ranked[0], tuple)


def test_wheel_straight_loses_to_six_high():
    wheel = hand('AH', '2D', '3C', '4S', '5H', '9C', 'KD')
    six_high = hand('6H', '2D', '3C', '4S', '5H', '9C', 'KD')
    assert wheel.hand_type[0] == PokerHand.STRAIGHT
    assert six_high.hand_type[0] == PokerHand.STRAIGHT
    assert wheel.get_strength()[1] == (5, 4, 3, 2, 1)
    ranked = HandEvaluator.rank_hands((wheel, six_high))
    assert ranked[0] is six_high


def test_wheel_straight_flush_loses_to_six_high():
    wheel = hand('AH', '2H', '3H', '4H', '5H', '9C', 'KD')
    six_high = hand('6H', '2H', '3H', '4H', '5H', '9C', 'KD')
    assert wheel.hand_type[0] == PokerHand.STRAIGHT_FLUSH
    ranked = HandEvaluator.rank_hands((wheel, six_high))
    assert ranked[0] is six_high


def test_flush_uses_best_five_only():
    f = hand('2H', '4H', '6H', '8H', '10H', 'QH', '2D')
    assert f.hand_type[0] == PokerHand.FLUSH
    assert len(f.hand_type[1]) == 5
    assert [c.face for c in f.hand_type[1]] == ['Q', '10', '8', '6', '4']


def test_flush_tie_when_top_five_equal():
    # same ranks, different suits: suits do not rank, so this is a tie
    a = hand('AH', 'KH', 'QH', 'JH', '9H', '2H', '3D')
    b = hand('AS', 'KS', 'QS', 'JS', '9S', '4S', '5C')
    ranked = HandEvaluator.rank_hands((a, b))
    assert isinstance(ranked[0], tuple)
    assert len(ranked[0]) == 2


def test_split_pot_board_straight():
    # both players play the board straight 5-9
    a = hand('5D', '6C', '7H', '8S', '9D', '2C', '3H')
    b = hand('5D', '6C', '7H', '8S', '9D', 'AC', 'KH')
    ranked = HandEvaluator.rank_hands((a, b))
    assert isinstance(ranked[0], tuple)
    assert len(ranked[0]) == 2


def test_split_pot_board_pair():
    # board has a pair of aces; both players play the board
    a = hand('AH', 'AD', 'KD', 'QS', 'JC', '2C', '3H')
    b = hand('AH', 'AD', 'KD', 'QS', 'JC', '4S', '5D')
    ranked = HandEvaluator.rank_hands((a, b))
    assert isinstance(ranked[0], tuple)
    assert len(ranked[0]) == 2


def test_full_house_from_double_trips():
    # two sets: aces full of kings
    fh = hand('AH', 'AS', 'AD', 'KH', 'KS', 'KD', '2C')
    trips_only = hand('QH', 'QS', 'QD', '9H', '9S', '9D', '2C')  # also a full house, queens full of nines
    ranked = HandEvaluator.rank_hands((trips_only, fh))
    assert ranked[0] is fh


def test_is_tied_compares_kickers():
    a = hand('8S', '8D', '6H', '6C', 'KC', '2D', '3H')
    b = hand('8C', '8H', '6D', '6S', 'QC', '4D', '5H')
    same = hand('8C', '8H', '6D', '6S', 'KC', '4D', '5H')
    assert HandEvaluator._is_tied(a, b) is False
    assert HandEvaluator._is_tied(a, same) is True
