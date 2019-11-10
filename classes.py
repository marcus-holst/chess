""" This module defines all classes in the game. """
from typing import List, Dict, Generator
import numpy as np
import matplotlib.pyplot as plt


"""
*******************************************************************************
                               Squares and moves
*******************************************************************************
"""


class Square:
    """ A single position on the board. It translates user input such as "A1"
    to col = 0 and row = 0. Has two properties: col and row.  """
    col_map = {letter: i for i, letter in enumerate('abcdefgh')}
    row_map = {num: int(num) - 1 for num in '12345678'}
    # TODO should this take in the user string? If so, move the col_map and
    row_map
    # from the Move class.
    # TODO should it also (can it?) contain information about the piece
    # occupying the spot?

    def __init__(self, user_input: str = None):
        # We need to create empty moves for the en passant and the last move,
        # for its first initiation
        if user_input is None:
            self.row = ''
            self.col = ''
        else:
            self.row = Square.row_map[user_input[1]]
            self.col = Square.col_map[user_input[0]]

    def get_coordinates(self):
        """ Returns the row (y) and then the column (x) for the square. """
        return [self.row, self.col]


class Move:
    """ Carries information from the user input to the board.
    A move is always in <letter><number><letter><number> format, indicating the
    position to move from and the position to move to. """

    def __init__(self, user_input: str):
        """ Used to have "start_x" and "start_y" etc. Was replaced by the
        square class to simplify. """
        self.start = Square(user_input[:2])
        self.end = Square(user_input[2:])
        self.squares = [self.start, self.end]
        self.delta_rows = (1 + self.end.row) - (1 + self.start.row)
        self.delta_cols = (1 + self.end.col) - (1 + self.start.col)

    def get_coordinates(self):
        """ Returns y and x coordinates of start and end position as two lists.
        """

        return [square.get_coordinates() for square in self.squares]


"""
*******************************************************************************
                                   Pieces
*******************************************************************************
"""
# Reference for markers  https://matplotlib.org/3.1.1/api/markers_api.html


class Piece:
    colors = {
        'white': '#b4b3bd',
        'black': '#8f1a1a',
    }
    markers = {
        'pawn': '^',
        'rook': 's',
        'knight': '1',
        'bishop': 'd',
        'queen': '*',
        'king': '+',
    }
    values = {
        'pawn': 1,
        'rook': 5,
        'knight': 3,
        'bishop': 3,
        'queen': 9,
        'king': 0,
    }
    size = 150

    def __init__(self, piece_type: str, team: str):
        self.type = piece_type
        self.team = team
        self.color = self.colors[team]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def verify_move(self, *args, **kwargs):
        """ Placeholder for the piece-specific verification methods. """
        pass

    def __repr__(self):

        if hasattr(self, 'type'):

            return self.type
        else:

            return 'piece archetype'


class Pawn(Piece):

    def __init__(self, team):
        super(Pawn, self).__init__('pawn', team)

    def verify_move(
        self,
        move: Move,
        captured_piece: Piece,
    ) -> bool:
        # Adding 1 to avoid dealing with the y and x intersects (at y or x = 0)
        delta_cols = move.delta_cols
        delta_rows = move.delta_rows

        if captured_piece == '' and delta_cols != 0:
            # No team can move diagonally unless there's a capture

            return False

        if delta_cols == 0 and captured_piece != '':
            # Cannot capture by walking straight

            return False

        if self.team == 'white' and delta_rows < 1:
            # White must advance

            return False

        if self.team == 'black' and delta_rows > -1:
            # Black advances down the y axis

            return False

        if abs(delta_rows) == 2 and (
                move.start.row == 1 or move.start.row == 6
                ):
            # 2 moves along y-axis only allowed from starting row
            # We've already checked that each team moves the right direction

            return True

        if abs(delta_rows) == 1:

            return True

        # Catch-all
        return False


class Rook(Piece):

    def __init__(self, team):
        super(Rook, self).__init__('rook', team)


class Bishop(Piece):

    def __init__(self, team):
        super(Bishop, self).__init__('bishop', team)


class Knight(Piece):

    def __init__(self, team):
        super(Knight, self).__init__('knight', team)


class Queen(Piece):

    def __init__(self, team):
        super(Queen, self).__init__('queen', team)


class King(Piece):

    def __init__(self, team):
        super(King, self).__init__('king', team)


"""
*******************************************************************************
                                   Positions
*******************************************************************************
"""


