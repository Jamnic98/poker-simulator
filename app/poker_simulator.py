from dealer import Dealer
from player import Player


class PokerSimulator:
    def __init__(self, player_count):
        self.running = False
        self.dealer = Dealer()
        self.players = self.__set_players(player_count)
        # init cards
        # init graphing

    def run(self):
        self.dealer.shuffle_cards()
        # self.deck.shuffle()
        # deal cards

        self.__graph_results()
        # self.running = True
        # while self.running:

    def __graph_results(self):
        pass

    def __set_players(self, player_count: int):
        return [Player() for _ in range(player_count)]
