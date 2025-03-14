from typing import List, Tuple, Union
from app.hand import Hand
from app.utils.enums import PokerHand


class HandEvaluator:
    @staticmethod
    def rank_hands(hands: Tuple[Hand, ...]) -> List[Union[Hand, Tuple[Hand, ...]]]:
        """
        Ranks all players' hands from strongest to weakest. If multiple hands tie,
        they are grouped as a tuple in the result list.
        """
        ranked_hands = []
        hands_dict: dict[PokerHand, List[Hand]] = {}

        # Group hands by their hand type
        for hand in hands:
            hands_dict.setdefault(hand.hand_type[0], []).append(hand)

        # Rank hand types by poker hierarchy
        for ph in reversed(PokerHand):
            if ph in hands_dict:
                # Sort hands within this type by main cards and kickers
                hands_dict[ph].sort(
                    key=lambda h: (
                        sorted(h.hand_type[1], reverse=True),  # Main cards
                        sorted(h.hand_type[2], reverse=True)   # Kickers
                    ),
                    reverse=True
                )

                # Group tied hands
                grouped_hands = []
                for idx, hand in enumerate(hands_dict[ph]):
                    if idx > 0 and HandEvaluator._is_tied(hands_dict[ph][idx - 1], hand):
                        grouped_hands[-1].append(hand)
                    else:
                        grouped_hands.append([hand])

                # Flatten groups of tied hands into tuples or single entries
                for group in grouped_hands:
                    if len(group) > 1:
                        ranked_hands.append(tuple(group))
                    else:
                        ranked_hands.append(group[0])

        return ranked_hands

    @staticmethod
    def _is_tied(hand1: Hand, hand2: Hand) -> bool:
        """Checks if two hands are tied."""
        return hand1.hand_type[1] == hand2.hand_type[1] and hand1.hand_type[2]
