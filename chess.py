from typing import List
# Classes for pieces


class Pawn:

    def __init__(
        self,
        start_position: List[List[int]],
        colour: str
    ):
        """ Initialises the piece. Decides which color it has."""
        self.position = start_position
        self.colour = colour
        self.symbol = 'p'

    def move(self, target_position: str):

        if target_position[0] != self.position[0]:

            return False


"""
Class for the board
The board should be a coordinate system of rows and columns
It needs a render function.
It needs to keep a state of the positions of all pieces.
"""
