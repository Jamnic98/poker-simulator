from app.utils.constants import CARD_FACE_VALUE_MAP, CARD_FACE_NAME_MAP, CARD_SUIT_NAME_MAP


class Card:
    def __init__(self, token: str):
        self.face: str = token[:-1]
        self.suit: str = token[-1]
        self.name: str = self.__set_name(self.face, self.suit)
        self.face_value: int = CARD_FACE_VALUE_MAP.get(self.face)

    def __repr__(self):
        return str(self.face+self.suit)

    def __set_name(self, face: str, suit: str):
        return f'{CARD_FACE_NAME_MAP.get(face)} of {CARD_SUIT_NAME_MAP.get(suit)}'
