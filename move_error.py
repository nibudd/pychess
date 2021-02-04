from coordinate import Coordinate


class MoveError(Exception):
    pass


class EmptyOriginError(MoveError):
    def __init__(self, origin: Coordinate):
        self.message = f"Empty move origin {origin}."


class ObstructedMoveError(MoveError):
    def __init__(self, intermediate_square: Coordinate):
        self.message = f"Move is obstructed at {intermediate_square}."


class ObstructedTargetError(MoveError):
    def __init__(self, target: Coordinate):
        self.message = f"Move is obstructed at {target}."
