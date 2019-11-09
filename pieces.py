""" Describes the properties of the pieces.  """
from typing import List


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
        move_coordinates: List[List[int]],
        captured_piece: Piece,
    ) -> bool:
        start_pos, end_pos = move_coordinates
        # Adding 1 to avoid dealing with the y and x intersects (at y or x = 0)
        delta_x = (1 + end_pos[0]) - (1 + start_pos[0])
        delta_y = (1 + end_pos[1]) - (1 + start_pos[1])

        if captured_piece == '' and delta_x != 0:
            # No team can move diagonally unless there's a capture

            return False

        if delta_x == 0 and captured_piece != '':
            # Cannot capture by walking straight
            return False

        if self.team == 'white' and delta_y < 1:
            # White must advance
            return False

        if self.team == 'black' and delta_y > -1:
            # Black advances down the y axis
            return False

        if abs(delta_y) == 2 and (start_pos[1] == 1 or start_pos[1] == 6):
            # 2 moves along y-axis only allowed from starting row
            # We've already checked that each team moves the right direction
            return True

        if abs(delta_y) == 1:
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
