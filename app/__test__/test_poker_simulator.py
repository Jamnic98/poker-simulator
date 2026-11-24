from app.board import Board
from app.card import Card
from app.player import DummyPlayer
from app.poker_simulator import PokerSimulator
from app.utils.enums import Mode


def make_sim() -> PokerSimulator:
    return PokerSimulator(mode=Mode.PRE_FLOP_SIM, player_count=2, run_count=1, top_starting_hands=None)


def result_entry(sim, board_cards, pockets):
    board = Board([Card(t) for t in board_cards])
    players = tuple(DummyPlayer([Card(t) for t in pocket]) for pocket in pockets)
    return sim._PokerSimulator__get_single_pre_flop_sim_result_entry(board, players)


def test_split_pot_marks_all_tied_players_as_winners():
    # board straight 5-9: both players play the board
    df = result_entry(
        make_sim(),
        ['5D', '6C', '7H', '8S', '9D'],
        [['2C', '3H'], ['AC', 'KH']],
    )
    assert len(df) == 2
    assert df['is_winning_hand'].all()
    assert (df['hand_type'] == 'STRAIGHT').all()


def test_single_winner():
    # rainbow board, pair of aces vs 7-2 offsuit
    df = result_entry(
        make_sim(),
        ['2D', '9C', 'JS', 'QH', 'KC'],
        [['AS', 'AD'], ['7H', '2C']],
    )
    assert len(df) == 2
    assert df['is_winning_hand'].sum() == 1
    winner = df[df['is_winning_hand']].iloc[0]
    assert winner['hand_type'] == 'PAIR'
    assert set(winner['pocket']) == {'AS', 'AD'}


def test_tie_group_not_at_top_does_not_crash():
    # board has a pair of aces and a king; P2 holds AC KH (full house, wins
    # outright), P0 and P1 both play the board pair and tie for second
    df = result_entry(
        make_sim(),
        ['AH', 'AD', 'KD', 'QS', 'JC'],
        [['2C', '3H'], ['4S', '5D'], ['AC', 'KH']],
    )
    assert len(df) == 3
    assert df['is_winning_hand'].sum() == 1
    winner = df[df['is_winning_hand']].iloc[0]
    assert winner['hand_type'] == 'FULL_HOUSE'
    assert set(winner['pocket']) == {'AC', 'KH'}
