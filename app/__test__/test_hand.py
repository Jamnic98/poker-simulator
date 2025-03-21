from pytest import raises
from app.card import Card
from app.hand import Hand
from app.utils import example_hands
from app.utils.cards import cards
from app.utils.enums import PokerHand


def test_init():
    hand = Hand()
    assert hand.cards == []
    test_cards = example_hands.three_of_a_kind.cards
    hand = Hand(test_cards)
    assert hand.cards == test_cards
    Hand([
        Card('7H'),
        Card('8H'),
        Card('9H'),
        Card('JH'),
        Card('10H'),
        Card('QH'),
        Card('AH'),
        Card('KH')]
    )
    assert raises(ValueError)

def test_init_with_duplicate_cards():
    Hand([Card('AS'), Card('AS')])
    assert raises(ValueError)

def test_add_cards():
    hand = Hand()
    hand.add_cards(example_hands.pair.cards)
    assert hand.cards == example_hands.pair.cards
    hand.add_cards([
        Card('7H'),
        Card('8H'),
        Card('9H'),
        Card('JH'),
        Card('10H'),
        Card('QH'),
        Card('AH'),
        Card('KH')
    ])
    assert raises(ValueError)

def test_get_hand_type():
    hand = example_hands.royal_flush
    assert hand.get_hand_type()[0] == PokerHand.ROYAL_FLUSH
    hand = example_hands.straight_flush
    assert hand.get_hand_type()[0] == PokerHand.STRAIGHT_FLUSH
    hand = example_hands.four_of_a_kind
    assert hand.get_hand_type()[0] == PokerHand.FOUR_OF_A_KIND
    hand = example_hands.full_house
    assert hand.get_hand_type()[0] == PokerHand.FULL_HOUSE
    hand = example_hands.hearts_flush
    assert hand.get_hand_type()[0] == PokerHand.FLUSH
    hand = example_hands.straight
    assert hand.get_hand_type()[0] == PokerHand.STRAIGHT
    hand = example_hands.three_of_a_kind
    assert hand.get_hand_type()[0] == PokerHand.THREE_OF_A_KIND
    hand = example_hands.two_pair
    assert hand.get_hand_type()[0] == PokerHand.TWO_PAIR
    hand = example_hands.pair
    assert hand.get_hand_type()[0] == PokerHand.PAIR
    hand = example_hands.high_card
    assert hand.get_hand_type()[0] == PokerHand.HIGH_CARD

def test_makes_royal_flush():
    assert example_hands.royal_flush.makes_royal_flush() is True
    assert example_hands.straight_flush.makes_royal_flush() is False
    assert example_hands.straight.makes_royal_flush() is False
    assert example_hands.hearts_flush.makes_royal_flush() is False

def test_makes_straight_flush():
    assert example_hands.straight_flush.makes_straight_flush() is True
    assert example_hands.hearts_flush.makes_straight_flush() is False

def test_makes_four_of_a_kind():
    assert example_hands.four_of_a_kind.makes_four_of_a_kind() is True
    assert example_hands.full_house.makes_four_of_a_kind() is False
    assert Hand([Card('AH'), Card('3H'), Card('2H'), Card('5D')]).makes_four_of_a_kind() is False
    assert example_hands.empty_hand.makes_four_of_a_kind() is False

def test_makes_full_house():
    assert example_hands.full_house.makes_full_house() is True
    assert example_hands.three_of_a_kind.makes_full_house() is False
    assert example_hands.four_of_a_kind.makes_full_house() is False
    assert example_hands.two_pair.makes_full_house() is False
    assert example_hands.empty_hand.makes_full_house() is False

def test_makes_flush():
    assert example_hands.hearts_flush.makes_flush() is True
    assert example_hands.royal_flush.makes_flush() is True
    assert example_hands.empty_hand.makes_flush() is False

def test_makes_straight():
    assert example_hands.straight.makes_straight() is True
    assert example_hands.royal_flush.makes_straight() is True

def test_makes_three_of_a_kind():
    assert example_hands.three_of_a_kind.makes_three_of_a_kind() is True
    assert example_hands.four_of_a_kind.makes_three_of_a_kind() is True
    assert example_hands.empty_hand.makes_three_of_a_kind() is False

def test_makes_two_pair():
    assert example_hands.two_pair.makes_two_pair() is True
    assert example_hands.full_house.makes_two_pair() is True
    assert example_hands.pair.makes_two_pair() is False
    assert example_hands.empty_hand.makes_two_pair() is False

def test_makes_pair():
    assert example_hands.pair.makes_pair() is True
    assert example_hands.two_pair.makes_pair() is True
    assert example_hands.single_card.makes_pair() is False
    assert example_hands.empty_hand.makes_pair() is False

def test_get_sorted_cards():
    # test 1
    test_hand = Hand([Card('8H'), Card('9H'), Card('JH'), Card('10H'), Card('QH'), Card('AH'), Card('KH')])
    ordered_test_hand = Hand([Card('9H'), Card('8H'), Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('10H')])
    for k, v in enumerate(test_hand.get_sorted_cards()):
        assert v.name == ordered_test_hand.cards[k].name

    # test 2
    test_hand = Hand([Card('2H'), Card('2C'), Card('3D'), Card('2S'), Card('8S'), Card('8D'), Card('KC')])
    ordered_test_hand = Hand([Card('2C'), Card('2H'), Card('KC'), Card('8D'), Card('8S'), Card('3D'), Card('2S')])
    for k, v in enumerate(test_hand.get_sorted_cards()):
        assert v.name == ordered_test_hand.cards[k].name

    # test 3
    test_hand = Hand([Card('6H'), Card('6C'), Card('3D'), Card('2S'), Card('8S'), Card('8D'), Card('KC')])
    ordered_test_hand = Hand([Card('6C'), Card('6H'), Card('KC'), Card('8D'), Card('8S'), Card('3D'), Card('2S')])
    for k, v in enumerate(test_hand.get_sorted_cards()):
        assert v.name == ordered_test_hand.cards[k].name


def test_get_two_pair_main_and_kickers():
    king_of_clubs = cards['king_of_clubs']
    king_of_hearts = cards['king_of_hearts']
    eight_of_diamonds = cards['eight_of_diamonds']
    eight_of_spades = cards['eight_of_spades']
    six_of_clubs = cards['six_of_clubs']
    six_of_hearts = cards['six_of_hearts']
    three_of_diamonds = cards['three_of_diamonds']
    two_of_spades = cards['two_of_spades']

    test_hand = Hand([
        six_of_hearts,
        eight_of_spades,
        six_of_clubs,
        three_of_diamonds,
        two_of_spades,
        eight_of_diamonds,
        king_of_clubs
    ])
    result = test_hand.get_two_pair_main_and_kickers()
    assert result == ((eight_of_spades, eight_of_diamonds, six_of_hearts, six_of_clubs), (king_of_clubs, ))

    test_hand = Hand([
        king_of_hearts,
        six_of_hearts,
        six_of_clubs,
        two_of_spades,
        eight_of_spades,
        eight_of_diamonds,
        king_of_clubs
    ])
    result = test_hand.get_two_pair_main_and_kickers()
    assert result == ((king_of_hearts, king_of_clubs, eight_of_spades, eight_of_diamonds), (six_of_hearts, ))
