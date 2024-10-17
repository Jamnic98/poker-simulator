from settings import config
from poker_simulator import PokerSimulator


PLAYER_COUNT = 2

def main():
    poker_simulator = PokerSimulator(player_count=PLAYER_COUNT)
    poker_simulator.run()

if __name__ == "__main__":
    main()
