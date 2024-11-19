from typing import List, Tuple, Union
from app.board import Board
from app.deck import Deck
from app.hand import Hand
from app.player import DummyPlayer
from app.utils.enums import PokerHand


class HandEvaluator:
    @staticmethod
    def rank_hands(board: Board, players: List[DummyPlayer]) -> List[Union[Hand, Tuple[Hand, ...]]]:
        """
        Ranks all players' hands from strongest to weakest. If multiple hands tie,
        they are grouped as a tuple in the result list.
        """
        ranked_hands = []
        hands_dict: dict[PokerHand, List[Hand]] = {}

        # Evaluate each player's hand and group by hand type
        for player in players:
            hand = Hand([*player.pocket, *board.cards])
            hands_dict.setdefault(hand.hand_type[0], []).append(hand)

        # Sort hand types from strongest to weakest
        for ph in reversed(PokerHand):
            if ph in hands_dict:
                # Sort hands within this hand type group
                hands_dict[ph].sort(
                    key=lambda h: (
                        h.hand_type[1],  # Main cards (e.g., triplet in Full House)
                        h.hand_type[2]   # Kickers
                    ),
                    reverse=True  # Strongest hands first
                )

                # Group tied hands
                tied_hands = []
                previous_hand = None
                for hand in hands_dict[ph]:
                    if previous_hand is not None and (
                        hand.hand_type[1] == previous_hand.hand_type[1] and
                        hand.hand_type[2] == previous_hand.hand_type[2]
                    ):
                        # Add to tie group if same strength
                        tied_hands[-1].append(hand)
                    else:
                        # Start a new group
                        tied_hands.append([hand])
                    previous_hand = hand

                # Flatten tied hands into tuples or single elements
                for group in tied_hands:
                    if len(group) > 1:
                        ranked_hands.append(tuple(group))  # Add as tuple if tied
                    else:
                        ranked_hands.append(group[0])  # Add single hand

        return ranked_hands
