import pytest
from rps_bot import Move


def test_move_parsing():
    assert Move.from_user_input("r") == Move.ROCK
    assert Move.from_user_input("Paper") == Move.PAPER
    assert Move.from_user_input("S") == Move.SCISSORS
    with pytest.raises(ValueError):
        Move.from_user_input("x")


@pytest.mark.parametrize(
    "left,right,expect",
    [
        (Move.ROCK, Move.SCISSORS, True),
        (Move.SCISSORS, Move.ROCK, False),
        (Move.PAPER, Move.PAPER, False),
    ],
)
def test_beats_logic(left, right, expect):
    assert left.beats(right) is expect
