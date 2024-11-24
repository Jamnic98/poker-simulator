from app.utils.constants import (
    CARD_FACE_VALUE_MAP,
    CARD_FACE_NAME_MAP,
    CARD_SUIT_NAME_MAP,
    CARD_SUIT_ICON_MAP,
    FACES,
    SUITS
)
from app.utils.logger_setup import logger


class Card:
    def __init__(self, token: str):
        face, suit = token[:-1], token[-1]
        try:
            if face not in FACES or suit not in SUITS:
                raise ValueError(f'Invalid token: {token}')
            self.token = token
            self.face: str = face
            self.suit: str = suit
            self.name: str = self.__set_name()
            self.face_value: int = CARD_FACE_VALUE_MAP.get(self.face)
        except ValueError as e:
            logger.error(e)

    def __str__(self):
        return self.face + CARD_SUIT_ICON_MAP.get(self.suit)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return CARD_FACE_VALUE_MAP[self.face] == CARD_FACE_VALUE_MAP[other.face]

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return CARD_FACE_VALUE_MAP[self.face] < CARD_FACE_VALUE_MAP[other.face]

    def __hash__(self):
        return hash(self.token)

    def __set_name(self):
        return f'{CARD_FACE_NAME_MAP.get(self.face)} of {CARD_SUIT_NAME_MAP.get(self.suit)}'
