from .royal_flush import *
from .straight_flush import *
from .four_of_a_kind import *
from .full_house import *
from .flush import *
from .straight import *
from .three_of_a_kind import *
from .two_pair import *
from .pair import *
from .high_card import *


empty_hand = Hand([])

single_card = Hand([
    Card('AS'),
])

unpaired_and_unsuited_pocket = Hand([
    Card('2C'),
    Card('3H')
])

suited_pocket = Hand([
    Card('4C'),
    Card('KC')
])
