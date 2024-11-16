from app.utils.constants import CARD_FACE_VALUE_MAP, CARD_FACE_NAME_MAP, CARD_SUIT_NAME_MAP, CARD_SUIT_ICON_MAP, FACES, SUITS


class Card:
    def __init__(self, token: str):
        face, suit = token[:-1], token[-1]
        try:
            if face not in FACES or suit not in SUITS:
                raise ValueError(f'Invalid token: {token}')
            self.face: str = face
            self.suit: str = suit
            self.name: str = self.__set_name()
            self.face_value: int = CARD_FACE_VALUE_MAP.get(self.face)
        except ValueError as e:
            print(e)

    def serialize(self):
        return {"face": self.face, "suit": self.suit}

    @classmethod
    def deserialize(cls, data):
        return cls(data["face"], data["suit"])

    def __repr__(self):
        return str(self.face + CARD_SUIT_ICON_MAP.get(self.suit))

    def __set_name(self):
        return f'{CARD_FACE_NAME_MAP.get(self.face)} of {CARD_SUIT_NAME_MAP.get(self.suit)}'
