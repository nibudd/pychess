from coordinate import Coordinate
from move import Move


def test_origin_returns_value_0():
    coordinate0 = Coordinate(0, 0)
    coordinate1 = Coordinate(1, 1)
    piece_move = Move(coordinate0, coordinate1)

    assert piece_move.origin == piece_move[0]


def test_target_returns_value_1():
    coordinate0 = Coordinate(0, 0)
    coordinate1 = Coordinate(1, 1)
    piece_move = Move(coordinate0, coordinate1)

    assert piece_move.target == piece_move[1]
