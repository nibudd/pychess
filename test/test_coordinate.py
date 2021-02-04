import pytest
from coordinate import Coordinate
from coordinate_error import InvalidRowError, InvalidColumnError


@pytest.mark.parametrize(
    "row, col",
    [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (2, 6),
        (2, 7),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4),
        (3, 5),
        (3, 6),
        (3, 7),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (4, 5),
        (4, 6),
        (4, 7),
        (5, 0),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 5),
        (5, 6),
        (5, 7),
        (6, 0),
        (6, 1),
        (6, 2),
        (6, 3),
        (6, 4),
        (6, 5),
        (6, 6),
        (6, 7),
        (7, 0),
        (7, 1),
        (7, 2),
        (7, 3),
        (7, 4),
        (7, 5),
        (7, 6),
        (7, 7),
    ],
)
def test_coordinate_valid_coordinates_returns_object(row, col):
    coordinate = Coordinate(row, col)
    assert type(coordinate) == Coordinate


@pytest.mark.parametrize("row", [-10, -1, 8, 20])
def test_coordinate_invalid_row_raises_InvalidRowException(row):
    with pytest.raises(InvalidRowError):
        Coordinate(row, 0)


@pytest.mark.parametrize("col", [-10, -1, 8, 20])
def test_coordinate_invalid_col_raises_InvalidColumnException(col):
    with pytest.raises(InvalidColumnError):
        Coordinate(0, col)


def test_row_returns_value_0():
    coordinate = Coordinate(0, 1)

    assert coordinate.row == coordinate[0]


def test_col_returns_value_1():
    coordinate = Coordinate(0, 1)

    assert coordinate.col == coordinate[1]
