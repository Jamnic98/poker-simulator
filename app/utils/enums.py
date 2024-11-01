from enum import Enum


class Mode(Enum):
    PRE_FLOP_SIM = "pre_flop_sim"


class PokerHand(Enum):
    ROYAL_FLUSH = "royal_flush"
    STRAIGHT_FLUSH = "straight_flush"
    FOUR_OF_A_KIND = "four_of_a_kind"
    FULL_HOUSE = "full_house"
    FLUSH = "flush"
    STRAIGHT = "straight"
    THREE_OF_A_KIND = "three_of_a_kind"
    TWO_PAIR = "two_pair"
    PAIR = "pair"
    HIGH_CARD = "high_card"
