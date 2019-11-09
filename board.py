""" Controls the drawing of the main playing board. """
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt
import pieces


def _create_board_background() -> List[int]:
    """ Creates an 8x8 matrix of 1's and 0's, which will colour the main
    background of the board."""
    # 0 is white
    board = []
    for value in range(1, 9):
        if value % 2 == 0:
            row = [0, 1] * 4
        else:
            row = [1, 0] * 4
        board.append(row)

    return board


def _remove_ax_elements(
        ax: plt.Axes,
        ticks: bool,
        spines: bool) -> plt.Axes:
    """ Removes x and y tick marks as well as all spines. """
    if ticks:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.tick_params(
            axis='both', which='both', bottom=False,
            top=False, left=False, right=False
        )

    if spines:
        ax.spines['right'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_color('none')

    return ax


def _create_board() -> Dict:
    """ Creates the main matplotlib figure for the board and its
    coordinates. Returns the figure and the axes as a dictionary. """
    background = _create_board_background()

    plt.ion()
    fig = plt.figure(figsize=(4.5, 4.5), dpi=150)
    # Using gridspec to be able to control the layout of the two axes
    # that hold coordinates.
    grid_spec = plt.GridSpec(
        nrows=2, ncols=2, figure=fig, width_ratios=[0.1, 0.9],
        height_ratios=[0.1, 0.9], wspace=0.03, hspace=0.03
    )
    ax_cols = fig.add_subplot(grid_spec[0, 1])
    ax_rows = fig.add_subplot(grid_spec[1, 0])
    ax_board = fig.add_subplot(grid_spec[1, 1])

    # Setting up main board
    ax_board.matshow(background, cmap='Greys')
    ax_board.set_xticks([])
    ax_board.set_yticks([])

    # Making sure the first and last squares are fully visible
    ax_board.set_ylim(bottom=-0.5, top=7.5)

    # Fixing columns
    X = np.arange(1.5, 9.5)
    Y = np.zeros(8)

    ax_cols.set_xticks([])
    ax_cols.set_yticks([])

    i = 0
    labels = 'abcdefgh'
    for x, y in zip(X, Y):
        ax_cols.text(
            x, y, labels[i], ha='center', va='bottom', fontsize=8
        )
        i += 1
    ax_cols.set_xlim(1, 9)
    ax_cols.set_ylim(bottom=0, top=2)

    # Fixing rows
    Y = np.arange(1.5, 9)
    X = np.zeros(8)

    i = 0
    labels = '123456789'
    for x, y in zip(X, Y):
        ax_rows.text(x, y, labels[i], ha='center', va='center', fontsize=8)
        i += 1
    ax_rows.set_xlim(-1, 1)
    ax_rows.set_ylim(bottom=1.1, top=9.1)

    ax_rows = _remove_ax_elements(ax_rows, True, True)
    ax_cols = _remove_ax_elements(ax_cols, True, True)
    ax_board = _remove_ax_elements(ax_board, True, False)
    fig.suptitle('Chess')

    return {
            'fig': fig,
            'board': ax_board,
            'rows': ax_cols,
            'cols': ax_cols
            }


class Board:
    """ The main board class.
    Properties:
        self.board: the fig and ax objects of the board.
    Methods:
        self.update_board(): draws an updated board.
    """
    def __init__(self):
        self.board = _create_board()

    def update_board(
            self,
            positions: List[List[pieces.Piece]],
            last_move: List[List[int]] = []
            ) -> plt.Axes:
        """ Updates the ax_board with the provided positions.
        Input: positions is a Position class with all pieces.
        last_move is a 2d list with x, y coordinates for the start and end
        positions. """
        plt.close()
        self.board = _create_board()
        for y, row in enumerate(positions):
            for x, piece in enumerate(row):
                if piece != '':
                    self.board['board'].scatter(
                        x, y, marker=piece.marker,
                        c=piece.color, s=piece.size, label=piece.type
                    )
                    X = []
        Y = []

        if last_move:
            for position in last_move:
                X.append(position[0])
                Y.append(position[1])
            self.board['board'].plot(X, Y, c='blue')
        plt.show()
        # self.board['fig'].canvas.draw()

    def show_board(self):
        """ Shows the figure. """
        plt.show()
        # self.board['fig'].canvas.draw()
