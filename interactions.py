""" This module acts as the input/output interface for the players. """


def request_move(*args):
    """ Asks the user for input in order to make a move. """
    print(
        'Example: E2E4 moves the piece on E2 to E4. You can use lower ' +
        'case.\n'
    )
    if len(args) == 0:
        move = input('Please enter your move: ')
    else:
        move = args[0]

    return move.lower().strip()
