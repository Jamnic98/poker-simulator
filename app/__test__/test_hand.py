from app.hand import Hand
from app.utils.data import example_hands
from app.utils.enums import PokerHand


# def test_get_hand_type():
#     hand = Hand(example_hands.royal_flush)
#     assert hand.get_hand_type() == PokerHand.ROYAL_FLUSH
#     hand = Hand(example_hands.straight_flush)
#     assert hand.get_hand_type() == PokerHand.STRAIGHT_FLUSH
#     hand = Hand(example_hands.four_of_a_kind)
#     assert hand.get_hand_type() == PokerHand.FOUR_OF_A_KIND
#     hand = Hand(example_hands.full_house)
#     assert hand.get_hand_type() == PokerHand.FULL_HOUSE
#     hand = Hand(example_hands.flush)
#     assert hand.get_hand_type() == PokerHand.FLUSH
#     hand = Hand(example_hands.straight)
#     assert hand.get_hand_type() == PokerHand.STRAIGHT
#     hand = Hand(example_hands.three_of_a_kind)
#     assert hand.get_hand_type() == PokerHand.THREE_OF_A_KIND
#     hand = Hand(example_hands.two_pair)
#     assert hand.get_hand_type() == PokerHand.TWO_PAIR
#     hand = Hand(example_hands.pair)
#     assert hand.get_hand_type() == PokerHand.PAIR
#     hand = Hand(example_hands.high_card)
#     assert hand.get_hand_type() == PokerHand.HIGH_CARD
#
# def test_makes_royal_flush():
#     hand = Hand(example_hands.royal_flush)
#     assert hand.makes_royal_flush() is True
#
# def test_makes_straight_flush():
#     hand = Hand(example_hands.straight_flush)
#     assert hand.makes_straight_flush() is True
#
def test_makes_four_of_a_kind():
    assert example_hands.four_of_a_kind.makes_four_of_a_kind() is True
#
# def test_makes_full_house():
#     hand = Hand(example_hands.full_house)
#     assert hand.makes_full_house() is True
#
# def test_makes_flush():
#     hand = Hand(example_hands.flush)
#     assert hand.makes_flush() is True
#
# def test_makes_straight():
#     hand = Hand(example_hands.straight)
#     assert hand.makes_straight() is True
#
def test_makes_three_of_a_kind():
    assert  example_hands.three_of_a_kind.makes_three_of_a_kind() is True

def test_makes_two_pair():
    assert example_hands.two_pair.makes_two_pair() is True

def test_makes_pair():
    assert example_hands.pair.makes_pair() is True