class Positions:
    """ Class containing information about the current positions on the playing
    board. The positions can be accessed both as a list of pieces and as a
    coordinate system of ones and zeros. """
    starting_positions = [
        [
            Rook('white'),
            Knight('white'),
            Bishop('white'),
            Queen('white'),
            King('white'),
            Bishop('white'),
            Knight('white'),
            Rook('white'),
        ],
        [
            Pawn('white'),
            Pawn('white'),
            Pawn('white'),
            Pawn('white'),
            Pawn('white'),
            Pawn('white'),
            Pawn('white'),
            Pawn('white'),
        ],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        [
            Pawn('black'),
            Pawn('black'),
            Pawn('black'),
            Pawn('black'),
            Pawn('black'),
            Pawn('black'),
            Pawn('black'),
            Pawn('black'),
        ],
        [
            Rook('black'),
            Knight('black'),
            Bishop('black'),
            Queen('black'),
            King('black'),
            Bishop('black'),
            Knight('black'),
            Rook('black'),
        ],
    ]

    def __init__(self):
        self.positions = Positions.starting_positions
        self.coordinates = [
            [1 if x != '' else 0 for x in row]
            for row in Positions.starting_positions
        ]

    def get_positions(self) -> List[List[Piece]]:
        """ Returns the nested list of pieces that make up the current
        playing board. """

        return self.positions

    def check_positions(
        self,
        move: Move
    ) -> Dict[str, Piece]:
        """ Used to get information that will help verify that the move is
        allowed. Returns the piece on the starting square, the piece on the
        destination square as well as any pieces in between (if piece is not a
        horse). """
        piece_start = self.positions[move.start.row][move.start.col]
        if piece_start.type != 'knight':
            # TODO Do the check of blocking pieces
            # If there are pieces in between, return error
            # Something can be done by taking the x1 - x2 and y1-y2
            pass
        piece_end = self.positions[move.end.row][move.end.col]

        return {'piece_start': piece_start, 'piece_end': piece_end}

    def update_positions(self, move: Move) -> List[int]:
        """ Takes the piece from the starting position and puts it at the end
        position. Returns the end positions. """
        piece = self.positions[move.start.row][move.start.col]
        self.positions[move.start.row][move.start.col] = ''
        self.positions[move.end.row][move.end.col] = piece

        return move.end.get_coordinates()

    def get_coordinates(self):
        """ Returns the nested list representing where there are pieces (1's)
        and which squares are empty (0's). """

        return self.coordinates

    def en_passant_capture(
        self,
        last_move_end: List[int]
    ) -> Piece:
        """ Executes the en_passant capture. The actual move will be done in
        the update_positions function. """
        captured_piece = self.positions[last_move_end[1]][last_move_end[0]]
        self.positions[last_move_end[1]][last_move_end[0]] = ''

        return captured_piece


"""
*******************************************************************************
                                     Board
*******************************************************************************
"""


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
            positions: List[List[Piece]],
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
                Y.append(position[0])
                X.append(position[1])
            self.board['board'].plot(X, Y, c='blue')
        plt.show()
        # self.board['fig'].canvas.draw()

    def show_board(self):
        """ Shows the figure. """
        plt.show()
        # self.board['fig'].canvas.draw()


"""
*******************************************************************************
                                    Players
*******************************************************************************
"""


class Player:
    """ The class is used to keep track of name, team and the points in the
    game. """
    teams = ['white', 'black']

    def __init__(self, name: str):
        self.name = name
        self.team = ''
        self.points = 0

    def assign_first_team(self):
        """ Randomly assigns a team to the player and returns the other colour,
        to be assigned to the other player. """
        idx = np.random.randint(2, size=1)[0]
        team = Player.teams[idx]
        self.team = team

        return Player.teams[idx - 1]

    def assign_second_team(self, team: str):
        """ Assigns the provided team as the player's team. The team of the
        first player is generated with the function Player.assign_first_team.
        """
        self.team = team

    def add_points(self, points: int) -> int:
        """ Add points after a piece has been captured. Returns current points.
        """
        self.points += points

        return self.points

    def __repr__(self):
        """ The class is described with the player name. """

        return self.name


def player_queue(players: List[Player]) -> Generator[Player, None, None]:
    """ Orders the players with the white team first and then creates an
    infinite queue. """
    for player in players:
        if player.team == 'white':
            first_player = player
        else:
            second_player = player
    queue = ['', first_player, second_player]
    i = 1
    while True:
        yield queue[i]
        i = i * -1
