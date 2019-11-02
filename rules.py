""" This module controls the behaviour of the pieces and makes sure that only
legal moves are done. """


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
