from app.poker_simulator import PokerSimulator
from app.utils.constants import PLAYER_COUNT
from app.utils.enums import Mode


def main():
    poker_simulator = PokerSimulator(player_count=PLAYER_COUNT, mode=Mode.PREFLOP_SIM)
    poker_simulator.run()

if __name__ == "__main__":
    main()
