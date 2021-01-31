from board_error import EmptySquareError
from coordinate import Coordinate
from piece import Piece
from piece_type import PieceType
from piece_colour import PieceColour

class Board:
    def __init__(self):
        self._pieces = _setup_board()

    @property
    def pieces(self) -> {Coordinate: Piece}:
        return self._pieces

    def piece(self, coordinate: Coordinate) -> Piece:
        try:
            return self._pieces[coordinate]
        except KeyError:
            raise EmptySquareError(coordinate)

    def square_is_empty(self, coordinate: Coordinate) -> bool:
        try:
            self.piece(coordinate)
        except EmptySquareError:
            return True

        return False

    def square_has_a_piece(self, coordinate: Coordinate) -> bool:
        return not self.square_is_empty(coordinate)

    def square_has_white_piece(self, coordinate: Coordinate) -> bool:
        try:
            piece = self.piece(coordinate)
        except EmptySquareError:
            return False

        if piece.colour == PieceColour.WHITE:
            return True

        return False
    
    def square_has_black_piece(self, coordinate: Coordinate) -> bool:
        try:
            piece = self.piece(coordinate)
        except EmptySquareError:
            return False

        if piece.colour == PieceColour.BLACK:
            return True

        return False

    def square_has_king(self, coordinate: Coordinate) -> bool:
        try:
            piece = self.piece(coordinate)
        except EmptySquareError:
            return False

        if piece.type == PieceType.KING:
            return True

        return False

def _setup_board() -> {Coordinate: Piece}:
    return {
            Coordinate(0, 0): Piece(PieceType.ROOK, PieceColour.WHITE),
            Coordinate(0, 1): Piece(PieceType.KNIGHT, PieceColour.WHITE),
            Coordinate(0, 2): Piece(PieceType.BISHOP, PieceColour.WHITE),
            Coordinate(0, 3): Piece(PieceType.QUEEN, PieceColour.WHITE),
            Coordinate(0, 4): Piece(PieceType.KING, PieceColour.WHITE),
            Coordinate(0, 5): Piece(PieceType.BISHOP, PieceColour.WHITE),
            Coordinate(0, 6): Piece(PieceType.KNIGHT, PieceColour.WHITE),
            Coordinate(0, 7): Piece(PieceType.ROOK, PieceColour.WHITE),
            
            Coordinate(1, 0): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 1): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 2): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 3): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 4): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 5): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 6): Piece(PieceType.PAWN, PieceColour.WHITE),
            Coordinate(1, 7): Piece(PieceType.PAWN, PieceColour.WHITE),

            Coordinate(7, 0): Piece(PieceType.ROOK, PieceColour.BLACK),
            Coordinate(7, 1): Piece(PieceType.KNIGHT, PieceColour.BLACK),
            Coordinate(7, 2): Piece(PieceType.BISHOP, PieceColour.BLACK),
            Coordinate(7, 3): Piece(PieceType.QUEEN, PieceColour.BLACK),
            Coordinate(7, 4): Piece(PieceType.KING, PieceColour.BLACK),
            Coordinate(7, 5): Piece(PieceType.BISHOP, PieceColour.BLACK),
            Coordinate(7, 6): Piece(PieceType.KNIGHT, PieceColour.BLACK),
            Coordinate(7, 7): Piece(PieceType.ROOK, PieceColour.BLACK),
            
            Coordinate(6, 0): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 1): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 2): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 3): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 4): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 5): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 6): Piece(PieceType.PAWN, PieceColour.BLACK),
            Coordinate(6, 7): Piece(PieceType.PAWN, PieceColour.BLACK)
        }
