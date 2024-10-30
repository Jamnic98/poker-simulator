from typing import List
from app.deck import Deck
from app.hand import Hand


def get_straight_flush(deck: Deck) -> List[Card]:
    return []

def get_four_of_a_kind(deck: Deck) -> List[Card]:
    return []

def get_full_house(deck: Deck) -> List[Card]:
    return []

def get_flush(deck: Deck) -> List[Card]:
    return []

def get_straight(deck: Deck) -> List[Card]:
    return []

def get_three_of_a_kind(deck: Deck) -> List[Card]:
    return []

def get_two_pair(deck: Deck) -> List[Card]:
    return []

def get_pair(deck: Deck) -> List[Card]:
    return []

def generate_hand_from_tokens(card_tokens: List[str]) -> Hand:
    return Hand([Card(token) for token in card_tokens])

# def generate_pair(card_count: int=2):
#     deck = Deck()


# def generate_two_pair(card_count: int=4):
#     deck = Deck()
#     for card in deck.cards():
#         # randomly select 2 cards from the deck with the same face_value (x2)
#         pass
