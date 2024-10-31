from app.card import Card
from app.hand import Hand


royal_flush = Hand([
    Card('KH'),
    Card('QH'),
    Card('JH'),
    Card('10H'),
    Card('2C'),
    Card('4S')
    ]
)

straight_flush = Hand([
    Card('9H'),
    Card('8H'),
    Card('7H'),
    Card('6H'),
    Card('5H')
])

four_of_a_kind = Hand([
    Card('4D'),
    Card('4C'),
    Card('4H'),
    Card('4S'),
    Card('AC')
])

full_house = Hand([
    Card('AH'),
    Card('AS'),
    Card('AD'),
    Card('KH'),
    Card('KS')
])

flush = Hand([
    Card('2H'),
    Card('4H'),
    Card('6H'),
    Card('8H'),
    Card('10H')
])

straight = Hand([
    Card('KD'),
    Card('QD'),
    Card('JS'),
    Card('10H'),
    Card('9H')
])

three_of_a_kind = Hand([
    Card('AH'),
    Card('AS'),
    Card('AC')
])

two_pair = Hand([
    Card('2H'),
    Card('2S'),
    Card('4D'),
    Card('4C')
])

pair = Hand([
    Card('AS'),
    Card('AC')
])

high_card = Hand([
    Card('AC'),
    Card('5H'),
    Card('2S'),
    Card('7D'),
    Card('10D'),
    Card('JH'),
    Card('9S')
])
