from typing import List
import pieces


class Positions:
    """ Class containing information about the current positions on the playing
    board. The positions can be accessed both as a list of pieces and as a
    coordinate system of ones and zeros. """
    starting_positions = [
        [
            pieces.Tower('white'),
            pieces.Knight('white'),
            pieces.Bishop('white'),
            pieces.Queen('white'),
            pieces.King('white'),
            pieces.Bishop('white'),
            pieces.Knight('white'),
            pieces.Tower('white'),
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
            pieces.Tower('black'),
            pieces.Knight('black'),
            pieces.Bishop('black'),
            pieces.Queen('black'),
            pieces.King('black'),
            pieces.Bishop('black'),
            pieces.Knight('black'),
            pieces.Tower('black'),
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

    def update_positions(self, move: List[List[int]]):
        """ Takes the piece from the starting position and puts it at the end
        position. """
        piece = self.positions[move[0][1]][move[0][0]]
        self.positions[move[0][1]][move[0][0]] = ''
        self.positions[move[1][1]][move[1][0]] = piece

    def get_coordinates(self):
        """ Returns the nested list representing where there are pieces (1's)
        and which squares are empty (0's). """

        return self.coordinates
