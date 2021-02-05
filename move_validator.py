from move import Move
from coordinate import Coordinate
from piece_type import PieceType
from piece_colour import PieceColour
from board import Board
from move_error import EmptyOriginError, ObstructedMoveError, ObstructedTargetError


def validate_move(board: Board, move: Move):
    _validate_origin(board, move)
    _validate_piece_move_legality(board, move)
    _validate_move_does_not_self_check(board, move)


def _validate_origin(board: Board, move: Move):
    origin = move.origin
    if board.square_is_empty(origin):
        raise EmptyOriginError(origin)


_piece_move_validators = {
    PieceType.PAWN: _pawn_move_validator,
    PieceType.KNIGHT: _knight_move_validator,
    PieceType.BISHOP: _bishop_move_validator,
    PieceType.ROOK: _rook_move_validator,
    PieceType.QUEEN: _queen_move_validator,
    PieceType.KING: _king_move_validator,
}


def _validate_piece_move_legality(board: Board, move: Move):
    piece = board.piece(move.origin)
    piece_move_validator = _piece_move_validators[piece.type]
    piece_move_validator(board, move)


def _validate_move_does_not_self_check(board: Board, move: Move):
    pass


def _pawn_move_validator(board: Board, move: Move) -> bool:
    origin = move.origin
    piece = board.piece(origin)

    if piece.colour == PieceColour.WHITE:
        sign = 1
    else:
        sign = -1
        
    double_step = origin + (sign*2, 0)
    single_step = origin + (sign*1, 0)
    take_left = origin + (sign*1, -1)
    take_right = origin + (sign*1, 1)    
    
    legal_moves = []
    
    if _pawn_has_not_moved(board, origin):
        if board.square_is_empty(single_step) and board.square_is_empty(double_step):
            legal_moves.append(double_step)

    if board.square_is_empty(single_step):
        legal_moves.append(single_step)

    if piece.colour == PieceColour.WHITE:
        if not board.square_has_white_piece(take_left):
            legal_moves.append(take_left)
        if not board.square_has_white_piece(take_right):
            legal_moves.append(take_right)
    else:
        if not board.square_has_black_piece(take_left):
            legal_moves.append(take_left)
        if not board.square_has_black_piece(take_right):
            legal_moves.append(take_right)


def _knight_move_validator(board: Board, move: Move) -> bool:
    pass


def _bishop_move_validator(board: Board, move: Move) -> bool:
    pass


def _rook_move_validator(board: Board, move: Move) -> bool:
    pass


def _queen_move_validator(board: Board, move: Move) -> bool:
    pass


def _king_move_validator(board: Board, move: Move) -> bool:
    pass


def _pawn_has_not_moved(board: Board, origin: Coordinate) -> bool:
    colour = board.piece(origin).colour
    white_pawn_starting_row = 1
    black_pawn_starting_row = 6

    if (colour == PieceColour.WHITE and origin.row == white_pawn_starting_row
        or colour == PieceColour.BLACK and origin.row == black_pawn_starting_row):
        return True

    return False
