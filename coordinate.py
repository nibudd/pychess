from coordinate_error import InvalidRowError, InvalidColumnError


class Coordinate(tuple):
    def __new__(cls, row: int, col: int):
        _validate_coordinate(row, col)
        return tuple.__new__(cls, (row, col))

    @property
    def row(self) -> int:
        return self[0]

    @property
    def col(self) -> int:
        return self[1]


def _validate_coordinate(row: int, col: int):
    if not _is_valid_coordinate_value(row):
        raise InvalidRowError(row)

    if not _is_valid_coordinate_value(col):
        raise InvalidColumnError(col)


def _is_valid_coordinate_value(value: int) -> bool:
    min = 0
    max = 7
    if min <= value <= max:
        return True
    return False
