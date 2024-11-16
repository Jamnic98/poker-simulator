from app.poker_simulator import PokerSimulator
from app.utils.constants import PLAYER_COUNT, RUN_COUNT
from app.utils.enums import Mode


def main():
    poker_simulator = PokerSimulator(
        mode=Mode.PRE_FLOP_SIM,
        run_count=RUN_COUNT,
        player_count=PLAYER_COUNT
    )
    poker_simulator.run()

if __name__ == "__main__":
    main()
