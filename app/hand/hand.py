from typing import List, Optional
from app.card import Card, CardHolder
from app.utils.enums import PokerHand
from app.utils.constants import CARD_FACE_VALUE_MAP


class Hand(CardHolder):
    def __init__(self, cards: Optional[List[Card]]=None):
        super().__init__(cards)
        self.type = self.get_hand_type()

    def __makes_x_of_a_kind(self, x: int) -> bool:
        """returns true if x number of occurrences of a card face in hand"""
        if len(self.cards) < x:
            return False
        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1
            if face_counts[card.face] == x:
                return True
        return False

    def get_hand_type(self) -> (PokerHand, List, List) or None:
        """returns the PokerHand which corresponds
         to the type of hand that can be made from the cards in the hand"""
        card_count = len(self.cards)
        if card_count == 0:
            return None
        elif self.makes_royal_flush():
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
        return hand_type, (), ()

    def makes_royal_flush(self) -> bool:
        """Returns True if it is possible to make a royal flush."""
        if len(self.cards) < 5:
            return False
        # Group cards by suit and get unique values for each suit
        suits = {}
        for card in self.cards:
            value = CARD_FACE_VALUE_MAP.get(card.face, card.face)
            if card.suit not in suits:
                suits[card.suit] = set()
            suits[card.suit].add(value)
        # Check each suit for the royal flush ranks (10, J, Q, K, A)
        royal_flush_ranks = {10, 11, 12, 13, 14}
        for ranks in suits.values():
            if royal_flush_ranks.issubset(ranks):
                return True
        return False

    def makes_straight_flush(self) -> bool:
        if len(self.cards) < 5:
            return False

        # Step 1: Organize cards by suit
        suits = {}
        for card in self.cards:
            if card.suit not in suits:
                suits[card.suit] = []
            # Handle Ace's dual values
            card_value = CARD_FACE_VALUE_MAP.get(card.face)
            if card.face == 'A':
                suits[card.suit].extend([card_value, 1])
            else:
                suits[card.suit].append(card_value)

        # Step 2: Check each suit for a straight
        for suit, ranks in suits.items():
            if len(ranks) < 5:
                continue
            # sort and remove duplicates
            sorted_ranks = sorted(set(ranks))
            # check for a sequence of 5 consecutive ranks
            for i in range(len(sorted_ranks) - 4):
                if sorted_ranks[i + 4] - sorted_ranks[i] == 4:
                    return True
        return False

    def makes_four_of_a_kind(self) -> bool:
        """Returns True if it is possible to make four of a kind"""
        return self.__makes_x_of_a_kind(x=4)

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
        return three_of_a_kind > 0 and pair > 0

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
        return self.__makes_x_of_a_kind(x=3)

    def makes_two_pair(self) -> bool:
        """Returns True if it is possible to make two pairs."""
        if len(self.cards) < 4:
            return False

        pair_count = 0
        face_count_map = {}
        for card in self.cards:
            face_count_map[card.face] = face_count_map.get(card.face, 0) + 1
            if face_count_map[card.face] == 2:
                pair_count += 1
                # Stop early if we have found two pairs
                if pair_count == 2:
                    return True
        return False

    def makes_pair(self) -> bool:
        """Returns True if it is possible to make a pair."""
        return self.__makes_x_of_a_kind(x=2)

    def get_sorted_cards(self) -> List[Card]:
        return self.cards



class Pocket(Hand):
    def __init__(self):
        super().__init__()
        self.win_percentage = 0
        self.tie_percentage = 0

    def __repr__(self):
        return f'Cards: {self.cards}\n' \
            f'Win %: {self.win_percentage}\n' \
            f'Tie %: {self.tie_percentage}\n'
