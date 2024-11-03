from typing import List, Optional
from app.card import Card
from app.utils.enums import PokerHand
from app.utils.constants import FACES, CARD_FACE_VALUE_MAP


class Hand:
    def __init__(self, cards: Optional[List[Card]]=None):
        self.cards = cards or []
        self.win_percentage = 0
        self.tie_percentage = 0

    def __repr__(self):
        return f'Cards: {self.cards}\n' \
            f'Win %: {self.win_percentage}\n' \
            f'Tie %: {self.tie_percentage}\n'

    def __makes_x_of_a_kind(self, target_count: int) -> bool:
        if len(self.cards) < target_count:
            return False

        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1
            if face_counts[card.face] == target_count:
                return True

        return False

    def add_cards(self, cards: List[Card]) -> None:
        self.cards.extend(cards)

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

    def makes_royal_flush(self) -> bool:
        """Returns True if it is possible to make a royal flush."""
        if not self.makes_straight_flush():
            return False

        # Collect cards of the same suit
        flush_cards = [card for card in self.cards if card.suit == self.cards[0].suit]

        # Check for both '10' and 'A' in flush cards
        return {'10', 'A'}.issubset({card.face for card in flush_cards})

    def makes_straight_flush(self) -> bool:
        return self.makes_straight() and self.makes_flush()

    def makes_four_of_a_kind(self) -> bool:
        """Returns True if it is possible to make four of a kind"""
        return self.__makes_x_of_a_kind(target_count=4)

    def makes_full_house(self) -> bool:
        """Returns True if it is possible to make a full house."""
        if len(self.cards) < 5:
            return False

        face_dict = {}
        for card in self.cards:
            face_dict.setdefault(card.face, []).append(card)

        # Count the number of faces that have exactly 3 and exactly 2 cards
        pair = sum(1 for cards in face_dict.values() if len(cards) == 2)
        three_of_a_kind = sum(1 for cards in face_dict.values() if len(cards) == 3)

        # A full house requires at least one three-of-a-kind and one pair
        return three_of_a_kind >= 1 and pair >= 1

    def makes_flush(self) -> bool:
        """Returns True if it is possible to make a flush."""
        if len(self.cards) < 5:
            return False

        suit_count = {}
        for card in self.cards:
            suit_count[card.suit] = suit_count.get(card.suit, 0) + 1
            if suit_count[card.suit] == 5:
                return True

        return False

    def makes_straight(self) -> bool:
        """Returns True if it is possible to make a straight."""
        if len(self.cards) < 5:
            return False

        # Collect unique rank values, accounting for Ace's dual values (14 and 1)
        rank_values = set()
        for card in self.cards:
            card_value = CARD_FACE_VALUE_MAP.get(card.face)
            # handle aces
            if card.face == 'A':
                rank_values.update((card_value, 1))
            else:
                rank_values.add(card_value)

        # Sort the unique ranks to check for consecutive sequences
        sorted_ranks = sorted(rank_values)

        # Check for any sequence of 5 consecutive ranks
        for i in range(len(sorted_ranks) - 4):
            if sorted_ranks[i + 4] - sorted_ranks[i] == 4:
                return True

        return False

    def makes_three_of_a_kind(self) -> bool:
        """Returns True if it is possible to make three of a kind"""
        return self.__makes_x_of_a_kind(target_count=3)

    def makes_two_pair(self) -> bool:
        """Returns True if it is possible to make two pairs."""
        if len(self.cards) < 4:
            return False

        face_count = {}
        pair_count = 0
        for card in self.cards:
            face_count[card.face] = face_count.get(card.face, 0) + 1
            if face_count[card.face] == 2:
                pair_count += 1
                # Stop early if we have found two pairs
                if pair_count == 2:
                    return True
                    
        return False

    def makes_pair(self) -> bool:
        """Returns True if it is possible to make a pair."""
        return self.__makes_x_of_a_kind(target_count=2)

    # class Pocket(Hand):
    # pass
