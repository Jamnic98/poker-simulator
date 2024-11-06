from typing import List
from collections import OrderedDict
from app.board import Board
from app.deck import Deck
from app.hand import Hand
from app.player import DummyPlayer
from app.utils.enums import PokerHand


class HandEvaluator:
    def rank_hands(self, board: Board, deck: Deck, players: List[DummyPlayer]) -> List[Hand]:
        hands: dict[PokerHand, List[Hand]] = {}
        for player in players:
            hand = Hand([*player.pocket, *board.cards])
            hand_type = hand.get_hand_type()
            hands.setdefault(hand.get_hand_type(), []).append(hand)

        # rank hands and handle ties
        ranked_hands = []
        for ph in PokerHand:
            h = hands.get(ph)
            if h:
                ranked_hands.extend(h)

        return ranked_hands
