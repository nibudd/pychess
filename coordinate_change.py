from coordinate_error import InvalidRowError, InvalidColumnError

class CoordinateChange(tuple):
    def __new__(cls, row: int, col: int):
        _validate_coordinate_change(row, col)
        return tuple.__new__(cls, (row, col))

    @property
    def row(self) -> int:
        return self[0]

    @property
    def col(self) -> int:
        return self[1]


def _validate_coordinate_change(row: int, col: int):
    if not _is_valid_coordinate_value(row):
        raise InvalidRowError(row)

    if not _is_valid_coordinate_value(col):
        raise InvalidColumnError(col)


def _is_valid_coordinate_value(value: int) -> bool:
    abs_max = 7
    if abs(value) <= abs_max:
        return True
    return False