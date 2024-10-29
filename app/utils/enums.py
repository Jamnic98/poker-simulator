from enum import Enum


class Mode(Enum):
    PREFLOP_SIM = "preflop_sim"


class PokerHands(Enum):
    HIGH_CARD = "high_card"
    ONE_PAIR = "one_pair"
    TWO_PAIR = "two_pair"
    THREE_OF_A_KIND = "three_of_a_kind"
    STRAIGHT = "straight"
    FLUSH = "flush"
    FULL_HOUSE = "full_house"
    FOUR_OF_A_KIND = "four_of_a_kind"
    STRAIGHT_FLUSH = "straigh_flush"
    ROYAL_FLUSH = "royal_flush"
