import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Poker simulation argument parser')

    # Player count argument (default: 2, range: 2-10)
    parser.add_argument(
        '-p', '--players',
        type=int,
        default=2,
        choices=range(2, 11),
        help='Number of players (default: 2, must be between 2 and 10)'
    )

    # Run count argument (required)
    parser.add_argument(
        '-r', '--runs',
        type=int,
        required=True,
        help='Number of simulation runs (required)'
    )

    # Top starting hands count argument (default: None, max value: 1326)
    parser.add_argument(
        '-tsh', '--top-starting-hands',
        type=int,
        default=None,
        choices=range(1, 1327),
        help='Number of top starting hands to analyze (default: None, max: 1326)'
    )

    # # Interstage calculation flag (y/n)
    # parser.add_argument(
    #     '-ci', '--calc-interstage',
    #     choices=['y', 'n'],
    #     default='n',
    #     help='Calculate relative hand strengths during interstage (y/n, default: n)'
    # )

    return parser.parse_args()
