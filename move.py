from coordinate import Coordinate


class Move(tuple):
    def __new__(cls, origin: Coordinate, target: Coordinate):
        return tuple.__new__(cls, (origin, target))

    @property
    def origin(self) -> Coordinate:
        return self[0]

    @property
    def target(self) -> Coordinate:
        return self[1]
