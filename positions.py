""" This module controls the positions of the board, which keeps all the pieces
as well as the classes for squares and moves. """
from typing import List, Dict
import pieces


class Positions:
    """ Class containing information about the current positions on the playing
    board. The positions can be accessed both as a list of pieces and as a
    coordinate system of ones and zeros. """
    starting_positions = [
        [
            pieces.Rook('white'),
            pieces.Knight('white'),
            pieces.Bishop('white'),
            pieces.Queen('white'),
            pieces.King('white'),
            pieces.Bishop('white'),
            pieces.Knight('white'),
            pieces.Rook('white'),
        ],
        [
            pieces.Pawn('white'),
            pieces.Pawn('white'),
            pieces.Pawn('white'),
            pieces.Pawn('white'),
            pieces.Pawn('white'),
            pieces.Pawn('white'),
            pieces.Pawn('white'),
            pieces.Pawn('white'),
        ],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        [
            pieces.Pawn('black'),
            pieces.Pawn('black'),
            pieces.Pawn('black'),
            pieces.Pawn('black'),
            pieces.Pawn('black'),
            pieces.Pawn('black'),
            pieces.Pawn('black'),
            pieces.Pawn('black'),
        ],
        [
            pieces.Rook('black'),
            pieces.Knight('black'),
            pieces.Bishop('black'),
            pieces.Queen('black'),
            pieces.King('black'),
            pieces.Bishop('black'),
            pieces.Knight('black'),
            pieces.Rook('black'),
        ],
    ]

    def __init__(self):
        self.positions = Positions.starting_positions
        self.coordinates = [
            [1 if x != '' else 0 for x in row]
            for row in Positions.starting_positions
        ]

    def get_positions(self) -> List[List[pieces.Piece]]:
        """ Returns the nested list of pieces that make up the current
        playing board. """

        return self.positions

    def check_positions(
        self,
        move: List[List[int]]
    ) -> Dict[str, pieces.Piece]:
        """ Used to get information that will help verify that the move is
        allowed. Returns the piece on the starting square, the piece on the
        destination square as well as any pieces in between (if piece is not a
        horse). """
        piece_start = self.positions[move[0][1]][move[0][0]]
        if piece_start.type != 'knight':
            # Do the check of blocking pieces
            # If there are pieces in between, return error
            # Something can be done by taking the x1 - x2 and y1-y2
            pass
        piece_end = self.positions[move[1][1]][move[1][0]]

        return {'piece_start': piece_start, 'piece_end': piece_end}

    def update_positions(self, move: List[List[int]]) -> List[int]:
        """ Takes the piece from the starting position and puts it at the end
        position. Returns the end positions. """
        piece = self.positions[move[0][1]][move[0][0]]
        self.positions[move[0][1]][move[0][0]] = ''
        self.positions[move[1][1]][move[1][0]] = piece

        return move[1]

    def get_coordinates(self):
        """ Returns the nested list representing where there are pieces (1's)
        and which squares are empty (0's). """

        return self.coordinates

    def en_passant_capture(
        self,
        last_move_end: List[int]
    ) -> pieces.Piece:
        """ Executes the en_passant capture. The actual move will be done in
        the update_positions function. """
        captured_piece = self.positions[last_move_end[1]][last_move_end[0]]
        self.positions[last_move_end[1]][last_move_end[0]] = ''

        return captured_piece


class Square:
    """ A single position on the board. """
    def __init__(self):
        self.row = ''
        self.col = ''

    def set_coordinates(self, row, col):
        self.row = row
        self.col = col


class Move:
    """ Carries information from the user input to the board.
    A move is always in <letter><number><letter><number> format, indicating the
    position to move from and the position to move to. """
    x_map = {letter: i for i, letter in enumerate('abcdefgh')}
    y_map = {num: int(num) - 1 for num in '12345678'}

    def __init__(self, user_input: str):
        self.start_x = Move.x_map[user_input[0]]
        self.start_y = Move.y_map[user_input[1]]
        self.end_x = Move.x_map[user_input[2]]
        self.end_y = Move.y_map[user_input[3]]

    def get_coordinates(self):
        """ Returns x and y coordinates of start and end position as two lists.
        """

        return [[self.start_x, self.start_y], [self.end_x, self.end_y]]


