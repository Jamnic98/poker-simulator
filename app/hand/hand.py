from typing import List, Optional, Tuple
from app.card import Card, CardHolder
from app.utils.enums import PokerHand
from app.utils.constants import CARD_FACE_VALUE_MAP


class Hand(CardHolder):
    def __init__(self, cards: Optional[List[Card]]=None):
        super().__init__(cards)
        self.hand_type = None
        try:
            if len(self) > 7:
                raise ValueError
            if cards and len(set(cards)) != len(set(self.cards)):
                raise ValueError
            self.hand_type = self.get_hand_type()
        except ValueError as e:
            self.reset()
            print(e)

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

    def add_cards(self, cards: List[Card]) -> None:
        if (cards_len := len(cards)) > 0:
            try:
                if cards_len + len(self) > 7:
                    raise ValueError
                if len(set(cards)) != len(set(cards.copy() + self.cards)):
                    raise ValueError
                self.cards.extend(cards)
            except ValueError as e:
                print(e)

    def get_hand_type(self) -> (PokerHand, Tuple[Card], Tuple[Card], str or None):
        """Returns a tuple: (PokerHand, <main_cards>, <kicker_cards>, <main_suit> if applicable)."""
        if not self.cards:
            return None, [], [], None
        # Check for hands in decreasing rank
        if self.makes_royal_flush():
            main_suit = self.get_flush_suit()
            main_cards = self.get_main_cards(main_suit, is_royal_flush=True)
            return PokerHand.ROYAL_FLUSH, main_cards, [], main_suit
        elif self.makes_straight_flush():
            main_suit = self.get_flush_suit()
            main_cards, kickers = self.get_main_cards(main_suit, is_flush=True, is_straight=True)
            return PokerHand.STRAIGHT_FLUSH, main_cards, kickers, main_suit
        elif self.makes_four_of_a_kind():
            main_cards, kickers = self.get_x_of_a_kind_main_and_kickers(x=4)
            return PokerHand.FOUR_OF_A_KIND, main_cards, kickers, None
        elif self.makes_full_house():
            main_cards, kickers = self.get_full_house_main_and_kickers()
            return PokerHand.FULL_HOUSE, main_cards, kickers, None
        elif self.makes_flush():
            main_suit = self.get_flush_suit()
            main_cards = self.get_main_cards(main_suit, is_flush=True)
            return PokerHand.FLUSH, main_cards, [], main_suit
        elif self.makes_straight():
            main_cards, kickers = self.get_main_cards(is_straight=True)
            return PokerHand.STRAIGHT, main_cards, kickers, None
        elif self.makes_three_of_a_kind():
            main_cards, kickers = self.get_x_of_a_kind_main_and_kickers(x=3)
            return PokerHand.THREE_OF_A_KIND, main_cards, kickers, None
        elif self.makes_two_pair():
            main_cards, kickers = self.get_two_pair_main_and_kickers()
            return PokerHand.TWO_PAIR, main_cards, kickers, None
        elif self.makes_pair():
            main_cards, kickers = self.get_x_of_a_kind_main_and_kickers(x=2)
            return PokerHand.PAIR, main_cards, kickers, None
        else:
            # High card
            sorted_cards = self.get_sorted_cards()
            main_cards = [sorted_cards[0]]
            kickers = sorted_cards[1:5]
            return PokerHand.HIGH_CARD, main_cards, kickers, None

    def get_flush_suit(self):
        suit_count = {}
        # Count the number of cards for each suit
        for card in self.cards:
            suit_count[card.suit] = suit_count.get(card.suit, 0) + 1
        # Find suits with at least 5 cards
        flush_suits = [suit for suit, count in suit_count.items() if count >= 5]
        if not flush_suits:
            return None  # No flush found

        if len(flush_suits) == 1:
            return flush_suits[0]  # Return the single flush suit

        # If multiple flush suits, choose the one with the highest-ranking cards
        # Build a dictionary of suited cards
        flush_candidates = {
            suit: sorted([card for card in self.cards if card.suit == suit],
                         key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)
            for suit in flush_suits
        }
        # Determine the best flush suit by highest-ranking card
        best_flush_suit = max(flush_candidates.keys(),
                              key=lambda s: CARD_FACE_VALUE_MAP[flush_candidates[s][0].face])
        return best_flush_suit

    def get_main_cards(self, main_suit=None, is_flush=False, is_straight=False, is_royal_flush=False) -> Tuple[Tuple, Tuple]:
        # Handle Flush and Royal Flush
        if is_flush or is_royal_flush:
            suited_cards = [card for card in self.cards if card.suit == main_suit]
            sorted_suited_cards = sorted(suited_cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)
            return tuple(sorted_suited_cards[:5]), ()

        # Handle Straight
        if is_straight:
            # Extract unique face values, accounting for Ace as both high and low
            sorted_cards = sorted(self.cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)
            unique_faces = list({CARD_FACE_VALUE_MAP[c.face]: c for c in sorted_cards}.values())
            ace_low_hand = False

            # Check for a straight sequence
            straight_cards = []
            for i in range(len(unique_faces) - 4):
                potential_straight = unique_faces[i:i + 5]
                if all(
                        CARD_FACE_VALUE_MAP[potential_straight[j].face] -
                        CARD_FACE_VALUE_MAP[potential_straight[j + 1].face] == 1
                        for j in range(4)
                ):
                    straight_cards = potential_straight
                    break

            # Special case: Ace-low straight (e.g., A-2-3-4-5)
            if not straight_cards and unique_faces[-1].face == '2' and unique_faces[0].face == 'A':
                ace_low_hand = True
                straight_cards = [unique_faces[-1], *unique_faces[-4:]]  # Order A-5 ascending

            if straight_cards:
                return tuple(straight_cards), ()

        # Default case for non-matching scenarios
        return (), ()

    def get_x_of_a_kind_main_and_kickers(self, x: int):
        """Returns main cards and kickers for 'x of a kind' hands."""
        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1

        main_cards = [card for card in self.cards if face_counts[card.face] == x]
        kickers = [card for card in self.cards if face_counts[card.face] < x]
        kickers = sorted(kickers, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)

        return sorted(main_cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True), kickers[:5 - x]

    def get_full_house_main_and_kickers(self):
        """Returns main cards and kickers for a full house."""
        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1

        # Identify the three of a kind and pair
        three_of_a_kind_faces = [face for face, count in face_counts.items() if count == 3]
        pair_faces = [face for face, count in face_counts.items() if count == 2]

        if not three_of_a_kind_faces or not pair_faces:
            return [], []

        # Get main cards
        main_cards = [card for card in self.cards if card.face in (three_of_a_kind_faces[0], pair_faces[0])]
        return sorted(main_cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True), []

    def get_two_pair_main_and_kickers(self):
        value_counts = {}
        for card in self.cards:
            value_counts[CARD_FACE_VALUE_MAP[card.face]] = value_counts.get(CARD_FACE_VALUE_MAP[card.face], []) + [card]

        # Extract pairs
        pairs = [cards for value, cards in value_counts.items() if len(cards) >= 2]
        sorted_pairs = sorted(pairs, key=lambda p: CARD_FACE_VALUE_MAP[p[0].face], reverse=True)

        if len(sorted_pairs) < 2:
            return [], []  # Not enough pairs for two-pair hand

        # Get the two highest pairs
        main_cards = sorted_pairs[0][:2] + sorted_pairs[1][:2]

        # Exclude the pairs from the kicker candidates
        pair_values = {CARD_FACE_VALUE_MAP[main_cards[0].face], CARD_FACE_VALUE_MAP[main_cards[2].face]}
        kicker_candidates = [card for card in self.cards if CARD_FACE_VALUE_MAP[card.face] not in pair_values]
        sorted_kickers = sorted(kicker_candidates, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)

        # Return main cards and a single kicker
        return main_cards, sorted_kickers[:1]

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
        # arrange cards by suit
        suits = {}
        for card in self.cards:
            if card.suit not in suits:
                suits[card.suit] = []
            card_value = CARD_FACE_VALUE_MAP.get(card.face)
            # update suits map and handle aces dual values (14, 1)
            if card.face == 'A':
                suits[card.suit].extend([card_value, 1])
            else:
                suits[card.suit].append(card_value)

        # test each suit for a straight
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
        # arrange cards by face
        face_dict = {}
        for card in self.cards:
            face_dict.setdefault(card.face, []).append(card)
        # count the number of faces that have exactly 3 and exactly 2 cards
        pair = sum(1 for cards in face_dict.values() if len(cards) == 2)
        three_of_a_kind = sum(1 for cards in face_dict.values() if len(cards) == 3)
        # test for a three-of-a-kind and one pair
        return three_of_a_kind > 0 and pair > 0

    def makes_flush(self) -> bool:
        """Returns True if it is possible to make a flush."""
        if len(self.cards) < 5:
            return False
        # collect suits and map to occurrence count
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
        # collect unique rank values
        rank_values = set()
        for card in self.cards:
            card_value = CARD_FACE_VALUE_MAP.get(card.face)
            # handle aces dual values (14, 1)
            if card.face == 'A':
                rank_values.update((card_value, 1))
            else:
                rank_values.add(card_value)
        # sort the unique ranks to check for consecutive sequences
        sorted_ranks = sorted(rank_values)
        # check for any sequence of 5 consecutive ranks
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
        # map card faces in cards to the number of occurrences
        pair_count = 0
        face_count_map = {}
        for card in self.cards:
            face_count_map[card.face] = face_count_map.get(card.face, 0) + 1
            if face_count_map[card.face] == 2:
                pair_count += 1
                # stop early once 2 pairs found
                if pair_count == 2:
                    return True
        return False

    def makes_pair(self) -> bool:
        """Returns True if it is possible to make a pair."""
        return self.__makes_x_of_a_kind(x=2)

    def get_sorted_cards(self) -> List[Card]:
        """Sorts cards in hand by sorting the pocket and board cards separately"""
        if len(self) == 0:
            return self.cards
        def sort_cards(cards: List[Card]):
            return sorted(
                    sorted(cards, key=lambda c: c.suit),
                    key=lambda c: CARD_FACE_VALUE_MAP.get(c.face), reverse=True
                )
        return sort_cards(self.cards[:2].copy()) + sort_cards(self.cards[2:].copy())

    def reset(self) -> None:
        """Resets the hand state"""
        self.cards.clear()
        self.hand_type = None


class Pocket(Hand):
    def __init__(self):
        super().__init__()
        self.win_percentage = 0
        self.tie_percentage = 0

    def __repr__(self):
        return f'Cards: {self.cards}\n' \
            f'Win %: {self.win_percentage}\n' \
            f'Tie %: {self.tie_percentage}\n'
