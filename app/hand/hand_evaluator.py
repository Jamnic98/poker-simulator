from typing import List, Tuple, Union
from app.hand import Hand


class HandEvaluator:
    @staticmethod
    def rank_hands(hands: Tuple[Hand, ...]) -> List[Union[Hand, Tuple[Hand, ...]]]:
        """
        Ranks all players' hands from strongest to weakest. Hands with equal
        strength (a draw / split pot) are grouped as a tuple in the result list.
        """
        ordered = sorted(hands, key=lambda h: h.get_strength(), reverse=True)

        groups: List[List[Hand]] = []
        for hand in ordered:
            if groups and HandEvaluator._is_tied(groups[-1][0], hand):
                groups[-1].append(hand)
            else:
                groups.append([hand])

        return [tuple(group) if len(group) > 1 else group[0] for group in groups]

    @staticmethod
    def _is_tied(hand1: Hand, hand2: Hand) -> bool:
        """Checks if two hands are tied (same category, main cards and kickers)."""
        return hand1.get_strength() == hand2.get_strength()
