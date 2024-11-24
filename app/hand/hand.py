from typing import List, Tuple
from app.card import Card, CardHolder
from app.utils.enums import PokerHand
from app.utils.constants import CARD_FACE_VALUE_MAP


class Hand(CardHolder):
    def __init__(self, cards: List[Card]=None):
        super().__init__(cards)
        self.hand_type = None
        try:
            if len(self) > 7:
                raise ValueError
            if cards and len(set(cards)) != len(set(self.cards)):
                raise ValueError
            self.hand_type = self.get_hand_type()
        except ValueError as e:
            print(f'Init hand failed: {e}')

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
                print(f'Error adding cards to hand {e}')

    def get_hand_type(self) -> (PokerHand, Tuple[Card], Tuple[Card], str or None):
        """Returns a tuple: (PokerHand, <main_cards>, <kicker_cards>, <main_suit> if applicable)."""
        if not self.cards:
            return None, (), (), None
        # Check for hands in decreasing rank
        if self.makes_royal_flush():
            main_suit = self.get_flush_suit()
            main_cards, kickers = self.get_main_cards(main_suit, is_royal_flush=True)
            return PokerHand.ROYAL_FLUSH, main_cards, kickers, main_suit
        if self.makes_straight_flush():
            main_suit = self.get_flush_suit()
            main_cards, kickers = self.get_main_cards(main_suit, is_flush=True, is_straight=True)
            return PokerHand.STRAIGHT_FLUSH, main_cards, kickers, main_suit
        if self.makes_four_of_a_kind():
            main_cards, kickers = self.get_x_of_a_kind_main_and_kickers(x=4)
            return PokerHand.FOUR_OF_A_KIND, main_cards, kickers, None
        if self.makes_full_house():
            main_cards, kickers = self.get_full_house_main_and_kickers()
            return PokerHand.FULL_HOUSE, main_cards, kickers, None
        if self.makes_flush():
            main_suit = self.get_flush_suit()
            main_cards, kickers = self.get_main_cards(main_suit, is_flush=True)
            return PokerHand.FLUSH, main_cards, kickers, main_suit
        if self.makes_straight():
            main_cards, kickers = self.get_main_cards(is_straight=True)
            return PokerHand.STRAIGHT, main_cards, kickers, None
        if self.makes_three_of_a_kind():
            main_cards, kickers = self.get_x_of_a_kind_main_and_kickers(x=3)
            return PokerHand.THREE_OF_A_KIND, main_cards, kickers, None
        if self.makes_two_pair():
            main_cards, kickers = self.get_two_pair_main_and_kickers()
            return PokerHand.TWO_PAIR, main_cards, kickers, None
        if self.makes_pair():
            main_cards, kickers = self.get_x_of_a_kind_main_and_kickers(x=2)
            return PokerHand.PAIR, main_cards, kickers, None

        # High card
        sorted_cards = self.get_sorted_cards()
        main_cards = tuple([sorted_cards[0]])
        kickers = tuple(sorted_cards[1:5])
        return PokerHand.HIGH_CARD, main_cards, kickers, None

    def get_flush_suit(self) -> str or None:
        suit_count = {}
        # Count the number of cards for each suit
        for card in self.cards:
            suit_count[card.suit] = suit_count.get(card.suit, 0) + 1
        # Find suits with at least 5 cards
        flush_suits = [suit for suit, count in suit_count.items() if count >= 5]
        if not flush_suits:
            # No flush found
            return None

        if len(flush_suits) == 1:
            # Return the single flush suit
            return flush_suits[0]

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

    def get_main_cards(self, main_suit=None, is_flush=False, is_straight=False, is_royal_flush=False) -> Tuple:
        # Handle Royal Flush
        if is_royal_flush:
            suited_cards = [card for card in self.cards if card.suit == main_suit]
            sorted_suited_cards = sorted(suited_cards, key=lambda card: CARD_FACE_VALUE_MAP[card.face], reverse=True)[:5]
            return tuple(sorted_suited_cards), ()

        # Handle Flush (only when not part of a straight)
        if is_flush and not is_straight:
            suited_cards = [card for card in self.cards if card.suit == main_suit]
            sorted_suited_cards = sorted(suited_cards, key=lambda card: CARD_FACE_VALUE_MAP[card.face], reverse=True)
            return tuple(sorted_suited_cards), ()

        # Handle Straight
        if is_straight:
            # Filter by suit if flush is also present
            suited_cards = [card for card in self.cards if card.suit == main_suit] if is_flush else self.cards

            # Extract unique face values, accounting for Ace as both high and low
            sorted_cards = sorted(suited_cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)
            unique_faces = list({CARD_FACE_VALUE_MAP[card.face]: card for card in sorted_cards}.values())

            # Find the straight sequence
            straight_cards = []
            for i in range(len(unique_faces) - 4):
                potential_straight = unique_faces[i:i + 5]
                if all(CARD_FACE_VALUE_MAP[potential_straight[j].face] - CARD_FACE_VALUE_MAP[
                    potential_straight[j + 1].face] == 1 for j in range(4)):
                    straight_cards = potential_straight
                    break

            # Special case: Ace-low straight (A-2-3-4-5)
            if not straight_cards and 'A' in [card.face for card in unique_faces] and '2' in [card.face for card in
                                                                                              unique_faces]:
                ace = next(card for card in unique_faces if card.face == 'A')
                low_cards = [card for card in unique_faces if CARD_FACE_VALUE_MAP[card.face] <= 5 and card.face != 'A']
                straight_cards = [ace] + sorted(low_cards, key=lambda card: CARD_FACE_VALUE_MAP[card.face])

            if straight_cards:
                return tuple(straight_cards), ()

        return (), ()

    def get_x_of_a_kind_main_and_kickers(self, x: int):
        """Returns main cards and kickers for 'x of a kind' hands."""
        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1

        main_cards = [card for card in self.cards if face_counts[card.face] == x]
        kickers = sorted([card for card in self.cards if face_counts[card.face] < x], key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)
        return tuple(sorted(main_cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)), tuple(kickers[:5 - x])

    def get_full_house_main_and_kickers(self):
        """Returns main cards and kickers for a full house."""
        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1

        # Identify the three-of-a-kind and pair
        three_of_a_kind_faces = sorted(
            [face for face, count in face_counts.items() if count >= 3],
            key=lambda face: CARD_FACE_VALUE_MAP[face],
            reverse=True
        )
        pair_faces = sorted(
            [face for face, count in face_counts.items() if count >= 2 and face not in three_of_a_kind_faces],
            key=lambda face: CARD_FACE_VALUE_MAP[face],
            reverse=True
        )

        # Ensure both three-of-a-kind and pair are present
        if not three_of_a_kind_faces or not pair_faces:
            return (), ()

        # Select the strongest full house (highest three-of-a-kind, then highest pair)
        three_of_a_kind_face = three_of_a_kind_faces[0]
        pair_face = pair_faces[0]

        # Get main cards (three-of-a-kind)
        main_cards = [card for card in self.cards if card.face == three_of_a_kind_face][:3]

        # Get kickers (pair)
        kickers = [card for card in self.cards if card.face == pair_face][:2]

        return tuple(sorted(main_cards, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)), \
            tuple(sorted(kickers, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True))

    def get_two_pair_main_and_kickers(self):
        value_counts = {}
        for card in self.cards:
            value_counts[CARD_FACE_VALUE_MAP[card.face]] = value_counts.get(CARD_FACE_VALUE_MAP[card.face], []) + [card]

        # Extract pairs
        pairs = [cards for value, cards in value_counts.items() if len(cards) >= 2]
        sorted_pairs = sorted(pairs, key=lambda p: CARD_FACE_VALUE_MAP[p[0].face], reverse=True)

        if len(sorted_pairs) < 2:
            return (), ()

        # Get the two highest pairs
        main_cards = sorted_pairs[0][:2] + sorted_pairs[1][:2]

        # Exclude the pairs from the kicker candidates
        pair_values = {CARD_FACE_VALUE_MAP[main_cards[0].face], CARD_FACE_VALUE_MAP[main_cards[2].face]}
        kicker_candidates = [card for card in self.cards if CARD_FACE_VALUE_MAP[card.face] not in pair_values]
        sorted_kickers = sorted(kicker_candidates, key=lambda c: CARD_FACE_VALUE_MAP[c.face], reverse=True)

        # Return main cards and a single kicker
        return tuple(main_cards), tuple(sorted_kickers[:1])

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

        # Dictionary to track ranks for each suit
        suits = {}

        # Populate the dictionary
        for card in self.cards:
            if card.suit not in suits:
                suits[card.suit] = set()
            card_value = CARD_FACE_VALUE_MAP[card.face]
            suits[card.suit].add(card_value)
            if card.face == 'A':
                suits[card.suit].add(1)  # Add Ace-low value

        # Check for straight flush in each suit
        for _suit, ranks in suits.items():
            if len(ranks) < 5:
                continue
            sorted_ranks = sorted(ranks)
            consecutive_count = 1
            for i in range(1, len(sorted_ranks)):
                if sorted_ranks[i] == sorted_ranks[i - 1] + 1:
                    consecutive_count += 1
                    if consecutive_count == 5:
                        return True
                else:
                    consecutive_count = 1

        return False

    def makes_four_of_a_kind(self) -> bool:
        """Returns True if it is possible to make four of a kind"""
        return self.__makes_x_of_a_kind(x=4)

    def makes_full_house(self) -> bool:
        if len(self.cards) < 5:
            return False

        face_counts = {}
        for card in self.cards:
            face_counts[card.face] = face_counts.get(card.face, 0) + 1

        has_three_of_a_kind = False
        has_pair = False

        for count in face_counts.values():
            if count >= 3 and not has_three_of_a_kind:
                has_three_of_a_kind = True
                count -= 3  # Simulate using one three-of-a-kind
            if count >= 2:
                has_pair = True

            if has_three_of_a_kind and has_pair:
                return True

        return False

    def makes_flush(self) -> bool:
        """Returns True if it is possible to make a flush."""
        if len(self.cards) < 5:
            return False
        # Collect suits and map to occurrence count
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
        # Collect unique rank values
        rank_values = set()
        for card in self.cards:
            card_value = CARD_FACE_VALUE_MAP.get(card.face)
            # Handle aces dual values (14, 1)
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
        # Map card faces in cards to the number of occurrences
        pair_count = 0
        face_count_map = {}
        for card in self.cards:
            face_count_map[card.face] = face_count_map.get(card.face, 0) + 1
            if face_count_map[card.face] == 2:
                pair_count += 1
                # Stop early once 2 pairs found
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
                    sorted(cards, key=lambda c: c.suit), key=lambda c: CARD_FACE_VALUE_MAP.get(c.face), reverse=True
            )
        return sort_cards(self.cards[:2].copy()) + sort_cards(self.cards[2:].copy())

    def reset(self) -> None:
        """Resets the hand state"""
        self.cards.clear()
        self.hand_type = None


class Pocket(Hand):
    def __init__(self):
        super().__init__()
