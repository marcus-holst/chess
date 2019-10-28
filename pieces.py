# Reference for markers  https://matplotlib.org/3.1.1/api/markers_api.html
class Piece:

    def __init__(self):
        self.colors = {
                'white': '#b4b3bd',
                'black': '#8f1a1a',
                }
        self.markers = {
                'pawn': '^',
                'tower': 's',
                'knight': '1',
                'bishop': 'd',
                'queen': '*',
                'king': '+',
                }
        self.values = {
                'pawn': 1,
                'tower': 5,
                'knight': 3,
                'bishop': 3,
                'queen': 9,
                'king': 0,
                }
        self.size = 150


class Pawn(Piece):

    def __init__(self, color):
        Piece.__init__(self)
        self.type = 'pawn'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def __repr__(self):

        return self.type


class Tower(Piece):

    def __init__(self, color):
        Piece.__init__(self)
        self.type = 'tower'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def __repr__(self):

        return self.type


class Bishop(Piece):

    def __init__(self, color):
        Piece.__init__(self)
        self.type = 'bishop'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def __repr__(self):

        return self.type


class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self)
        self.type = 'knight'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def __repr__(self):

        return self.type


class Queen(Piece):

    def __init__(self, color):
        Piece.__init__(self)
        self.type = 'queen'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def __repr__(self):

        return self.type


class King(Piece):

    def __init__(self, color):
        Piece.__init__(self)
        self.type = 'king'
        self.color = self.colors[color]
        self.marker = self.markers[self.type]
        self.value = self.values[self.type]

    def __repr__(self):

        return self.type


