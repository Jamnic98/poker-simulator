from utils.constants import CARD_FACE_VALUE_MAP, CARD_FACE_NAME_MAP, CARD_SUIT_NAME_MAP

class Card:
    def __init__(self, token: str):
        self.face = token[:-1]
        self.suit = token[-1]
        self.face_value = CARD_FACE_VALUE_MAP.get(self.face)
        self.name = self.__set_name(self.face, self.suit)

    def __set_name(self, face: str, suit: str) -> str:
        face_name = CARD_FACE_NAME_MAP.get(face)
        suit_name = CARD_SUIT_NAME_MAP.get(suit)
        return f'{face_name} of {suit_name}'

    def __repr__(self):
        return str(self.face+self.suit)
