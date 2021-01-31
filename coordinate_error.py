class CoordinateError(Exception):
    pass

class InvalidRowError(CoordinateError):
    def __init__(self, row: int):
        self.message = f"invalid coordinate row {row}."

class InvalidColumnError(CoordinateError):
    def __init__(self, col: int):
        self.message = f"invalid coordinate column {col}."