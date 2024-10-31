from typing import List
from app.board import Board
from app.deck import Deck
from app.hand import Hand
from app.player import DummyPlayer
from app.utils.enums import PokerHand


class HandEvaluator:

    def rank_hands(self, board: Board, deck: Deck, players: List[DummyPlayer]) -> List[Hand]:
        # FIXME
        deck.shuffle()
        hand = Hand(players[0].pocket.copy().extend(board))
        return [hand]

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

    def makes_royal_flush(self, hand: Hand) -> bool:
        return False

    def makes_straight_flush(self, hand: Hand) -> bool:
        return False

    def makes_four_of_a_kind(self, hand: Hand) -> bool:
        return False

    def makes_full_house(self, hand: Hand) -> bool:
        return False

    def makes_flush(self, hand: Hand) -> bool:
        return False

    def makes_straight(self, hand: Hand) -> bool:
        return False

    def makes_three_of_a_kind(self, hand: Hand) -> bool:
        return False

    def makes_two_pair(self, hand: Hand) -> bool:
        return False

    def makes_pair(self, hand: Hand) -> bool:
        # two cards with matching faces
        return False
