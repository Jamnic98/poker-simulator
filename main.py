from poker_simulator import PokerSimulator
from app.utils.constants import PLAYER_COUNT


def main():
    poker_simulator = PokerSimulator(player_count=PLAYER_COUNT)
    poker_simulator.run()

if __name__ == "__main__":
    main()
