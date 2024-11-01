# from typing import List
# from app.board import Board
# from app.deck import Deck
from app.hand.hand import Hand
# from app.player import DummyPlayer
from app.utils.enums import PokerHand


class HandEvaluator:

    # @staticmethod
    # def rank_hands(board: Board, deck: Deck, players: List[DummyPlayer]) -> List[Hand]:
    #     return []

    @staticmethod
    def makes_royal_flush(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_straight_flush(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_four_of_a_kind(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_full_house(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_flush(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_straight(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_three_of_a_kind(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_two_pair(hand: Hand) -> bool:
        return False

    @staticmethod
    def makes_pair(hand: Hand) -> bool:
        # two cards with matching faces
        return False

    def get_hand_type(self, hand: Hand) -> PokerHand:
        if self.makes_royal_flush(hand):
            hand_type = PokerHand.ROYAL_FLUSH
        elif self.makes_straight_flush(hand):
            hand_type = PokerHand.STRAIGHT_FLUSH
        elif self.makes_four_of_a_kind(hand):
            hand_type = PokerHand.FOUR_OF_A_KIND
        elif self.makes_full_house(hand):
            hand_type = PokerHand.FULL_HOUSE
        elif self.makes_flush(hand):
            hand_type = PokerHand.FLUSH
        elif self.makes_straight(hand):
            hand_type = PokerHand.STRAIGHT
        elif self.makes_three_of_a_kind(hand):
            hand_type = PokerHand.THREE_OF_A_KIND
        elif self.makes_two_pair(hand):
            hand_type = PokerHand.TWO_PAIR
        elif self.makes_pair(hand):
            hand_type = PokerHand.PAIR
        else:
            hand_type = PokerHand.HIGH_CARD
        return hand_type
