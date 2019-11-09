""" This module includes the controls and checks that make sure the game rules
are being followed. """
import re
from typing import List
from pieces import Piece


def check_only_valid_characters(move_string):
    """ Checks that the input follows the convention
    <letter><number><letter><number> and that letters are only a-h and numbers
    1-8. """

    if re.match('^[a-h][1-8][a-h][1-8]$', move_string):

        return True

    return False


def check_team_and_capture(
        player_team: str,
        piece_team: str,
        captured_piece: Piece
        ) -> bool:
    """ Checks that the player team is equal to the moved piece's team and that
    the piece that currently is placed on the end position is not of the same
    team. Prints the error message and returns False for invalid moves and True
    for valid ones. """
    if player_team != piece_team:
        print('You cannot move a piece of the other team!')
        return False

    if captured_piece != '':
        if player_team == captured_piece.team:
            print('Destination square already occupied by one of your pieces.')
            return False

    return True


def check_en_passant(
        move_piece_type: str,
        end_position: List[int],
        en_passant_position: List[int]
) -> bool:
    """ Checks whether the moved piece is a pawn and if it's moving to an
    eligible en passant position (basically if it was passed by the opponent's
    pawn, which was moving two squares) """
    if move_piece_type == 'pawn' and end_position == en_passant_position:
        return True
    return False


def update_en_passant_position(
    move_piece_type: str,
    move_coordinates: List[List[int]]
) -> List[int]:
    """ Checks if the last moved piece was a pawn and the absolute distance
    travelled along the x axis was 2. It then returns the position between the
    start and end position on the y axis. """
    start_move, end_move = move_coordinates
    delta_y = (1 + end_move[1]) - (1 + start_move[1])
    if move_piece_type == 'pawn' and abs(delta_y) == 2:
        if delta_y > 0:
            return [end_move[0], end_move[1] - 1]
        else:
            return [end_move[0], end_move[1] + 1]

    return ['', '']
