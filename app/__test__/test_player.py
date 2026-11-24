from pytest import raises
from app.card import Card
from app.player import DummyPlayer


def test_add_cards_up_to_two():
    player = DummyPlayer()
    player.add_cards([Card('AS')])
    player.add_cards([Card('KD')])
    assert [c.token for c in player.pocket] == ['AS', 'KD']


def test_add_cards_third_raises():
    player = DummyPlayer([Card('AS'), Card('KD')])
    with raises(ValueError):
        player.add_cards([Card('QH')])
    assert len(player.pocket) == 2


def test_reset():
    player = DummyPlayer([Card('AS'), Card('KD')])
    player.reset()
    assert player.pocket == []
