from piece_type import PieceType
from piece_colour import PieceColour

class Piece:
    def __init__(self, type: PieceType, colour: PieceColour):
        self._type = type
        self._colour = colour

    @property
    def type(self) -> PieceType:
        return self._type

    @property
    def colour(self) -> PieceColour:
        return self._colour