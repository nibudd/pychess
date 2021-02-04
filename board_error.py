from coordinate import Coordinate


class BoardError(Exception):
    pass


class EmptySquareError(BoardError):
    def __init__(self, coordinate: Coordinate):
        self.message = f"Coordinate ({coordinate.row}, {coordinate.col}) is empty."
