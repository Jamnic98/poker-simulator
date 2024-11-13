from typing import List
from collections import OrderedDict
from app.board import Board
from app.deck import Deck
from app.hand import Hand
from app.player import DummyPlayer
from app.utils.enums import PokerHand


class HandEvaluator:
    @staticmethod
    def rank_hands(board: Board, players: List[DummyPlayer]) -> dict[PokerHand, List[Hand]]:
        ranked_hands = []
        hands_dict: dict[PokerHand, List[Hand]] = {}
        for player in players:
            hand = Hand([*player.pocket, *board.cards])
            hands_dict.setdefault(hand.type[0], []).append(hand)

        for ph in reversed(PokerHand):
            ranked_hands.extend(hands_dict.get(ph) or [])
            
        return ranked_hands