from board import Board
from coordinate import Coordinate
from piece_type import PieceType

def list_piece_moves(board: Board, origin: Coordinate) -> [Coordinate]:
    pass

_piece_incrementers = {
    PieceType.PAWN: [()]
    PieceType.KNIGHT: 
    PieceType.BISHOP: 
    PieceType.ROOK: 
    PieceType.QUEEN: 
    PieceType.KING: 
}

# todo: maybe an object initialized with the piece's current position
# it contains the logic of possible moves to check, and cycles through
# all of them, compiling a list of possible moves for that piece

# or it compiles a list of all possible moves for all possible pieces