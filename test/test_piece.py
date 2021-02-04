from piece import Piece
from piece_type import PieceType
from piece_colour import PieceColour


def test_type_getter():
    type = PieceType.PAWN
    colour = PieceColour.WHITE

    sut = Piece(type, colour)

    assert sut.type == type


def test_colour_getter():
    type = PieceType.PAWN
    colour = PieceColour.WHITE

    sut = Piece(type, colour)

    assert sut.colour == colour
