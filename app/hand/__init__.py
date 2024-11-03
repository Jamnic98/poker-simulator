from typing import List, Optional
from app.card import Card
from app.utils.enums import PokerHand


class Hand:
    def __init__(self, cards: Optional[List[Card]]):
        self.cards = cards or []
        self.win_percentage = 0
        self.tie_percentage = 0

    def add_cards_to_hand(self, cards: List[Card]) -> None:
        self.cards.extend(cards)

    def makes_royal_flush(self) -> bool:
        return False

    def makes_straight_flush(self) -> bool:
        return False

    def makes_four_of_a_kind(self) -> bool:
        """Returns True if it is possible to make four of a kind"""
        face_dict = {}
        for card in self.cards:
            face_dict.setdefault(card.face, []).append(card)
            if len(face_dict[card.face]) == 4:
                return True
        return False

    def makes_full_house(self) -> bool:
        return False

    def makes_flush(self) -> bool:
        return False

    def makes_straight(self) -> bool:
        return False

    def makes_three_of_a_kind(self) -> bool:
        """Returns True if it is possible to make three of a kind"""
        face_dict = {}
        for card in self.cards:
            face_dict.setdefault(card.face, []).append(card)
            if len(face_dict[card.face]) == 3:
                return True
        return False

    def makes_two_pair(self) -> bool:
        """Returns True if it is possible to make two pairs"""
        pair_count = 0
        face_dict = {}
        for card in self.cards:
            face_dict.setdefault(card.face, []).append(card)
            if len(face_dict[card.face]) == 2:
                pair_count += 1
                if pair_count == 2:
                    return True
        return False

    def makes_pair(self) -> bool:
        """Returns True if it is possible to make a pair"""
        face_dict = {}
        for card in self.cards:
            face_dict.setdefault(card.face, []).append(card)
            if len(face_dict[card.face]) == 2:
                return True
        return False

    def get_hand_type(self) -> PokerHand:
        if self.makes_royal_flush():
            hand_type = PokerHand.ROYAL_FLUSH
        elif self.makes_straight_flush():
            hand_type = PokerHand.STRAIGHT_FLUSH
        elif self.makes_four_of_a_kind():
            hand_type = PokerHand.FOUR_OF_A_KIND
        elif self.makes_full_house():
            hand_type = PokerHand.FULL_HOUSE
        elif self.makes_flush():
            hand_type = PokerHand.FLUSH
        elif self.makes_straight():
            hand_type = PokerHand.STRAIGHT
        elif self.makes_three_of_a_kind():
            hand_type = PokerHand.THREE_OF_A_KIND
        elif self.makes_two_pair():
            hand_type = PokerHand.TWO_PAIR
        elif self.makes_pair():
            hand_type = PokerHand.PAIR
        else:
            hand_type = PokerHand.HIGH_CARD
        return hand_type



# class Pocket(Hand):
# pass
