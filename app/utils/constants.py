PLAYER_COUNT = 2
RUN_COUNT = int(1e6)


CARD_FACE_VALUE_MAP = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

CARD_FACE_NAME_MAP = {
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
    'A': 'Ace'
}

CARD_SUIT_NAME_MAP = {
    'C': 'Clubs',
    'D': 'Diamonds',
    'H': 'Hearts',
    'S': 'Spades'
}

CARD_SUIT_ICON_MAP = {
    'C': ' ♣ ',
    'D': ' ♦ ',
    'H': ' ♥ ',
    'S': ' ♠ '
}

FACES = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
SUITS = ['C', 'D', 'H', 'S']
