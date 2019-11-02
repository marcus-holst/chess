""" This module includes the controls and checks that make sure the game rules
are being followed. """
import re


def check_only_valid_characters(move_string):
    """ Checks that the input follows the convention
    <letter><number><letter><number> and that letters are only a-h and numbers
    1-8. """

    if re.match('[ah][1-8][ah][1-8]$', move_string):

        return True

    return False
