""" Describes the properties of the pieces.
"""
# Reference for markers  https://matplotlib.org/3.1.1/api/markers_api.html
class Piece:
    colors = {
        'white': '#b4b3bd',
        'black': '#8f1a1a',
    }
    markers = {
        'pawn': '^',
        'tower': 's',
        'knight': '1',
        'bishop': 'd',
        'queen': '*',
        'king': '+',
    }
    values = {
        'pawn': 1,
        'tower': 5,
        'knight': 3,
        'bishop': 3,
        'queen': 9,
        'king': 0,
    }
    size = 150

    def __repr__(self):

        if hasattr(self, 'type'):

            return self.type
        else:

            return 'piece archetype'


class Pawn(Piece):

    def __init__(self, color):
        self.type = 'pawn'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]


class Tower(Piece):

    def __init__(self, color):
        self.type = 'tower'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]


class Bishop(Piece):

    def __init__(self, color):
        self.type = 'bishop'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]


class Knight(Piece):

    def __init__(self, color):
        self.type = 'knight'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]


class Queen(Piece):

    def __init__(self, color):
        self.type = 'queen'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]


class King(Piece):

    def __init__(self, color):
        self.type = 'king'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]


pawn = Pawn('white')
print(pawn)
piece = Piece()
print(piece)
