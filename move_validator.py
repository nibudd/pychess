from move import Move
from coordinate import Coordinate
from piece_type import PieceType
from piece_colour import PieceColour
from board import Board
from move_error import EmptyOriginError, ObstructedMoveError, ObstructedTargetError


def validate_origin(board: Board, move: Move):
    origin = move.origin
    if board.square_is_empty(origin):
        raise EmptyOriginError(origin)


def validate_move_is_possible_for_piece(board: Board, move: Move):
    pass


def validate_move_does_not_self_check(board: Board, move: Move):
    pass


def _is_move_possible_for_rook(board: Board, move: Move):
    pass
