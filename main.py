import argparse
from sys import argv
from app.poker_simulator import PokerSimulator
from app.utils.enums import Mode
from app.utils.arg_parser import parse_arguments
from app.settings import config


def main():
    arguments = parse_arguments()
    poker_simulator = PokerSimulator(
        mode=Mode.PRE_FLOP_SIM,
        player_count=arguments.players,
        run_count=arguments.runs,
        top_starting_hands=arguments.top_starting_hands
    )
    poker_simulator.run()

if __name__ == "__main__":
    main()
