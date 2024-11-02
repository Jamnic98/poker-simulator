from app.card import Card
from app.hand import Hand

# Royal Flush of Hearts
royal_flush = Hand([
    Card('AH'),
    Card('KH'),
    Card('QH'),
    Card('JH'),
    Card('10H')
])

# Straight Flush of Hearts 5 -> 9
straight_flush = Hand([
    Card('5H'),
    Card('6H'),
    Card('7H'),
    Card('8H'),
    Card('9H')
])

# Four 4's
four_of_a_kind = Hand([
    Card('4D'),
    Card('4C'),
    Card('4H'),
    Card('4S'),
    Card('AC')
])

# Full House, Kings in Aces
full_house = Hand([
    Card('AH'),
    Card('AS'),
    Card('AD'),
    Card('KH'),
    Card('KS')
])

# Flush of Hearts
flush = Hand([
    Card('2H'),
    Card('4H'),
    Card('6H'),
    Card('8H'),
    Card('10H')
])

# Straight, 9 -> K
straight = Hand([
    Card('KD'),
    Card('QD'),
    Card('JS'),
    Card('10H'),
    Card('9H')
])

# Three 3's
three_of_a_kind = Hand([
    Card('3H'),
    Card('3S'),
    Card('3C')
])

# Two Pair of 2's and 4's
two_pair = Hand([
    Card('2H'),
    Card('2S'),
    Card('4D'),
    Card('4C')
])

# Pair of Aces
pair = Hand([
    Card('AS'),
    Card('AC')
])

# High Card, Ace High
high_card = Hand([
    Card('AC'),
    Card('5H'),
    Card('2S'),
    Card('7D'),
    Card('10D'),
    Card('JH'),
    Card('9S')
])
