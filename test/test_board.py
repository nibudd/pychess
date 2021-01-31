import pytest
from piece import Piece
from piece_type import PieceType
from piece_colour import PieceColour
from coordinate import Coordinate
from board import Board
from board_error import EmptySquareError

empty_squares = [
    (Coordinate(2, 0)), (Coordinate(2, 1)), (Coordinate(2, 2)), (Coordinate(2, 3)), (Coordinate(2, 4)), (Coordinate(2, 5)), (Coordinate(2, 6)), (Coordinate(2, 7)),
    (Coordinate(3, 0)), (Coordinate(3, 1)), (Coordinate(3, 2)), (Coordinate(3, 3)), (Coordinate(3, 4)), (Coordinate(3, 5)), (Coordinate(3, 6)), (Coordinate(3, 7)),
    (Coordinate(4, 0)), (Coordinate(4, 1)), (Coordinate(4, 2)), (Coordinate(4, 3)), (Coordinate(4, 4)), (Coordinate(4, 5)), (Coordinate(4, 6)), (Coordinate(4, 7)),
    (Coordinate(5, 0)), (Coordinate(5, 1)), (Coordinate(5, 2)), (Coordinate(5, 3)), (Coordinate(5, 4)), (Coordinate(5, 5)), (Coordinate(5, 6)), (Coordinate(5, 7))
]

white_pieces = [
    (Coordinate(0, 0)), (Coordinate(0, 1)), (Coordinate(0, 2)), (Coordinate(0, 3)), (Coordinate(0, 4)), (Coordinate(0, 5)), (Coordinate(0, 6)), (Coordinate(0, 7)),
    (Coordinate(1, 0)), (Coordinate(1, 1)), (Coordinate(1, 2)), (Coordinate(1, 3)), (Coordinate(1, 4)), (Coordinate(1, 5)), (Coordinate(1, 6)), (Coordinate(1, 7))
]

black_pieces = [
    (Coordinate(7, 0)), (Coordinate(7, 1)), (Coordinate(7, 2)), (Coordinate(7, 3)), (Coordinate(7, 4)), (Coordinate(7, 5)), (Coordinate(7, 6)), (Coordinate(7, 7)),
    (Coordinate(6, 0)), (Coordinate(6, 1)), (Coordinate(6, 2)), (Coordinate(6, 3)), (Coordinate(6, 4)), (Coordinate(6, 5)), (Coordinate(6, 6)), (Coordinate(6, 7))
]

kings = [Coordinate(0, 4), Coordinate(7, 4)]

not_kings = [
    (Coordinate(0, 0)), (Coordinate(0, 1)), (Coordinate(0, 2)), (Coordinate(0, 3)), (Coordinate(0, 5)), (Coordinate(0, 6)), (Coordinate(0, 7)),
    (Coordinate(1, 0)), (Coordinate(1, 1)), (Coordinate(1, 2)), (Coordinate(1, 3)), (Coordinate(1, 4)), (Coordinate(1, 5)), (Coordinate(1, 6)), (Coordinate(1, 7)),
    (Coordinate(2, 0)), (Coordinate(2, 1)), (Coordinate(2, 2)), (Coordinate(2, 3)), (Coordinate(2, 4)), (Coordinate(2, 5)), (Coordinate(2, 6)), (Coordinate(2, 7)),
    (Coordinate(3, 0)), (Coordinate(3, 1)), (Coordinate(3, 2)), (Coordinate(3, 3)), (Coordinate(3, 4)), (Coordinate(3, 5)), (Coordinate(3, 6)), (Coordinate(3, 7)),
    (Coordinate(4, 0)), (Coordinate(4, 1)), (Coordinate(4, 2)), (Coordinate(4, 3)), (Coordinate(4, 4)), (Coordinate(4, 5)), (Coordinate(4, 6)), (Coordinate(4, 7)),
    (Coordinate(5, 0)), (Coordinate(5, 1)), (Coordinate(5, 2)), (Coordinate(5, 3)), (Coordinate(5, 4)), (Coordinate(5, 5)), (Coordinate(5, 6)), (Coordinate(5, 7)),
    (Coordinate(6, 0)), (Coordinate(6, 1)), (Coordinate(6, 2)), (Coordinate(6, 3)), (Coordinate(6, 4)), (Coordinate(6, 5)), (Coordinate(6, 6)), (Coordinate(6, 7)),
    (Coordinate(7, 0)), (Coordinate(7, 1)), (Coordinate(7, 2)), (Coordinate(7, 3)), (Coordinate(7, 5)), (Coordinate(7, 6)), (Coordinate(7, 7)),
]

def test_pieces_returns__pieces_dict():
    board = Board()

    assert board.pieces == board._pieces

@pytest.mark.parametrize("coordinate", white_pieces + black_pieces)
def test_piece_squares_with_pieces_return_pieces(coordinate: Coordinate):
    board = Board()

    piece = board.piece(coordinate)

    assert type(piece) == Piece

@pytest.mark.parametrize("coordinate", empty_squares)
def test_piece_empty_squares_raise_EmptySquareError(coordinate: Coordinate):
    board = Board()

    with pytest.raises(EmptySquareError):
        board.piece(coordinate)    

@pytest.mark.parametrize("coordinate", empty_squares)
def test_square_is_empty_empty_squares_returns_true(coordinate: Coordinate):
    board = Board()

    assert board.square_is_empty(coordinate) == True

@pytest.mark.parametrize("coordinate", white_pieces + black_pieces)
def test_square_is_empty_filled_squares_returns_false(coordinate: Coordinate):
    board = Board()

    assert board.square_is_empty(coordinate) == False

@pytest.mark.parametrize("coordinate", empty_squares)
def test_square_has_a_piece_empty_squares_returns_false(coordinate: Coordinate):
    board = Board()

    assert board.square_has_a_piece(coordinate) == False

@pytest.mark.parametrize("coordinate", white_pieces + black_pieces)
def test_square_has_a_piece_filled_squares_returns_true(coordinate: Coordinate):
    board = Board()

    assert board.square_has_a_piece(coordinate) == True

@pytest.mark.parametrize("coordinate", white_pieces)
def test_square_has_white_piece_white_pieces_returns_true(coordinate: Coordinate):
    board = Board()

    assert board.square_has_white_piece(coordinate) == True

@pytest.mark.parametrize("coordinate", empty_squares + black_pieces)
def test_square_has_white_piece_black_pieces_or_empty_returns_false(coordinate: Coordinate):
    board = Board()

    assert board.square_has_white_piece(coordinate) == False

@pytest.mark.parametrize("coordinate", black_pieces)
def test_square_has_black_piece_black_pieces_returns_true(coordinate: Coordinate):
    board = Board()

    assert board.square_has_black_piece(coordinate) == True

@pytest.mark.parametrize("coordinate", empty_squares + white_pieces)
def test_square_has_black_piece_white_pieces_or_empty_returns_false(coordinate: Coordinate):
    board = Board()

    assert board.square_has_black_piece(coordinate) == False

@pytest.mark.parametrize("coordinate", kings)
def test_square_has_king_king_returns_true(coordinate):
    board = Board()

    assert board.square_has_king(coordinate) == True

@pytest.mark.parametrize("coordinate", not_kings)
def test_square_has_king_not_king_returns_false(coordinate):
    board = Board()

    assert board.square_has_king(coordinate) == False