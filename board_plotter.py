import matplotlib.pyplot as plt

from board import Board
from coordinate import Coordinate
from piece import Piece
from piece_type import PieceType
from piece_colour import PieceColour

def plot_board(board : Board):
    _, axs = plt.subplots()
    _plot_pieces(axs, board)
    _colour_squares(axs)
    axs.axis('equal')
    axs.set_aspect('equal', 'box')
    axs.axis([0, 8, 0, 8])
    plt.show()

def _colour_squares(axs):
    for x in range(0, 8, 2):
        for y in range(0, 8, 1):
            xx = x + y%2
            axs.fill([xx, xx, xx+1, xx+1], [y, y+1, y+1, y], "k")

def _plot_pieces(axs, board: Board):
    for coordinate, piece in board.pieces.items():
        y = coordinate.row + 0.5
        x = coordinate.col + 0.5
        marker = marker_shape_map[piece.type]
        colour = marker_colour_map[piece.colour]
        axs.plot(x, y, marker=marker, color=colour, markersize=20)

marker_colour_map = {
    PieceColour.BLACK: "#303030",
    PieceColour.WHITE: "#e3e3e3"
}

marker_shape_map = {
    PieceType.PAWN: "o",
    PieceType.ROOK: "s",
    PieceType.BISHOP: "d",
    PieceType.KNIGHT: "p",
    PieceType.KING: "P",
    PieceType.QUEEN: "*"
}

if __name__ == "__main__":
    plot_board(Board())